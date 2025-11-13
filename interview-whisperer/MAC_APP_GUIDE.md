# 🎯 Interview Whisperer - macOS App Guide

## ✨ You Now Have a True macOS Application!

Your Interview Whisperer is now a proper `.app` bundle that works just like any other Mac application.

---

## 🚀 How to Use

### **Method 1: Double-Click (Easiest)**

1. **Navigate to the project folder** in Finder:
   ```
   /home/user/interview-whisperer/
   ```

2. **Double-click:** `Interview Whisperer.app`

3. **First time only:**
   - Right-click → "Open"
   - Click "Open" in the security dialog
   - (This bypasses Gatekeeper for unsigned apps)

4. **After first time:**
   - Regular double-click works!

### **Method 2: Add to Applications Folder**

1. **Drag `Interview Whisperer.app` to `/Applications`**

2. **Launch from Launchpad or Spotlight:**
   - Press `Cmd + Space`
   - Type "Interview Whisperer"
   - Press Enter

### **Method 3: Add to Dock**

1. **Drag `Interview Whisperer.app` to your Dock**

2. **Click the icon anytime to launch**

---

## 🎨 What Happens When You Launch

```
You: *double-click Interview Whisperer.app*
     ↓
[First Time Only]
- Creates virtual environment
- Installs dependencies (2-3 minutes)
- Shows notification when ready
     ↓
[Every Time]
- Checks Python version ✓
- Activates virtual environment ✓
- Starts Ollama (if not running) ✓
- Shows "Starting Interview Whisperer..." notification ✓
     ↓
🖥️ Beautiful GUI Window Opens!
```

**No terminal window** - just clean notifications and the GUI!

---

## 🎨 Customize the App Icon

The app currently uses the default system icon. To add a custom icon:

### **Quick Method:**

1. **Find an icon you like** (PNG, 1024x1024 recommended)
   - Search "microphone icon" or "target icon"
   - Or design your own

2. **Convert to .icns:**
   - Use: https://cloudconvert.com/png-to-icns
   - Upload PNG → Download .icns

3. **Add to app:**
   ```bash
   cp YourIcon.icns "/home/user/interview-whisperer/Interview Whisperer.app/Contents/Resources/AppIcon.icns"
   ```

4. **Refresh icon cache:**
   ```bash
   touch "/home/user/interview-whisperer/Interview Whisperer.app"
   killall Finder
   ```

**Icon suggestions:**
- 🎤 Microphone (represents interview audio)
- 🎯 Target/Bullseye (represents precision)
- 💡 Light bulb (represents intelligent suggestions)
- 🗣️ Speech bubble (represents conversation)

---

## 🔧 How It Works

### **App Structure:**

```
Interview Whisperer.app/
├── Contents/
│   ├── Info.plist          (App metadata - name, version, permissions)
│   ├── PkgInfo             (App type identifier)
│   ├── MacOS/
│   │   └── launcher        (Executable script - runs when app opens)
│   └── Resources/
│       └── AppIcon.icns    (App icon - optional)
```

### **Project Files:**

The `.app` lives **inside** your project folder:

```
/home/user/interview-whisperer/
├── Interview Whisperer.app/    ← The macOS application
├── app/                         ← Python source code
├── documents/                   ← Your interview documents
├── data/                        ← Database and logs
└── venv/                        ← Virtual environment (auto-created)
```

**The app accesses the surrounding project files** - everything stays organized in one place!

---

## 📱 Permissions

The app requests these macOS permissions:

### **Microphone Access** 🎤
- **Why:** To capture interview questions in real-time
- **When:** When you click "Start Interview Mode"
- **How to grant:**
  1. System Settings → Privacy & Security → Microphone
  2. Enable "Interview Whisperer" or "Terminal"

### **Files and Folders** 📁
- **Why:** To read your documents from the documents/ folder
- **When:** When you process documents
- **Automatic:** Should be granted automatically

---

## 🆘 Troubleshooting

### **"Interview Whisperer.app is damaged and can't be opened"**

This happens because the app is not code-signed. Fix:

```bash
# Remove quarantine flag
xattr -cr "/home/user/interview-whisperer/Interview Whisperer.app"

# Then right-click → Open (first time)
```

### **"Python 3 is required but not installed"**

Install Python:
```bash
# Using Homebrew
brew install python@3.11

# Or download from:
# https://www.python.org/downloads/
```

### **"Ollama is not installed"**

Install Ollama:
```bash
# Install
curl -fsSL https://ollama.ai/install.sh | sh

# Pull required models
ollama pull llama3.1:8b
ollama pull nomic-embed-text
```

### **App won't open / nothing happens**

Check the Console app for errors:
1. Open **Console.app**
2. Search for "Interview Whisperer"
3. Look for error messages

Or check logs:
```bash
ls -la /home/user/interview-whisperer/data/logs/
```

### **Microphone not working**

Grant microphone permission:
1. **System Settings** → **Privacy & Security** → **Microphone**
2. Enable for "Interview Whisperer" or "Terminal"
3. Restart the app

---

## 🎁 Benefits of .app Bundle

**Before (using .command file):**
- ⚠️ Terminal window stays open
- ⚠️ Looks like a script
- ⚠️ Can't add to Applications
- ⚠️ No custom icon

**Now (using .app):**
- ✅ No terminal window
- ✅ Looks like a real app
- ✅ Can add to Applications/Dock
- ✅ Custom icon support
- ✅ Proper Mac experience
- ✅ Native notifications

---

## 🔄 Updating the App

When you update Interview Whisperer code:

**The app automatically uses the latest code!**

Why? Because the `.app` is just a launcher that runs your Python files. Update the Python files, and the app uses them immediately - no rebuild needed.

To update:
1. Pull latest code: `git pull`
2. Update dependencies: `source venv/bin/activate && pip install -r requirements.txt`
3. Launch app as normal

---

## 📦 Sharing with Others

**Current setup:** Works only on your Mac (requires Python/Ollama installed)

**To share with someone else:**
1. They need Python 3.10+ installed
2. They need Ollama installed
3. Give them the entire project folder (not just the .app)
4. They can double-click the .app

**For true sharing:** Would need Option 3 (py2app) to bundle everything into a self-contained app (~300MB).

---

## 🎯 What's Different from Other Options?

| Feature | .command File | .app Bundle | py2app Bundle |
|---------|---------------|-------------|---------------|
| **Mac-native** | ❌ | ✅ | ✅ |
| **Terminal-free** | ❌ | ✅ | ✅ |
| **In Applications** | ❌ | ✅ | ✅ |
| **Custom icon** | ❌ | ✅ | ✅ |
| **Self-contained** | ❌ | ❌ | ✅ |
| **File size** | 1 KB | 10 KB | 300 MB |
| **Setup time** | None | 30 min | 1-2 hrs |

**You have the .app bundle** - perfect balance of native experience and simplicity!

---

## 🚀 Quick Start Recap

1. **Double-click** `Interview Whisperer.app`
2. **First time:** Right-click → "Open" → Click "Open"
3. **Wait for setup** (first launch only, 2-3 minutes)
4. **Use the GUI!**

That's it! Enjoy your native Mac app experience! 🎉

---

## 📞 Need Help?

- **Documentation:** See `README.md` in project root
- **Logs:** Check `data/logs/` folder
- **Console:** Open Console.app and search "Interview Whisperer"

---

**Enjoy your Interview Whisperer macOS app!** 🎯✨
