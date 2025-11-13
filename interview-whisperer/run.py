#!/usr/bin/env python3
"""
Interview Whisperer - Pure Python Launcher
Double-click this file to launch the app (no terminal needed!)
"""

import sys
import os
import subprocess
from pathlib import Path

# Change to project directory
os.chdir(Path(__file__).parent)

def check_python_version():
    """Ensure Python 3.10+"""
    if sys.version_info < (3, 10):
        print("❌ Python 3.10+ required")
        print(f"   Current: Python {sys.version_info.major}.{sys.version_info.minor}")
        input("Press Enter to exit...")
        sys.exit(1)

def setup_environment():
    """First-time setup: create venv and install dependencies"""
    venv_path = Path("venv")

    if not venv_path.exists():
        print("🔧 First-time setup (this will take a minute)...")
        print("   Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)

        # Determine pip path
        if sys.platform == "win32":
            pip_path = venv_path / "Scripts" / "pip"
        else:
            pip_path = venv_path / "bin" / "pip"

        print("   Installing dependencies...")
        subprocess.run([str(pip_path), "install", "-q", "-r", "requirements.txt"], check=True)
        print("✅ Setup complete!")

    # Return python path in venv
    if sys.platform == "win32":
        return venv_path / "Scripts" / "python"
    else:
        return venv_path / "bin" / "python"

def check_ollama():
    """Check if Ollama is running, try to start if not"""
    import socket

    # Check if port 11434 is open
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('localhost', 11434))
    sock.close()

    if result != 0:
        print("🚀 Starting Ollama...")
        if sys.platform == "darwin":  # macOS
            subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif sys.platform == "linux":
            subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        import time
        time.sleep(2)  # Give Ollama time to start

def launch_gui(python_path):
    """Launch the GUI application"""
    print("🎯 Launching Interview Whisperer...")

    # Launch GUI
    launcher_path = Path("app") / "launcher.py"
    subprocess.run([str(python_path), str(launcher_path)])

def main():
    """Main launcher logic"""
    try:
        print("=" * 50)
        print("🎯 Interview Whisperer")
        print("=" * 50)
        print()

        # Check Python version
        check_python_version()

        # Setup environment (if needed)
        python_path = setup_environment()

        # Check/start Ollama
        check_ollama()

        # Launch GUI
        launch_gui(python_path)

    except KeyboardInterrupt:
        print("\n\n👋 Cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nFor help, see README.md")
        input("\nPress Enter to exit...")
        sys.exit(1)

if __name__ == "__main__":
    main()
