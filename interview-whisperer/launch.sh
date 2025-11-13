#!/bin/bash
#
# Interview Whisperer - Quick Launch Script
# Double-click this file or run from terminal
#

cd "$(dirname "$0")"

echo "🎯 Launching Interview Whisperer..."
echo ""

# Check if Python3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "Please install Python 3 to use Interview Whisperer"
    exit 1
fi

# Check if tkinter is available
python3 -c "import tkinter" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  Warning: tkinter not found"
    echo "Install with: sudo apt-get install python3-tk"
    echo ""
fi

# Launch the application
python3 app/launcher.py

echo ""
echo "✅ Interview Whisperer closed"
