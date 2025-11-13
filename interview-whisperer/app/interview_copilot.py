#!/usr/bin/env python3
"""
Interview Copilot - Main Integration Layer

Orchestrates all components of Interview Whisperer:
- Document processing and RAG context
- Real-time audio capture and transcription
- LLM-powered answer generation
- Overlay UI for displaying suggestions
"""

import threading
import time
import json
from pathlib import Path
from typing import Optional, Callable, Dict, Any
from datetime import datetime
import logging

# Local imports
try:
    from .config import (
        WHISPER_MODEL,
        OLLAMA_LLM_MODEL,
        CHUNK_DURATION_SECONDS,
        DOCUMENTS_DIR,
        DATA_DIR,
        CHROMA_DB_DIR,
        LOGS_DIR,
        check_ollama_running,
        logger
    )
    from .document_processor import DocumentProcessor
    from .audio_engine import AudioEngine
    from .llm_engine import LLMEngine
    from .overlay import OverlayWindow
except ImportError:
    # Fallback for direct execution
    from config import (
        WHISPER_MODEL,
        OLLAMA_LLM_MODEL,
        CHUNK_DURATION_SECONDS,
        DOCUMENTS_DIR,
        DATA_DIR,
        CHROMA_DB_DIR,
        LOGS_DIR,
        check_ollama_running,
        logger
    )
    from document_processor import DocumentProcessor
    from audio_engine import AudioEngine
    from llm_engine import LLMEngine
    from overlay import OverlayWindow


