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
    python3 -m venv venv
    source venv/bin/activate
    pip install --quiet -r requirements.txt
    echo "✅ Setup complete!"
else
    source venv/bin/activate
fi

# Start Ollama if not running
if ! curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
    echo "🚀 Starting Ollama..."
    ollama serve > /dev/null 2>&1 &
    sleep 2
fi

# Launch GUI (no more terminal output)
echo "🎯 Launching Interview Whisperer..."
python app/launcher.py

# Keep terminal open if there's an error
if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Error occurred. Press any key to close..."
    read -n 1
fi
