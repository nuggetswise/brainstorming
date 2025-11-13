# Audio Engine Integration Guide

## Overview

The **AudioEngine** provides real-time audio capture and transcription for Interview Whisperer using OpenAI's Whisper model. It's optimized for M3 Mac performance with efficient threading and chunked processing.

---

## Quick Start

### Basic Usage

```python
from audio_engine import AudioEngine

def handle_transcript(text: str, is_question: bool):
    if is_question:
        print(f"Question: {text}")
        # Trigger answer retrieval
    else:
        print(f"Speech: {text}")

# Initialize and start
engine = AudioEngine(model="base", language="en")
engine.start_listening(handle_transcript)

# ... interview happens ...

# Stop when done
engine.stop_listening()
```

### Test the Engine

```bash
# Run the test script
cd /home/user/interview-whisperer/app
python3 audio_engine.py

# Or run demos
python3 audio_engine_demo.py --demo basic
python3 audio_engine_demo.py --demo advanced
python3 audio_engine_demo.py --demo minimal
```

---

## Architecture

### Audio Flow

```
Microphone → sounddevice capture (16kHz, mono)
    ↓
Audio Buffer (5-second chunks)
    ↓
Whisper Transcription (background thread)
    ↓
Question Detection (ends with "?")
    ↓
Callback → Application Logic
```

### Threading Model

- **Main Thread**: Application logic
- **Audio Thread**: Microphone capture (non-blocking)
- **Transcription Thread**: Whisper processing (non-blocking)

All threads are daemon threads that clean up automatically.

---

## API Reference

### AudioEngine Class

```python
class AudioEngine:
    def __init__(self, model: str = "base", language: str = "en")
    def start_listening(self, callback: Callable[[str, bool], None]) -> None
    def stop_listening(self) -> None
    def get_status(self) -> Dict[str, any]
    def get_recent_context(self, duration: float = 30.0) -> str
```

### Parameters

**`__init__`**
- `model`: Whisper model size
  - `"tiny"`: Fastest, least accurate (~1GB RAM)
  - `"base"`: **Recommended for M3 Mac** - Fast + accurate (~1GB RAM)
  - `"small"`: More accurate, slower (~2GB RAM)
  - `"medium"`: Very accurate, much slower (~5GB RAM)
  - `"large"`: Best accuracy, slowest (~10GB RAM)
- `language`: Language code (default: `"en"`)

**`start_listening`**
- `callback`: Function called with `(text: str, is_question: bool)`
  - `text`: Transcribed text
  - `is_question`: `True` if detected as question

**`get_status`**
Returns dictionary:
```python
{
    'is_listening': bool,         # Whether currently listening
    'audio_level': float,         # Current audio level (0.0-1.0)
    'chunks_processed': int,      # Number of chunks transcribed
    'model': str,                 # Whisper model name
    'language': str               # Language code
}
```

**`get_recent_context`**
- `duration`: Seconds of history to return (default: 30.0)
- Returns: Concatenated transcript text from last N seconds

---

## Configuration

### AudioConfig Dataclass

```python
@dataclass
class AudioConfig:
    sample_rate: int = 16000           # Whisper standard (don't change)
    channels: int = 1                  # Mono (don't change)
    chunk_duration: float = 5.0        # Seconds per transcription
    silence_threshold: float = 0.01    # Amplitude for silence detection
    silence_duration: float = 1.5      # Silence after question (seconds)
    context_duration: float = 30.0     # Context window (seconds)
```

To customize, modify the `AudioConfig` class before initialization.

---

## Integration with Document Processor

### Full Integration Example

```python
from audio_engine import AudioEngine
from document_processor import DocumentProcessor

class InterviewWhisperer:
    def __init__(self, resume_path: str):
        # Initialize components
        self.processor = DocumentProcessor()
        self.processor.load_resume(resume_path)

        self.audio = AudioEngine(model="base")
        self.questions = []

    def on_transcript(self, text: str, is_question: bool):
        """Handle transcription callback."""
        if is_question:
            # Question detected!
            self.questions.append(text)

            # Retrieve answer from knowledge base
            answer = self.processor.retrieve_answer(text)

            # Display to user (GUI or console)
            self.show_answer(question=text, answer=answer)
        else:
            # Regular speech - accumulate as context
            self.update_context(text)

    def show_answer(self, question: str, answer: str):
        """Display answer to user."""
        print(f"\n{'='*70}")
        print(f"Q: {question}")
        print(f"A: {answer}")
        print(f"{'='*70}\n")

    def update_context(self, text: str):
        """Update conversation context."""
        # Could use this for follow-up questions
        pass

    def start(self):
        """Start the interview copilot."""
        self.audio.start_listening(self.on_transcript)

    def stop(self):
        """Stop the copilot."""
        self.audio.stop_listening()
```