class InterviewCopilot:
    """
    Main orchestrator for Interview Whisperer.

    Integrates:
    - DocumentProcessor: Loads and indexes user documents
    - AudioEngine: Captures and transcribes speech
    - LLMEngine: Generates contextual answers
    - OverlayWindow: Displays suggestions to user

    Workflow:
    1. User starts interview mode
    2. Audio engine listens for questions
    3. When question detected → LLM generates answer using RAG
    4. Answer displayed in overlay
    5. Session logged for review
    """

    def __init__(self):
        """Initialize the Interview Copilot."""
        self.logger = logging.getLogger('InterviewWhisperer.Copilot')

        # State
        self._is_active = False
        self._session_start_time: Optional[float] = None
        self._session_log: Dict[str, Any] = {}
        self._questions_answered = 0

        # Components (initialized on demand)
        self.document_processor: Optional[DocumentProcessor] = None
        self.audio_engine: Optional[AudioEngine] = None
        self.llm_engine: Optional[LLMEngine] = None
        self.overlay: Optional[OverlayWindow] = None

        # Threading
        self._lock = threading.Lock()

        self.logger.info("InterviewCopilot initialized")

    def initialize_components(self) -> bool:
        """
        Initialize all components.

        Returns:
            True if successful, False otherwise
        """
        try:
            self.logger.info("Initializing components...")

            # Initialize document processor
            self.document_processor = DocumentProcessor(
                documents_dir=str(DOCUMENTS_DIR),
                db_path=str(CHROMA_DB_DIR)
            )
            self.logger.info("✓ Document processor initialized")

            # Initialize LLM engine
            self.llm_engine = LLMEngine(
                db_path=str(CHROMA_DB_DIR),
                model=OLLAMA_LLM_MODEL
            )
            self.logger.info("✓ LLM engine initialized")

            # Initialize audio engine
            self.audio_engine = AudioEngine(
                model=WHISPER_MODEL,
                language="en"
            )
            self.logger.info("✓ Audio engine initialized")

            # Initialize overlay
            self.overlay = OverlayWindow()
            self.logger.info("✓ Overlay window initialized")

            return True

        except Exception as e:
            self.logger.error(f"Failed to initialize components: {e}", exc_info=True)
            return False

    def check_prerequisites(self) -> Dict[str, Any]:
        """
        Check if system is ready to start interview mode.

        Returns:
            Dictionary with check results:
            {
                'ready': bool,
                'issues': List[str],
                'documents_loaded': int,
                'ollama_running': bool
            }
        """
        issues = []

        # Check Ollama
        ollama_running = check_ollama_running()
        if not ollama_running:
            issues.append("Ollama is not running. Start it with: ollama serve")

        # Check documents
        if self.document_processor is None:
            try:
                self.document_processor = DocumentProcessor(
                    documents_dir=str(DOCUMENTS_DIR),
                    db_path=str(CHROMA_DB_DIR)
                )
            except Exception as e:
                issues.append(f"Failed to initialize document processor: {e}")

        stats = self.document_processor.get_stats() if self.document_processor else {}
        documents_loaded = stats.get('files_processed', 0)

        if documents_loaded == 0:
            issues.append("No documents processed. Please add and process documents first.")

        # Check microphone (basic check)
        try:
            import sounddevice as sd
            devices = sd.query_devices()
            has_input = any(d['max_input_channels'] > 0 for d in devices)
            if not has_input:
                issues.append("No microphone detected")
        except Exception as e:
            issues.append(f"Microphone check failed: {e}")

        return {
            'ready': len(issues) == 0,
            'issues': issues,
            'documents_loaded': documents_loaded,
            'ollama_running': ollama_running
        }

    def start_interview_mode(self) -> bool:
        """
        Start the interview copilot.

        Returns:
            True if started successfully, False otherwise
        """
        with self._lock:
            if self._is_active:
                self.logger.warning("Interview mode already active")
                return False

            # Check prerequisites
            prereq_check = self.check_prerequisites()
            if not prereq_check['ready']:
                self.logger.error("Prerequisites not met:")
                for issue in prereq_check['issues']:
                    self.logger.error(f"  - {issue}")
                return False

            try:
                # Initialize components if not already done
                if self.audio_engine is None or self.llm_engine is None:
                    if not self.initialize_components():
                        return False

                # Start session
                self._session_start_time = time.time()
                self._questions_answered = 0
                self._session_log = {
                    'start_time': datetime.now().isoformat(),
                    'questions': []
                }

                # Show overlay
                self.overlay.show()
                self.overlay.clear()  # Clear any previous content

                # Start audio engine
                self.audio_engine.start_listening(callback=self._on_transcript)

                self._is_active = True
                self.logger.info("🎯 Interview mode started")

                return True

            except Exception as e:
                self.logger.error(f"Failed to start interview mode: {e}", exc_info=True)
                return False

    def stop_interview_mode(self) -> bool:
        """
        Stop the interview copilot.

        Returns:
            True if stopped successfully
        """
        with self._lock:
            if not self._is_active:
                self.logger.warning("Interview mode not active")
                return False

            try:
                # Stop audio engine
                if self.audio_engine:
                    self.audio_engine.stop_listening()

                # Hide overlay
                if self.overlay:
                    self.overlay.hide()

                # Save session log
                self._save_session_log()

                self._is_active = False
                self.logger.info("🛑 Interview mode stopped")

                return True

            except Exception as e:
                self.logger.error(f"Error stopping interview mode: {e}", exc_info=True)
                return False

    def _on_transcript(self, text: str, is_question: bool) -> None:
        """
        Callback from audio engine when new transcript is available.

        Args:
            text: Transcribed text
            is_question: Whether the text appears to be a question
        """
        if not self._is_active:
            return

        self.logger.info(f"Transcript: {text} (question={is_question})")

        if is_question:
            # Generate answer in background thread
            threading.Thread(
                target=self._handle_question,
                args=(text,),
                daemon=True
            ).start()
        else:
            # Update context (optional - for now just log)
            self.logger.debug(f"Context update: {text}")

    def _handle_question(self, question: str) -> None:
        """
        Handle a detected question.

        Args:
            question: The interview question
        """
        try:
            start_time = time.time()

            # Show loading state
            if self.overlay:
                self.overlay.show_suggestion(
                    question=question[:100] + "..." if len(question) > 100 else question,
                    answer="⏳ Generating answer...",
                    confidence=0.0,
                    tips={
                        'time': 'Please wait...',
                        'method': 'Searching documents and generating response'
                    }
                )

            # Generate answer using LLM
            self.logger.info(f"Generating answer for: {question}")
            result = self.llm_engine.generate_answer(
                question=question,
                temperature=0.7,
                max_tokens=250
            )

            # Display in overlay
            if self.overlay:
                self.overlay.show_suggestion(
                    question=question,
                    answer=result['answer'],
                    confidence=result['confidence'],
                    tips={
                        'time': '60-90 seconds recommended',
                        'method': 'Use STAR method (Situation, Task, Action, Result)'
                    }
                )

            # Log question/answer
            self._log_question_answer(question, result)

            self._questions_answered += 1

            elapsed = time.time() - start_time
            self.logger.info(
                f"✓ Answer generated in {elapsed:.2f}s "
                f"(confidence: {result['confidence']:.0%})"
            )

        except Exception as e:
            self.logger.error(f"Error handling question: {e}", exc_info=True)

            # Show error in overlay
            if self.overlay:
                self.overlay.show_suggestion(
                    question=question,
                    answer=(
                        "I apologize, but I encountered an error generating an answer. "
                        "Please try rephrasing the question."
                    ),
                    confidence=0.0,
                    tips={
                        'time': 'Error occurred',
                        'method': f'Error: {str(e)[:50]}'
                    }
                )

    def _log_question_answer(self, question: str, result: Dict[str, Any]) -> None:
        """
        Log a question/answer pair to session log.

        Args:
            question: The interview question
            result: LLM generation result
        """
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'question': question,
            'answer': result['answer'],
            'confidence': result['confidence'],
            'sources': result['sources'],
            'context_used': result.get('context_used', False),
            'generation_time': result.get('generation_time', 0)
        }

        self._session_log['questions'].append(log_entry)

    def _save_session_log(self) -> None:
        """Save session log to file."""
        if not self._session_log.get('questions'):
            self.logger.info("No questions answered, skipping session log")
            return

        try:
            # Calculate session duration
            if self._session_start_time:
                duration_seconds = time.time() - self._session_start_time
                self._session_log['duration_seconds'] = duration_seconds
                self._session_log['duration_minutes'] = duration_seconds / 60

            self._session_log['end_time'] = datetime.now().isoformat()
            self._session_log['total_questions'] = len(self._session_log['questions'])

            # Save to file
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            log_file = LOGS_DIR / f"session_{timestamp}.json"

            with open(log_file, 'w', encoding='utf-8') as f:
                json.dump(self._session_log, f, indent=2, ensure_ascii=False)

            self.logger.info(f"✓ Session log saved to: {log_file}")

        except Exception as e:
            self.logger.error(f"Failed to save session log: {e}", exc_info=True)

    def get_status(self) -> Dict[str, Any]:
        """
        Get current copilot status.

        Returns:
            Dictionary with status information
        """
        return {
            'is_active': self._is_active,
            'documents_loaded': (
                self.document_processor.get_stats().get('files_processed', 0)
                if self.document_processor else 0
            ),
            'questions_answered': self._questions_answered,
            'session_duration': (
                time.time() - self._session_start_time
                if self._session_start_time else 0
            ),
            'components_initialized': all([
                self.document_processor is not None,
                self.audio_engine is not None,
                self.llm_engine is not None,
                self.overlay is not None
            ])
        }

    def cleanup(self) -> None:
        """Clean up resources."""
        self.logger.info("Cleaning up Interview Copilot...")

        if self._is_active:
            self.stop_interview_mode()

        if self.audio_engine:
            self.audio_engine.stop_listening()

        if self.overlay:
            self.overlay.destroy()

        self.logger.info("✓ Cleanup complete")

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.cleanup()


