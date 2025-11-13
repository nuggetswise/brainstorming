# 🚀 How to Launch Interview Whisperer

You have **3 easy ways** to launch the app. Choose your favorite!

---

## ✨ Option 1: Double-Click (Mac) - **EASIEST**

**On macOS (your M3 Mac):**

1. **Find this file** in Finder:
   ```
   Interview_Whisperer.command
   ```

2. **Double-click it**

3. **Done!** The GUI opens automatically.

> **Note:** First time only, you may need to:
> - Right-click → "Open" (to bypass Gatekeeper)
> - Enter password (to allow terminal access)
> - After first time, regular double-click works!

---

## 🐍 Option 2: Pure Python - **NO SHELL REQUIRED**

**Run directly with Python:**

```bash
cd /home/user/interview-whisperer
python3 run.py
```

**Or double-click `run.py` if you have Python configured for that.**

This works on **any platform** (Mac, Linux, Windows).

---

## 🔧 Option 3: Shell Script - **ORIGINAL**

**Use the bash script:**

```bash
cd /home/user/interview-whisperer
./START_APP.sh
```

Same as Option 2, but uses bash instead of Python.

---

## 🎯 What Happens When You Launch?

**All 3 options do the same thing:**

```
1. Check Python is installed ✓
2. Create virtual environment (first time only) ✓
3. Install dependencies (first time only) ✓
4. Start Ollama (if not running) ✓
5. Launch GUI window ✓
```

**Result:** Beautiful GUI window appears!

```
┌──────────────────────────────────┐
│  🎯 Interview Whisperer          │
│  AI-Powered Interview Copilot    │
├──────────────────────────────────┤
│  System Status                   │
│  ✅ Ready to start!              │
│  🤖 Ollama: Connected            │
│  📄 Documents: 0 files           │
│             [🔄 Refresh Status]  │
├──────────────────────────────────┤
│  [📁 Manage Documents]           │
│                                  │
│  [🎯 Start Interview Mode]      │
│                                  │
│  [⚙️ Settings]                  │
├──────────────────────────────────┤
│  📂 Documents: .../documents     │
│  💡 Click 'Manage Documents'...  │
└──────────────────────────────────┘
```

**No terminal window stays open** - just the GUI!

---

## 💡 Recommended for Mac (M3):

**Use Option 1** (`Interview_Whisperer.command`)

- ✅ Native Mac experience
- ✅ Just double-click
- ✅ No terminal commands to remember
- ✅ Can put in Dock for easy access

### **Add to Dock:**

1. Drag `Interview_Whisperer.command` to your Dock
2. Now you can launch with one click anytime!

---

## 🆘 Troubleshooting

### "Permission denied"
```bash
chmod +x Interview_Whisperer.command
# Then double-click again
```

### "Python not found"
Install Python 3.10+ from https://python.org

### "Ollama not available"
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull models
ollama pull llama3.1:8b
ollama pull nomic-embed-text
```

---

## 🎉 Quick Start After Launch

1. **Add documents** (click "Manage Documents")
2. **Process them** (click "Process Documents" button)
3. **Start interview mode** (click "Start Interview Mode")
4. **Done!** AI copilot is listening.

---

**All three options are equivalent - use whichever you prefer!** ✨