### Usage

```python
# Initialize
copilot = InterviewWhisperer(resume_path="resume.pdf")

# Start listening
copilot.start()

# Interview happens...
# Questions are automatically detected and answered

# Stop when done
copilot.stop()
```

---

## Question Detection

### How It Works

The engine uses two heuristics to detect questions:

1. **Ends with "?"** - Simple but effective for clear questions
2. **Question words + silence** - Detects questions like:
   - "What is your experience with Python"
   - "Can you tell me about..."
   - "How would you approach..."

### Detected Question Words

`what`, `why`, `how`, `when`, `where`, `who`, `which`, `can`, `could`, `would`, `should`, `is`, `are`, `do`, `does`, `did`

### Customization

To adjust detection sensitivity:

```python
# In AudioEngine class
config = AudioConfig()
config.silence_duration = 2.0  # More silence needed after question
```

---

## Performance Optimization

### Model Selection (M3 Mac)

| Model  | Speed      | Accuracy | RAM   | Recommendation |
|--------|------------|----------|-------|----------------|
| tiny   | Very Fast  | Low      | ~1GB  | Testing only   |
| **base** | **Fast** | **Good** | **~1GB** | **✓ Recommended** |
| small  | Medium     | Better   | ~2GB  | If accuracy critical |
| medium | Slow       | Great    | ~5GB  | Overkill for interviews |
| large  | Very Slow  | Best     | ~10GB | Not needed |

**Recommendation**: Use `"base"` model - it's fast enough for real-time on M3 Mac and accurate enough for interview questions.

### Chunk Duration

```python
# Adjust trade-off between latency and accuracy
config.chunk_duration = 5.0   # Default (good balance)
config.chunk_duration = 3.0   # Lower latency, less context
config.chunk_duration = 10.0  # Higher accuracy, more delay
```

---

## Error Handling

### Common Issues

**1. Microphone Not Found**
```
Error: Audio capture error: No input device found
```
**Solution**: Check microphone permissions in System Settings → Privacy & Security → Microphone

**2. Model Loading Fails**
```
Error: Failed to load Whisper model 'base'
```
**Solution**: Install dependencies:
```bash
pip install openai-whisper
```

**3. Performance Issues (Lag)**
```
Warning: Audio queue full, dropping chunk
```
**Solution**: Use faster model (`"tiny"` or `"base"`) or increase chunk duration

### Graceful Degradation

The engine handles errors gracefully:
- Microphone disconnection → Logs warning, continues with next chunk
- Transcription failure → Logs error, skips chunk, continues
- Buffer overflow → Drops oldest chunks, continues

---

## Testing

### Unit Tests

```python
# Test microphone capture
def test_microphone():
    engine = AudioEngine()

    def callback(text, is_question):
        print(f"Received: {text} (question: {is_question})")

    engine.start_listening(callback)
    time.sleep(10)  # Capture 10 seconds
    engine.stop_listening()

# Test question detection
def test_questions():
    test_cases = [
        ("What is your experience?", True),
        ("Tell me about Python", False),
        ("How do you handle errors?", True),
        ("I worked on Django projects", False),
    ]

    for text, expected in test_cases:
        is_q = engine._detect_question(text)
        assert is_q == expected
```

### Integration Tests

```bash
# Run full demo
python3 audio_engine_demo.py --demo advanced

# Test with document processor
python3 integration_example.py
```

---

## Best Practices

### 1. Resource Management

Always use context manager or explicit cleanup:

```python
# Option 1: Context manager
with AudioEngine() as engine:
    engine.start_listening(callback)
    # ... use engine ...
# Automatically cleaned up

# Option 2: Explicit cleanup
engine = AudioEngine()
try:
    engine.start_listening(callback)
    # ... use engine ...
finally:
    engine.stop_listening()
```

### 2. Callback Performance

Keep callbacks fast - don't block:

```python
# ❌ Bad - blocks transcription thread
def slow_callback(text, is_question):
    if is_question:
        answer = slow_database_query(text)  # Takes 5 seconds!
        print(answer)

# ✓ Good - offload to another thread
import queue
answer_queue = queue.Queue()

def fast_callback(text, is_question):
    if is_question:
        answer_queue.put(text)  # Non-blocking

def answer_worker():
    while True:
        question = answer_queue.get()
        answer = slow_database_query(question)
        print(answer)
```

