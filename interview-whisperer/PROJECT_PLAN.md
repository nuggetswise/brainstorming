# Interview Whisperer - AI Interview Copilot

## 🎯 Product Vision
A privacy-first, local-only desktop app that provides real-time interview assistance by:
1. Processing your resume, job description, and notes
2. Listening to interview questions in real-time
3. Suggesting intelligent answers based on YOUR documents
4. Displaying suggestions in an always-on-top overlay

## 🏗️ Architecture

```
interview-whisperer/
├── app/
│   ├── launcher.py              # Main GUI launcher (START HERE)
│   ├── document_processor.py    # Load & embed documents
│   ├── audio_engine.py          # Whisper integration
│   ├── llm_engine.py            # Ollama + RAG
│   ├── overlay.py               # Suggestion overlay window
│   └── config.py                # Settings
├── documents/                   # USER DROPS FILES HERE
│   ├── .gitkeep
│   └── README.md
├── data/
│   ├── chroma_db/              # Vector database (auto-created)
│   └── logs/                   # App logs
├── assets/
│   ├── icon.png
│   └── styles.css
├── requirements.txt
├── setup.sh                    # One-click setup script
└── README.md

## 💻 Tech Stack (All Local)
- Python 3.10+
- Tkinter (GUI - built-in to Python)
- Whisper (local transcription)
- Ollama (local LLM)
- ChromaDB (local vector DB)
- sounddevice (audio capture)

## 🎨 UX Flow

### First Launch:
1. User opens app → sees beautiful launcher window
2. Clicks "📁 Manage Documents" → drag-drop interface
3. Drops resume.pdf, job_description.txt
4. Clicks "Process Documents" → progress bar shows processing
5. Status: "✅ Ready for interviews! 47 chunks loaded"

### During Interview:
1. User clicks "🎯 Start Interview Mode"
2. Small overlay appears (top-right corner, draggable)
3. Status: "🎤 Listening..."
4. Interviewer asks question
5. Overlay updates: "💡 Suggested Answer: [...]"
6. User reads/adapts answer naturally
7. Click "Stop" when done

## 🔒 Privacy
- 100% local processing
- No cloud APIs
- No telemetry
- Documents never leave your machine

## 📅 3-Day Build Plan

### Day 1: Foundation + Document Processing
- Setup project structure
- Build launcher GUI
- Document upload & processing
- ChromaDB integration

### Day 2: Audio + Transcription
- Whisper integration
- Real-time audio capture
- Question detection

### Day 3: LLM + Overlay + Polish
- Ollama RAG integration
- Overlay UI
- End-to-end testing
- UX polish

## 🤖 AI Agent Team

1. **Setup Agent** - Project structure, dependencies
2. **Document Agent** - PDF/DOCX parsing, ChromaDB
3. **Audio Agent** - Whisper, microphone capture
4. **LLM Agent** - Ollama, RAG pipeline
5. **UX Agent** - Beautiful UI/UX, overlay design
6. **Integration Agent** - Tie everything together

## ✅ Success Criteria
- [ ] One-click launch (no terminal commands)
- [ ] Beautiful, intuitive GUI
- [ ] <3 second response time
- [ ] Works with Zoom/Meet/Teams
- [ ] Handles PDF, DOCX, TXT files
- [ ] Draggable, resizable overlay
- [ ] Clean, modern design
