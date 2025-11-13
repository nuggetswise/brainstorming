# Interview Whisperer 🎯

**AI-Powered Interview Copilot (100% Local & Private)**

Real-time interview assistance that listens to questions and provides contextual answers based on your documents—all running locally on your machine.

---

## Features

- 🎤 **Real-time Audio Transcription**: Captures and transcribes interview questions using Whisper
- 📚 **Document-Aware Answers**: RAG-powered responses using your resume, notes, and project documents
- 💡 **Smart Overlay**: Non-intrusive suggestion window with confidence scores
- 🔒 **100% Private**: Everything runs locally—no data sent to external servers
- 📊 **Session Logging**: Review your interview performance with detailed session logs

---

## Quick Start

### 1. Prerequisites

- **Python 3.10+** ([Download](https://python.org))
- **Ollama** ([Install](https://ollama.ai))
- **Microphone** (for audio capture)

### 2. Installation

```bash
# Clone or download this repository
cd interview-whisperer

# Run the one-click launcher (handles setup automatically)
./START_APP.sh
```

The launcher will:
- Create a virtual environment
- Install dependencies
- Start Ollama (if not running)
- Launch the application

### 3. Add Your Documents

1. Click **"Manage Documents"** in the launcher
2. Add your documents (PDF, DOCX, TXT, MD):
   - Resume/CV
   - Project descriptions
   - Interview prep notes
   - Technical documentation
3. Click **"Process Documents"**

### 4. Start Interview Mode

1. Click **"Start Interview Mode"**
2. Speak your interview questions naturally
3. Suggestions appear in the overlay window
4. Click **"Stop Interview Mode"** when done

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Interview Whisperer                      │
└─────────────────────────────────────────────────────────────┘

┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   Document   │───▶│     LLM      │───▶│   Overlay    │
│  Processor   │    │    Engine    │    │      UI      │
└──────────────┘    └──────────────┘    └──────────────┘
       │                    │                    │
       ▼                    ▼                    ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   ChromaDB   │    │    Ollama    │    │   Tkinter    │
│ (Vector DB)  │    │   (LLM API)  │    │   (GUI)      │
└──────────────┘    └──────────────┘    └──────────────┘

       ▲
       │
┌──────────────┐
│    Audio     │
│   Engine     │
└──────────────┘
       │
       ▼
┌──────────────┐
│   Whisper    │
│ (Transcribe) │
└──────────────┘
```

### Core Components

1. **Document Processor** (`document_processor.py`)
   - Extracts text from PDF, DOCX, TXT, MD files
   - Chunks documents intelligently
   - Creates embeddings via Ollama
   - Stores in ChromaDB vector database

2. **Audio Engine** (`audio_engine.py`)
   - Captures microphone input
   - Transcribes using OpenAI Whisper
   - Detects questions vs. general speech
   - Provides 5-second chunked transcription

3. **LLM Engine** (`llm_engine.py`)
   - Retrieval-Augmented Generation (RAG)
   - Queries ChromaDB for relevant context
   - Generates answers using Ollama
   - Provides confidence scores

4. **Overlay UI** (`overlay.py`)
   - Always-on-top suggestion window
   - Displays questions, answers, and tips
   - Draggable and resizable
   - Keyboard shortcuts (Ctrl+H, Ctrl+C, Esc)

5. **Interview Copilot** (`interview_copilot.py`)
   - Orchestrates all components
   - Manages session state
   - Logs questions and answers
   - Thread-safe operations

6. **Launcher** (`launcher.py`)
   - Main GUI for configuration
   - Document management
   - Status monitoring
   - Start/stop interview mode

---

## Configuration

Edit `app/config.py` to customize:

```python
# Whisper model (tiny, base, small, medium, large)
WHISPER_MODEL = "base"

# Ollama models
OLLAMA_LLM_MODEL = "llama3.1:8b"
OLLAMA_EMBED_MODEL = "nomic-embed-text"

# Audio settings
CHUNK_DURATION_SECONDS = 5

# Document processing
CHUNK_SIZE = 500  # words
CHUNK_OVERLAP = 50  # words
```

---

## Usage Tips

### For Best Results

1. **Document Quality**
   - Use well-formatted documents
   - Include specific examples and metrics
   - Organize by topic (resume, projects, notes)

2. **Audio Quality**
   - Use a good microphone
   - Minimize background noise
   - Speak clearly and at normal pace

3. **Interview Practice**
   - Practice with the overlay visible
   - Use suggestions as talking points (don't read verbatim)
   - Adapt answers to your speaking style

### Keyboard Shortcuts (Overlay)

- `Ctrl+H` - Hide/show overlay
- `Ctrl+C` - Copy answer to clipboard
- `Esc` - Clear current suggestion

---

## Session Logs

After each interview session, review your performance:

```bash
# Logs are saved in:
data/logs/session_YYYYMMDD_HHMMSS.json

# Each log contains:
{
  "start_time": "2024-11-13T10:30:00",
  "end_time": "2024-11-13T11:15:00",
  "duration_minutes": 45,
  "total_questions": 12,
  "questions": [
    {
      "timestamp": "10:32:15",
      "question": "Tell me about your PM experience",
      "answer": "I have 5 years of...",
      "confidence": 0.85,
      "sources": ["resume.pdf", "notes.txt"]
    }
  ]
}
```

---

## Troubleshooting

### Ollama Not Running

```bash
# Start Ollama manually
ollama serve

# Pull required models
ollama pull llama3.1:8b
ollama pull nomic-embed-text
```

### No Documents Processed

1. Check documents are in `documents/` folder
2. Verify supported formats: PDF, DOCX, TXT, MD
3. Click "Process Documents" in Document Manager
4. Check logs in `data/logs/` for errors

### Microphone Not Working

```bash
# Test microphone
python3 -c "import sounddevice as sd; print(sd.query_devices())"

# List available devices
# Update config.py if needed to select specific device
```

### Poor Transcription Quality

- Use Whisper `small` or `medium` model for better accuracy
- Ensure good microphone quality
- Minimize background noise
- Speak clearly

---

## Development

### Project Structure

```
interview-whisperer/
├── app/
│   ├── audio_engine.py          # Audio capture & transcription
│   ├── document_processor.py    # Document parsing & embedding
│   ├── llm_engine.py            # RAG & answer generation
│   ├── overlay.py               # Suggestion overlay UI
│   ├── interview_copilot.py     # Main orchestrator
│   ├── launcher.py              # GUI launcher
│   └── config.py                # Configuration
├── documents/                    # Your documents (PDF, DOCX, TXT, MD)
├── data/
│   ├── chroma_db/               # Vector database
│   └── logs/                    # Session logs
├── requirements.txt             # Python dependencies
├── START_APP.sh                 # One-click launcher
└── README.md                    # This file
```

### Running Tests

```bash
# Test document processor
python3 app/test_processor.py

# Test LLM engine
python3 app/test_llm_engine.py

# Test audio engine
python3 app/audio_engine.py

# Test overlay
python3 app/overlay.py
```

---

## Privacy & Security

- ✅ All processing happens locally
- ✅ No data sent to external servers
- ✅ Documents stored on your machine
- ✅ Ollama runs locally
- ✅ No telemetry or tracking

---

## System Requirements

- **OS**: macOS, Linux, or Windows (WSL)
- **RAM**: 8GB minimum (16GB recommended for large models)
- **Storage**: 5GB for models and data
- **Microphone**: Any USB or built-in mic

---

## Credits

Built with:
- [OpenAI Whisper](https://github.com/openai/whisper) - Audio transcription
- [Ollama](https://ollama.ai) - Local LLM inference
- [ChromaDB](https://www.trychroma.com/) - Vector database
- [Python](https://python.org) & [Tkinter](https://docs.python.org/3/library/tkinter.html) - Application framework

---

## License

MIT License - See LICENSE file for details

---

## Support

For issues, feature requests, or questions:
- Check `data/logs/` for error details
- Review this README
- Check Ollama status: `ollama list`

---

**Happy Interviewing! 🎯**
