#!/usr/bin/env python3
"""
Audio Engine for Interview Whisperer
Real-time audio capture and transcription using Whisper

Optimized for M3 Mac with fast, efficient processing.
"""

import threading
import queue
import time
import numpy as np
import sounddevice as sd
import whisper
from typing import Callable, Dict, Optional, Tuple
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class AudioConfig:
    """Audio configuration parameters."""
    sample_rate: int = 16000  # Whisper standard
    channels: int = 1  # Mono
    chunk_duration: float = 5.0  # Seconds per transcription chunk
    silence_threshold: float = 0.01  # Amplitude threshold for silence
    silence_duration: float = 1.5  # Seconds of silence after question
    context_duration: float = 30.0  # Seconds of context to keep


class AudioEngine:
    """
    Real-time audio capture and transcription engine using Whisper.

    Features:
    - Non-blocking audio capture
    - Chunked transcription (5-second intervals)
    - Question detection (ends with "?")
    - Context accumulation (30 seconds)
    - Thread-safe operations
    """

    def __init__(self, model: str = "base", language: str = "en", config: Optional[AudioConfig] = None):
        """
        Initialize the audio engine.

        Args:
            model: Whisper model size ("tiny", "base", "small", "medium", "large")
                  "base" is recommended for M3 Mac (fast + accurate enough)
            language: Language code for transcription ("en" for English)
            config: Optional custom AudioConfig. If None, uses defaults.
        """
        self.config = config if config is not None else AudioConfig()
        self.language = language
        self.model_name = model

        # State
        self._is_listening = False
        self._audio_thread: Optional[threading.Thread] = None
        self._transcription_thread: Optional[threading.Thread] = None
        self._stop_event = threading.Event()

        # Audio buffers
        self._audio_queue: queue.Queue = queue.Queue()
        self._audio_buffer = []

        # Transcription state
        self._callback: Optional[Callable[[str, bool], None]] = None
        self._transcript_history = []  # Last 30 seconds
        self._chunks_processed = 0
        self._current_audio_level = 0.0
        self._last_speech_time = 0.0

        # Load Whisper model
        logger.info(f"Loading Whisper model '{model}'...")
        try:
            self.model = whisper.load_model(model)
            logger.info(f"✓ Whisper model '{model}' loaded successfully")
        except Exception as e:
            logger.error(f"✗ Failed to load Whisper model: {e}")
            raise RuntimeError(f"Failed to load Whisper model '{model}': {e}")

    def start_listening(self, callback: Callable[[str, bool], None]) -> None:
        """
        Start capturing and transcribing audio.

        Args:
            callback: Function called with (text: str, is_question: bool)
                     when new transcription is available

        Raises:
            RuntimeError: If already listening or microphone unavailable
        """
        if self._is_listening:
            raise RuntimeError("Already listening. Stop before starting again.")

        self._callback = callback
        self._stop_event.clear()
        self._is_listening = True
        self._chunks_processed = 0
        self._transcript_history = []

        # Start audio capture thread
        self._audio_thread = threading.Thread(
            target=self._audio_capture_loop,
            daemon=True,
            name="AudioCapture"
        )
        self._audio_thread.start()

        # Start transcription thread
        self._transcription_thread = threading.Thread(
            target=self._transcription_loop,
            daemon=True,
            name="Transcription"
        )
        self._transcription_thread.start()

        logger.info("🎤 Audio engine started")

    def stop_listening(self) -> None:
        """Stop audio capture and transcription."""
        if not self._is_listening:
            return

        logger.info("Stopping audio engine...")
        self._is_listening = False
        self._stop_event.set()

        # Wait for threads to finish
        if self._audio_thread and self._audio_thread.is_alive():
            self._audio_thread.join(timeout=2.0)
        if self._transcription_thread and self._transcription_thread.is_alive():
            self._transcription_thread.join(timeout=2.0)

        # Clear queues
        while not self._audio_queue.empty():
            try:
                self._audio_queue.get_nowait()
            except queue.Empty:
                break

        self._audio_buffer = []
        logger.info("🛑 Audio engine stopped")

    def update_config(self, config: AudioConfig) -> None:
        """
        Update audio configuration.

        Note: Must call stop_listening() before updating config.
        Changes take effect on next start_listening() call.

        Args:
            config: New AudioConfig to use

        Raises:
            RuntimeError: If currently listening
        """
        if self._is_listening:
            raise RuntimeError("Cannot update config while listening. Call stop_listening() first.")

        self.config = config
        logger.info(f"Audio config updated: sensitivity={config.silence_threshold}, chunk={config.chunk_duration}s")

    def get_status(self) -> Dict[str, any]:
        """
        Get current engine status.

        Returns:
            Dictionary with:
            - is_listening: bool
            - audio_level: float (0.0 to 1.0)
            - chunks_processed: int
            - model: str
        """
        return {
            'is_listening': self._is_listening,
            'audio_level': self._current_audio_level,
            'chunks_processed': self._chunks_processed,
            'model': self.model_name,
            'language': self.language
        }

    def _audio_capture_loop(self) -> None:
        """
        Audio capture loop (runs in background thread).
        Captures microphone input and queues chunks for transcription.
        """
        chunk_samples = int(self.config.sample_rate * self.config.chunk_duration)
        buffer = []

        def audio_callback(indata, frames, time_info, status):
            """Called by sounddevice for each audio block."""
            if status:
                logger.warning(f"Audio callback status: {status}")

            # Calculate audio level (RMS)
            audio_data = indata[:, 0]  # Get mono channel
            self._current_audio_level = float(np.sqrt(np.mean(audio_data**2)))

            # Add to buffer
            buffer.extend(audio_data)

            # If buffer reaches chunk size, queue it for transcription
            if len(buffer) >= chunk_samples:
                chunk = np.array(buffer[:chunk_samples], dtype=np.float32)
                buffer[:] = buffer[chunk_samples:]  # Keep remainder

                try:
                    self._audio_queue.put(chunk, block=False)
                except queue.Full:
                    logger.warning("Audio queue full, dropping chunk")

        try:
            with sd.InputStream(
                samplerate=self.config.sample_rate,
                channels=self.config.channels,
                callback=audio_callback,
                blocksize=1024
            ):
                logger.info("✓ Microphone capture started")
                while not self._stop_event.is_set():
                    time.sleep(0.1)
        except Exception as e:
            logger.error(f"✗ Audio capture error: {e}")
            self._is_listening = False

    def _transcription_loop(self) -> None:
        """
        Transcription loop (runs in background thread).
        Processes queued audio chunks with Whisper.
        """
        while not self._stop_event.is_set():
            try:
                # Get audio chunk (timeout to check stop event)
                audio_chunk = self._audio_queue.get(timeout=0.5)
            except queue.Empty:
                continue

            # Transcribe
            try:
                text = self._transcribe_chunk(audio_chunk)
                if text:
                    is_question = self._detect_question(text)

                    # Update history
                    self._transcript_history.append({
                        'text': text,
                        'timestamp': time.time(),
                        'is_question': is_question
                    })
                    self._cleanup_history()

                    # Call callback
                    if self._callback:
                        self._callback(text, is_question)

                    self._chunks_processed += 1

                    if is_question:
                        logger.info(f"❓ Detected question: {text}")
                    else:
                        logger.debug(f"💬 Transcribed: {text}")

            except Exception as e:
                logger.error(f"✗ Transcription error: {e}")

    def _transcribe_chunk(self, audio_chunk: np.ndarray) -> str:
        """
        Transcribe an audio chunk using Whisper.

        Args:
            audio_chunk: Audio data as numpy array

        Returns:
            Transcribed text (empty string if no speech detected)
        """
        try:
            # Whisper expects float32 audio
            if audio_chunk.dtype != np.float32:
                audio_chunk = audio_chunk.astype(np.float32)

            # Check if chunk has meaningful audio
            if np.max(np.abs(audio_chunk)) < self.config.silence_threshold:
                return ""  # Silence

            # Transcribe
            result = self.model.transcribe(
                audio_chunk,
                language=self.language,
                fp16=False,  # Use FP32 for M-series Macs
                verbose=False
            )

            text = result['text'].strip()
            return text

        except Exception as e:
            logger.error(f"Transcription failed: {e}")
            return ""

    def _detect_question(self, text: str) -> bool:
        """
        Detect if text is a question.

        Args:
            text: Transcribed text

        Returns:
            True if text appears to be a question
        """
        if not text:
            return False

        # Simple heuristics
        text_lower = text.lower().strip()

        # Ends with question mark
        if text.endswith('?'):
            return True

        # Starts with question words
        question_words = ['what', 'why', 'how', 'when', 'where', 'who', 'which', 'can', 'could', 'would', 'should', 'is', 'are', 'do', 'does', 'did']
        first_word = text_lower.split()[0] if text_lower.split() else ""

        if first_word in question_words:
            # Check for silence after (indicates end of question)
            current_time = time.time()
            if current_time - self._last_speech_time > self.config.silence_duration:
                return True

        self._last_speech_time = time.time()
        return False

    def _cleanup_history(self) -> None:
        """Remove transcript history older than context duration."""
        cutoff_time = time.time() - self.config.context_duration
        self._transcript_history = [
            item for item in self._transcript_history
            if item['timestamp'] > cutoff_time
        ]

    def get_recent_context(self, duration: float = 30.0) -> str:
        """
        Get recent transcript context.

        Args:
            duration: Seconds of history to return

        Returns:
            Concatenated transcript text
        """
        cutoff_time = time.time() - duration
        recent = [
            item['text'] for item in self._transcript_history
            if item['timestamp'] > cutoff_time
        ]
        return " ".join(recent)

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.stop_listening()

    def __del__(self):
        """Cleanup on deletion."""
        if self._is_listening:
            self.stop_listening()