# =============================================================================
# TESTING
# =============================================================================

def test_copilot():
    """Test the Interview Copilot with simulated questions."""
    import sys

    print("=" * 70)
    print("🎯 Interview Whisperer - Copilot Test")
    print("=" * 70)
    print()

    # Create copilot
    copilot = InterviewCopilot()

    # Check prerequisites
    print("1️⃣  Checking prerequisites...")
    prereqs = copilot.check_prerequisites()

    if prereqs['ready']:
        print("   ✓ System ready")
        print(f"   - Documents loaded: {prereqs['documents_loaded']}")
        print(f"   - Ollama running: {prereqs['ollama_running']}")
    else:
        print("   ✗ System not ready:")
        for issue in prereqs['issues']:
            print(f"     - {issue}")
        print()
        print("Please fix these issues and try again.")
        return

    print()
    print("2️⃣  Starting interview mode...")

    if copilot.start_interview_mode():
        print("   ✓ Interview mode started")
    else:
        print("   ✗ Failed to start interview mode")
        return

    print()
    print("3️⃣  Testing question detection...")
    print("   (Speak into your microphone to test)")
    print("   Press Ctrl+C to stop")
    print()

    try:
        # Run until interrupted
        while True:
            status = copilot.get_status()
            print(
                f"\r   Status: Active | Questions: {status['questions_answered']} | "
                f"Duration: {status['session_duration']:.0f}s   ",
                end='',
                flush=True
            )
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n")
        print("4️⃣  Stopping interview mode...")
        copilot.stop_interview_mode()
        print("   ✓ Interview mode stopped")

        status = copilot.get_status()
        print()
        print("📊 Session Summary:")
        print(f"   - Questions answered: {status['questions_answered']}")
        print(f"   - Duration: {status['session_duration']:.0f} seconds")

    finally:
        copilot.cleanup()

    print()
    print("=" * 70)
    print("✅ Test complete")
    print("=" * 70)


if __name__ == "__main__":
    test_copilot()
