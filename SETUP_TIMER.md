# Interview Timer - Setup Guide

## 🚀 Quick Start (5 minutes)

### Step 1: Install Dependencies

```bash
pip install sounddevice numpy
```

Or using the requirements file:
```bash
pip install -r requirements.txt
```

### Step 2: Run the Timer

```bash
python interview_timer.py
```

That's it! A floating green circle should appear on your screen.

---

## 🎯 How to Use

1. **Position the timer**: Drag it anywhere on your screen (won't block your Zoom window)

2. **Start practicing**:
   - Have your friend ask you a question
   - Start answering (speak for ~3 seconds)
   - Timer auto-starts! 🎤

3. **Watch the colors**:
   - 🟢 **Green (0-60s)**: You're on track, keep going
   - 🟡 **Yellow (60-90s)**: Start wrapping up your answer
   - 🔴 **Red (90s+)**: Finish your answer now!

4. **Reset for next question**: Double-click the timer

5. **Close when done**: Click the X or close the terminal window

---

## ⚙️ Customization

Open `interview_timer.py` and adjust these settings:

### Change Time Thresholds
```python
# Around line 115-120 in update_display() function
if seconds < 60:      # Change this to adjust yellow warning time
    color = '#4CAF50'
elif seconds < 90:    # Change this to adjust red warning time
    color = '#FFC107'
```

### Adjust Microphone Sensitivity
```python
# Line 41
self.audio_threshold = 0.02  # Lower = more sensitive, Higher = less sensitive
```

If timer starts too easily (background noise), increase to `0.03` or `0.04`
If timer doesn't start when you speak, decrease to `0.015` or `0.01`

### Change Speech Detection Time
```python
# Line 42
self.speech_duration_needed = 2.5  # Seconds of speech needed to trigger
```

Increase if timer starts during "umm..." or throat clearing
Decrease for faster triggering

### Change Window Size
```python
# Line 22
self.window_size = 150  # Make larger (200) or smaller (100)
```

---

## 🐛 Troubleshooting

### "No module named sounddevice"
```bash
pip install sounddevice numpy
```

### Timer doesn't start when speaking
- **Check microphone permissions** (System Settings > Privacy > Microphone)
- **Adjust sensitivity**: Change `audio_threshold` to `0.01` (line 41)
- **Test microphone**: Record a voice memo to ensure mic works

### Timer starts too easily (false triggers)
- **Increase threshold**: Change `audio_threshold` to `0.03` or `0.04`
- **Increase speech duration**: Change `speech_duration_needed` to `3.0` or `3.5`

### Window won't stay on top
- This is rare, but if it happens, the window might hide behind Zoom
- Try clicking it to bring to front
- On Mac: System Settings > Accessibility > Display > Reduce transparency

### "Audio error" message
- **Mac**: System Settings > Privacy & Security > Microphone > Terminal (allow)
- **Windows**: Settings > Privacy > Microphone > Allow apps (enable Python)
- **Linux**: Check `alsa-utils` or `pulseaudio` is installed

---

## 💡 Pro Tips

1. **Position before interview**: Put timer in top-right corner where you can glance at it

2. **Practice awareness**: Don't stare at timer, just use peripheral vision

3. **Calibrate sensitivity**: Do a test run with your friend before real practice

4. **Multiple monitors**: Works great on second monitor!

5. **Quick exit**: Press Ctrl+C in terminal or close window

---

## 🎨 What It Looks Like

```
┌─────────────────┐
│                 │
│   🟢 Green      │
│                 │
│     00:45       │   (0-60 seconds)
│   On track ✓    │
│                 │
└─────────────────┘

┌─────────────────┐
│                 │
│   🟡 Yellow     │
│                 │
│     01:15       │   (60-90 seconds)
│   Wrap up!      │
│                 │
└─────────────────┘

┌─────────────────┐
│                 │
│   🔴 Red        │
│                 │
│     01:35       │   (90+ seconds)
│  Finish now!    │
│                 │
└─────────────────┘
```

---

## 🔧 Technical Details

**No LLM needed** - Uses simple audio volume detection
**All local** - No data sent anywhere, mic data stays on your computer
**Lightweight** - ~150 lines of Python, minimal CPU usage
**Cross-platform** - Works on Mac, Windows, Linux

---

## 📝 Notes

- Timer keeps running during pauses (realistic interview simulation)
- Window position is remembered within session
- Double-click anywhere on circle to reset
- Works over Zoom, Google Meet, Teams, any video call software

---

**Questions?** Check the troubleshooting section or adjust the sensitivity settings!

**Enjoy your interview practice!** 🎯