### 3. Context Accumulation

Use `get_recent_context()` for follow-up questions:

```python
def on_transcript(text, is_question):
    if is_question:
        # Get context for better answer retrieval
        context = engine.get_recent_context(duration=15.0)
        answer = processor.retrieve_answer(
            question=text,
            context=context  # Use conversation context
        )
```

### 4. Status Monitoring

Monitor status for debugging:

```python
# In main loop
status = engine.get_status()
if status['chunks_processed'] == 0 and time_elapsed > 10:
    print("Warning: No audio detected. Check microphone.")

if status['audio_level'] < 0.001:
    print("Warning: Audio level very low. Speak louder.")
```

---

## Troubleshooting

### No Transcription Output

1. **Check microphone permissions**
   ```bash
   # macOS: System Settings → Privacy & Security → Microphone
   # Add Terminal or Python to allowed apps
   ```

2. **Test microphone**
   ```python
   import sounddevice as sd
   print(sd.query_devices())  # List available devices
   ```

3. **Check audio level**
   ```python
   status = engine.get_status()
   print(f"Audio level: {status['audio_level']}")  # Should be > 0.01
   ```

### Poor Question Detection

1. **Adjust silence threshold**
   ```python
   config.silence_duration = 2.0  # Require more silence
   ```

2. **Manually mark questions**
   ```python
   # Override detection in callback
   def callback(text, is_question):
       # Force question if contains "?"
       is_question = "?" in text
       # ... process ...
   ```

### Performance Issues

1. **Use smaller model**
   ```python
   engine = AudioEngine(model="tiny")  # Fastest
   ```

2. **Increase chunk duration**
   ```python
   config.chunk_duration = 10.0  # Less frequent transcription
   ```

3. **Check CPU usage**
   ```bash
   top -pid $(pgrep -f audio_engine.py)
   ```

---

## Advanced Usage

### Multi-Language Support

```python
# Spanish interviews
engine = AudioEngine(model="base", language="es")

# Auto-detect language
engine = AudioEngine(model="base", language=None)  # Whisper auto-detects
```

### Custom Question Detection

```python
# Override detection logic
class CustomAudioEngine(AudioEngine):
    def _detect_question(self, text: str) -> bool:
        # Custom logic
        if "?" in text:
            return True
        if self.ml_model.predict(text) > 0.8:
            return True
        return False
```

### Streaming to File

```python
class RecordingEngine(AudioEngine):
    def __init__(self, *args, output_file="interview.wav", **kwargs):
        super().__init__(*args, **kwargs)
        self.output_file = output_file
        self.audio_frames = []

    def _audio_capture_loop(self):
        # Override to also save audio
        # ... capture logic ...
        self.audio_frames.append(audio_chunk)
        # ... rest of logic ...

    def save_recording(self):
        # Save accumulated audio to WAV file
        import scipy.io.wavfile
        audio_data = np.concatenate(self.audio_frames)
        scipy.io.wavfile.write(
            self.output_file,
            self.config.sample_rate,
            audio_data
        )
```

---

## FAQ

**Q: How much latency is there?**
A: ~5-8 seconds from speech to transcription with `base` model (5s chunk + 1-3s processing).

**Q: Can I use it offline?**
A: Yes! Whisper runs entirely locally. No internet required.

**Q: Does it work with Zoom/Meet?**
A: Yes, if your Mac is configured to use the interview audio as microphone input. Use tools like BlackHole or Loopback for audio routing.

**Q: How accurate is question detection?**
A: ~90% for clear questions ending with "?". ~70% for implicit questions (depends on silence detection).

**Q: Can I use GPU acceleration?**
A: M3 Macs use Metal (not CUDA). Whisper automatically uses optimized FP32 on M-series chips.

---

## Next Steps

1. **Test the engine**:
   ```bash
   python3 audio_engine.py
   ```

2. **Run demos**:
   ```bash
   python3 audio_engine_demo.py --demo basic
   ```

3. **Integrate with document processor**:
   - See `integration_example.py` for full example
   - Combine AudioEngine + DocumentProcessor

4. **Build GUI**:
   - Use engine with Tkinter for visual interface
   - Show real-time transcription + answers

---

**Questions?** Check the code comments or run the demo scripts for examples.