# ============================================================================
# TEST SCRIPT
# ============================================================================

if __name__ == "__main__":
    import sys

    print("=" * 60)
    print("🎤 Interview Whisperer - Audio Engine Test")
    print("=" * 60)
    print()
    print("This will capture your microphone and transcribe in real-time.")
    print("Speak naturally and ask questions (ending with '?')")
    print()
    print("Press Ctrl+C to stop.")
    print()

    # Callback for transcripts
    def print_transcript(text: str, is_question: bool) -> None:
        """Print transcribed text with visual markers."""
        marker = "❓ QUESTION" if is_question else "💬 Speech"
        timestamp = time.strftime("%H:%M:%S")
        print(f"[{timestamp}] {marker}: {text}")
        print()

    try:
        # Initialize engine
        print("Loading Whisper model (this may take a moment)...")
        engine = AudioEngine(model="base", language="en")

        # Start listening
        print("✓ Model loaded. Starting audio capture...")
        print()
        engine.start_listening(print_transcript)

        # Run until interrupted
        while True:
            time.sleep(1)
            status = engine.get_status()

            # Show audio level as visual bar
            level = status['audio_level']
            bar_length = int(level * 50)
            bar = "█" * bar_length + "░" * (50 - bar_length)

            sys.stdout.write(f"\r🎚️  Audio Level: {bar} | Chunks: {status['chunks_processed']}")
            sys.stdout.flush()

    except KeyboardInterrupt:
        print("\n")
        print("🛑 Stopping audio engine...")
        engine.stop_listening()
        print("✓ Stopped. Goodbye!")

    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
