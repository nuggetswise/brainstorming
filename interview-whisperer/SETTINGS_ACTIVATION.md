# Settings Activation Flow - Interview Whisperer

## When Are Settings Activated?

This document explains exactly when and how settings take effect in Interview Whisperer.

---

## Settings Lifecycle

### 1. **On App Launch** (Startup)

```
User launches app
    ↓
launcher.py: __init__()
    ↓
SettingsManager() loads from data/settings.json
    ↓
Settings loaded into memory
    ↓
InterviewCopilot created with SettingsManager
    ↓
(Components NOT created yet - lazy initialization)
```

**What happens:**
- Settings file (`data/settings.json`) is loaded
- Settings stored in `SettingsManager` instance
- No components created yet (audio, overlay, etc.)
- Settings are **ready but not active**

---

### 2. **When User Clicks "Start Interview Mode"** (Activation)

```
User clicks "Start Interview Mode"
    ↓
launcher.py: start_interview_mode()
    ↓
copilot.start_interview_mode()
    ↓
copilot.initialize_components()  ← SETTINGS ACTIVATED HERE
    ↓
Components created with settings:
    - DocumentProcessor (chunk_size, chunk_overlap, extensions)
    - LLMEngine (model, temperature, max_tokens, n_results)
    - AudioEngine (whisper_model, sensitivity, chunk_duration)
    - OverlayWindow (size, position, transparency, fonts)
    ↓
Components running with your custom settings ✅
```

**What happens:**
- `initialize_components()` reads settings from SettingsManager
- Each component is created with your configured values
- **Settings are now ACTIVE and in use**

---

### 3. **When User Changes Settings** (Update)

```
User clicks "Settings" button
    ↓
Settings dialog opens
    ↓
User changes values
    ↓
User clicks "Save Settings"
    ↓
SettingsManager.save() writes to data/settings.json
    ↓
Settings saved to disk ✅
    ↓
(Interview Mode still using OLD settings)
    ↓
User clicks "Stop Interview Mode"
    ↓
Components destroyed
    ↓
User clicks "Start Interview Mode" again
    ↓
copilot.initialize_components() runs again
    ↓
NEW settings loaded and activated ✅
```

**What happens:**
- Settings saved to `data/settings.json`
- Currently running components **keep using old settings**
- **Must restart Interview Mode** for new settings to take effect
- Next time components are created, new settings are used

---

## Why Restart Is Required

### Design Decision: Safety & Stability

Components are created once when Interview Mode starts. We don't hot-reload settings because:

1. **Audio Engine**: Changing Whisper model mid-transcription could corrupt audio processing
2. **Overlay Window**: Resizing/repositioning while visible might cause rendering issues
3. **Document Processor**: Changing chunk size requires reprocessing all documents
4. **LLM Engine**: Changing models mid-generation could cause partial responses

**Solution:** Restart Interview Mode after changing settings. This ensures:
- Clean component initialization
- No partial state issues
- Consistent behavior
- Safer operation

---

## Settings Activation Timeline

| Event | Settings State | Components State | Active Settings |
|-------|---------------|------------------|----------------|
| App Launches | Loaded from JSON | Not created | None (default) |
| "Start Interview Mode" clicked | In memory | Creating... | **Activating** |
| Interview Mode running | In memory | Running | **Active** ✅ |
| User changes settings | Being edited | Running | Old settings still active |
| User saves settings | Saved to JSON | Running | Old settings still active |
| User stops Interview Mode | In memory | Destroyed | None |
| User starts Interview Mode again | Re-read from JSON | Creating... | **New settings activated** ✅ |

---

## Code Flow

### Startup (launcher.py)

```python
def __init__(self):
    # 1. Load settings from JSON
    self.settings_manager = SettingsManager()

    # 2. Pass settings to copilot (not activated yet)
    self.copilot = InterviewCopilot(settings_manager=self.settings_manager)
```

### Activation (interview_copilot.py)

```python
def initialize_components(self):
    # 3. Get settings from manager
    audio_config = self.settings_manager.get_audio_config()
    overlay_config = self.settings_manager.get_overlay_config()
    doc_config = self.settings_manager.get_document_config()
    llm_config = self.settings_manager.get_llm_config()

    # 4. Create components WITH settings
    self.audio_engine = AudioEngine(
        model=audio_config['model'],
        config=AudioConfig(
            silence_threshold=audio_config['silence_threshold'],
            chunk_duration=audio_config['chunk_duration'],
            # ... all audio settings
        )
    )

    self.overlay = OverlayWindow(
        width=overlay_config['width'],
        height=overlay_config['height'],
        transparency=overlay_config['transparency'],
        position=overlay_config['position'],
        # ... all overlay settings
    )

    # Settings now ACTIVE in components ✅
```

