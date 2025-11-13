# Interview Whisperer - Application

This directory contains the GUI applications for Interview Whisperer.

## Launcher

The main launcher provides a beautiful, user-friendly interface to manage your interview preparation.

### Usage

```bash
python3 /home/user/interview-whisperer/app/launcher.py
```

Or use the convenient launch script:

```bash
cd /home/user/interview-whisperer
./launch.sh
```

## Features

### 🎯 Main Launcher (launcher.py)
- **Modern Dark Theme UI** - Professional, easy on the eyes
- **System Status Monitoring** - Real-time checks for Ollama and documents
- **Document Management** - Easy access to add and process your materials
- **Interview Mode** - One-click launch of the voice-activated copilot
- **Settings** - Customize your experience

### Status Indicators
- ✅ Green: System ready
- ⚠️ Yellow: Action needed
- ❌ Red: Error/not available
- 🔄 Refresh: Update status any time

## Components

### Current
- `launcher.py` - Main application launcher (COMPLETE)

### Coming Soon
- `document_manager.py` - Manage and process documents
- `interview_mode.py` - Voice-activated copilot interface
- `settings.py` - Configuration panel

## Requirements

- Python 3.8+
- tkinter (included with Python)
- Ollama (for AI functionality)

## Architecture

The launcher follows clean MVC-style patterns:
- Clear separation of UI and logic
- Status checking methods
- Event-driven button actions
- Modular, extensible design

## UI Design

- **600x550px window** - Perfect size, not too big or small
- **Dark theme** - Modern color scheme (#1e1e2e base)
- **Large buttons** - Easy to click and read
- **Clear status** - Know what's happening at a glance
- **Helpful messages** - Guides you through setup

## Development Notes

The launcher is designed to be the **only entry point** users need. No terminal commands, no configuration files to edit manually. Everything through the GUI.
