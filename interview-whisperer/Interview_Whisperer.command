#!/bin/bash

# Interview Whisperer - Mac Double-Click Launcher
# Save as: Interview_Whisperer.command
# Make executable: chmod +x Interview_Whisperer.command
# Double-click to launch!

# Navigate to script directory
cd "$(dirname "$0")"

# Set up environment (first time only)
if [ ! -d "venv" ]; then
    echo "🔧 First-time setup (this will take a minute)..."
    /opt/homebrew/bin/python3.13 -m venv venv
    if [ ! -d "venv" ]; then
        echo "❌ Failed to create virtual environment"
        exit 1
    fi
fi

# Activate venv
source venv/bin/activate

# Install dependencies if needed
if [ ! -f "venv/.installed" ]; then
    pip install --quiet -r requirements.txt
    touch venv/.installed
    echo "✅ Setup complete!"
fi

# Start Ollama if not running
if ! curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
    echo "🚀 Starting Ollama..."
    ollama serve > /dev/null 2>&1 &
    sleep 2
fi

# Launch GUI (no more terminal output)
echo "🎯 Launching Interview Whisperer..."
venv/bin/python app/launcher.py

# Keep terminal open if there's an error
if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Error occurred. Press any key to close..."
    read -n 1
fi