### Update (settings_dialog.py)

```python
def _save_settings(self):
    # 5. Update settings in memory
    self.settings.audio.silence_threshold = self.sensitivity_var.get()
    # ... update all settings

    # 6. Save to JSON file
    self.settings.save()  # → writes to data/settings.json

    # 7. Notify user
    messagebox.showinfo(
        "Success",
        "Settings saved! Restart Interview Mode for changes to take effect."
    )
```

---

## Quick Reference

### Q: When do settings take effect?
**A:** When you click "Start Interview Mode" AFTER saving settings.

### Q: Do I need to restart the app?
**A:** No, just stop and restart Interview Mode.

### Q: What if I don't restart Interview Mode?
**A:** Old settings stay active until you restart Interview Mode.

### Q: Can I see which settings are active?
**A:** Check the logs in `data/logs/interview_whisperer_*.log`
- Look for: `"Using custom settings from SettingsManager"`
- Check component initialization messages

### Q: What if settings file is deleted?
**A:** App creates new `settings.json` with defaults on next launch.

---

## Testing Your Settings

### 1. Verify Settings Were Saved

```bash
# Check settings file
cat interview-whisperer/data/settings.json

# Should show your changes
```

### 2. Verify Settings Were Loaded

```bash
# Check log file
tail -n 50 interview-whisperer/data/logs/interview_whisperer_*.log

# Look for:
# "Using custom settings from SettingsManager"
# "Audio engine initialized" (with your Whisper model)
# "Overlay window initialized" (with your dimensions)
```

### 3. Visual Verification

**Audio Settings:**
- Speak softly: Does it detect your voice? (sensitivity)
- Check transcription speed (chunk duration)

**Display Settings:**
- Is overlay in correct position?
- Is size what you configured?
- Is transparency correct?

**Document Settings:**
- Check processed chunks count (chunk size affects this)

**LLM Settings:**
- Check answer length (max tokens)
- Check answer creativity (temperature)

---

## Troubleshooting

### Settings not taking effect?

**1. Did you save?**
```bash
# Check if file was modified
ls -la interview-whisperer/data/settings.json
# Timestamp should be recent
```

**2. Did you restart Interview Mode?**
- Click "Stop Interview Mode"
- Click "Start Interview Mode"
- Settings now active ✅

**3. Check for errors**
```bash
# View log file
cat interview-whisperer/data/logs/interview_whisperer_*.log | grep -i error
```

**4. Validate settings**
- Open Settings dialog
- Check for validation errors (red text)
- Fix any issues
- Save again

### Settings file corrupted?

```bash
# Delete and let app recreate with defaults
rm interview-whisperer/data/settings.json

# Or restore from backup
cp settings.json.backup interview-whisperer/data/settings.json
```

---

## Best Practices

### 1. **Test Settings Before Important Interviews**

- Change one setting at a time
- Test with practice questions
- Verify everything works
- Only then save as your default

### 2. **Backup Your Settings**

```bash
# Before major changes
cp data/settings.json data/settings.json.backup

# To restore
cp data/settings.json.backup data/settings.json
```

### 3. **Use Validation Warnings**

- Yellow warnings = still works but may not be optimal
- Red errors = must fix before saving
- Listen to the validation advice

### 4. **Document Your Changes**

Keep notes on what settings work best for:
- Different interview types (technical vs behavioral)
- Different environments (quiet vs noisy)
- Different interviewers (fast vs slow speakers)

---

## Advanced: Programmatic Access

### Reading Current Active Settings

```python
from settings_manager import SettingsManager

settings = SettingsManager()

# Check what's configured
print(f"Sensitivity: {settings.audio.silence_threshold}")
print(f"Overlay size: {settings.display.width}x{settings.display.height}")
print(f"LLM model: {settings.llm.ollama_llm_model}")
```

### Modifying Settings Programmatically

```python
from settings_manager import SettingsManager

settings = SettingsManager()

# Change settings
settings.audio.silence_threshold = 0.02
settings.display.width = 500

# Validate
validation = settings.validate()
if validation['errors']:
    print("Errors:", validation['errors'])
else:
    # Save
    settings.save()
    print("Settings saved to data/settings.json")
```

---

## Summary

**When are settings activated?**
→ When you click "Start Interview Mode" after saving settings.

**The flow:**
1. Launch app → Settings loaded
2. Change settings → Settings saved to JSON
3. Stop Interview Mode → Components destroyed
4. Start Interview Mode → **Settings activated** ✅

**Key Point:**
Settings are activated during component initialization, which happens when Interview Mode starts. This ensures clean, safe initialization of all components with your configured values.

---

**Last Updated:** November 13, 2025
**Version:** 2.0 (Settings Activation)
