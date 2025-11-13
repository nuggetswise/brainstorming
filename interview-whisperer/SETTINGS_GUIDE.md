# Settings Guide - Interview Whisperer

Complete guide to configuring Interview Whisperer settings for optimal performance.

---

## Overview

Interview Whisperer now includes a comprehensive settings system that allows you to customize:

- **Audio Settings** - Voice activation sensitivity, transcription parameters
- **Display Preferences** - Overlay appearance and positioning
- **Document Processing** - Chunk sizes and file type handling
- **LLM Configuration** - Model selection and generation parameters

All settings are stored in `data/settings.json` and persist across sessions.

---

## Accessing Settings

1. Launch Interview Whisperer
2. Click **"⚙️ Settings"** button
3. Use the tabbed interface to configure different aspects
4. Click **"💾 Save Settings"** to apply changes
5. **Restart Interview Mode** for changes to take effect

---

## Audio Settings Tab 🎤

### Whisper Model
**What it does:** Controls the transcription accuracy and speed

**Options:**
- `tiny` - Fastest, least accurate (good for testing)
- `base` - **Recommended** - Balanced speed and accuracy
- `small` - Better accuracy, slower
- `medium` - High accuracy, requires more resources
- `large` - Best accuracy, slowest

**Recommendation:** Use `base` for M3 Mac. Upgrade to `small` if transcription is inaccurate.

---

### Voice Activation Sensitivity
**What it does:** Controls how sensitive the microphone is to sound

**Range:** 0.001 (very sensitive) to 0.1 (requires loud speech)

**Default:** 0.01

**Tuning Guide:**
- **If it's picking up background noise:** Increase to 0.02-0.03
- **If it's missing your speech:** Decrease to 0.005-0.008
- **In quiet environment:** Keep at 0.01
- **In noisy environment:** Increase to 0.03-0.05

---

### Transcription Chunk Duration
**What it does:** How often audio is transcribed (in seconds)

**Range:** 1-30 seconds

**Default:** 5 seconds

**When to adjust:**
- **Shorter (2-3s):** More responsive, but higher CPU usage
- **Longer (7-10s):** Better context, less frequent updates
- **For interviews:** Keep at 5 seconds

---

### Silence Duration
**What it does:** How long silence must last after speech to trigger question detection

**Range:** 0.5-5.0 seconds

**Default:** 1.5 seconds

**When to adjust:**
- **Fast-paced interviews:** Reduce to 1.0 second
- **Thoughtful discussions:** Increase to 2.0-2.5 seconds
- **Multiple speakers:** Increase to 2.0 seconds

---

### Context Window
**What it does:** How much previous audio to keep in memory

**Range:** 10-120 seconds

**Default:** 30 seconds

**When to adjust:**
- **Short questions:** Keep at 30 seconds
- **Long discussions:** Increase to 60-90 seconds
- **RAM constrained:** Reduce to 20 seconds

---

## Display Preferences Tab 🖥️

### Overlay Width
**What it does:** Width of the suggestion window

**Range:** 200-1000 pixels

**Default:** 400 pixels

**Recommendation:**
- **Standard monitor (1080p):** 400-500 pixels
- **Large monitor (4K):** 600-800 pixels
- **Small screen:** 300-400 pixels

---

### Overlay Height
**What it does:** Height of the suggestion window

**Range:** 200-800 pixels

**Default:** 350 pixels

**Recommendation:**
- **Standard setup:** 350-400 pixels
- **More content visible:** 500-600 pixels
- **Minimal:** 250-300 pixels

---

### Transparency
**What it does:** How see-through the overlay window is

**Range:** 0.3 (very transparent) to 1.0 (fully opaque)

**Default:** 0.95

**When to adjust:**
- **Want to see through it:** 0.7-0.8
- **Prefer solid window:** 0.95-1.0
- **During screen sharing:** 1.0 (fully opaque)

---

### Overlay Position
**What it does:** Where the overlay appears on screen

**Options:**
- `top-right` - **Default** - Top right corner
- `top-left` - Top left corner
- `bottom-right` - Bottom right corner
- `bottom-left` - Bottom left corner
- `center` - Center of screen

**Recommendation:**
- **Zoom/Meet interviews:** `top-right` (away from video)
- **Teams interviews:** `bottom-right`
- **Screen sharing:** `top-left` (less obtrusive)

---

### Font Size
**What it does:** Base font size for text in overlay

**Range:** 8-16 pixels

**Default:** 10 pixels

**When to adjust:**
- **High DPI/4K monitors:** 12-14 pixels
- **Standard monitors:** 10-11 pixels
- **Reading difficulties:** 13-16 pixels

---

### Always on Top
**What it does:** Keeps overlay above all other windows

**Default:** Enabled

**When to disable:**
- You want overlay to be minimizable
- Working with full-screen applications
- Testing multiple windows

---

### Show Confidence Scores
**What it does:** Displays confidence percentage for each answer

**Default:** Enabled

**When to disable:**
- You trust all answers equally
- Prefer cleaner interface
- Find it distracting

---

### Show Source Documents
**What it does:** Lists which documents were used for answer

**Default:** Enabled

**When to disable:**
- You know your documents well
- Prefer minimal interface
- Limited screen space

---

## Document Processing Tab 📄

### Chunk Size
**What it does:** How many words per text chunk for embeddings

**Range:** 100-1000 words

**Default:** 500 words

**When to adjust:**
- **Short documents (resumes):** 300-400 words
- **Long documents (reports):** 600-800 words
- **Technical docs:** 400-500 words
- **Better context:** Larger chunks (700-800)
- **Faster processing:** Smaller chunks (300-400)

---

### Chunk Overlap
**What it does:** How many words overlap between chunks

**Range:** 0-200 words

**Default:** 50 words

**Purpose:** Ensures context isn't lost at chunk boundaries

**When to adjust:**
- **More continuity:** Increase to 75-100 words
- **Less redundancy:** Decrease to 25-40 words
- **Must be less than chunk size**

---

### Supported File Types
**What it does:** Which file extensions to process

**Default:** `.pdf`, `.docx`, `.txt`, `.md`

**Note:** Currently not editable in UI (future feature)

---

### Auto-Process New Documents
**What it does:** Automatically process documents when added to folder

**Default:** Disabled

**When to enable:**
- You frequently add documents
- Want seamless updates
- Have fast machine

**When to disable:**
- Manual control preferred
- Limited processing power
- Want to batch process

---

## LLM Settings Tab 🤖

### Ollama LLM Model
**What it does:** Which language model to use for answer generation

**Default:** `llama3.1:8b`

**Other options:**
- `llama3.1:70b` - Better answers, requires 40GB+ RAM
- `llama2:13b` - Older model, still good
- `mistral:7b` - Fast, concise answers
- `phi3:mini` - Lightweight, 4GB RAM

**To install a model:**
```bash
ollama pull llama3.1:8b
ollama pull mistral:7b
```

**Click "📋 List Models"** to see installed models

---

### Embedding Model
**What it does:** Model used to create document embeddings

**Default:** `nomic-embed-text`

**Alternative:** `all-minilm:l6-v2` (faster, less accurate)

**Note:** Changing this requires reprocessing all documents

---

### Temperature
**What it does:** Controls creativity/randomness of answers

**Range:** 0.0 (deterministic) to 2.0 (very creative)

**Default:** 0.7

**When to adjust:**
- **More consistent answers:** 0.3-0.5
- **More creative answers:** 0.8-1.0
- **For interviews (recommended):** 0.6-0.8
- **Technical questions:** 0.4-0.6
- **Behavioral questions:** 0.7-0.9

---

### Max Answer Tokens
**What it does:** Maximum length of generated answers

**Range:** 50-1000 tokens (~40-800 words)

**Default:** 250 tokens (~200 words)

**When to adjust:**
- **Concise answers:** 150-200 tokens
- **Detailed answers:** 300-400 tokens
- **Very brief:** 100-150 tokens
- **Long explanations:** 400-500 tokens

**Note:** 1 token ≈ 0.75 words on average

---

### Context Chunks to Retrieve
**What it does:** How many document chunks to use for context

**Range:** 1-10 chunks

**Default:** 3 chunks

**When to adjust:**
- **Simple questions:** 2-3 chunks
- **Complex questions:** 4-6 chunks
- **Faster generation:** 2 chunks
- **More thorough:** 5-7 chunks
- **More chunks = slower but more context**

---

### Ollama Host
**What it does:** URL of Ollama API server

**Default:** `http://localhost:11434`

**When to change:**
- Running Ollama on different port
- Using remote Ollama instance
- Testing with custom setup

---

## Resetting Settings

To reset all settings to defaults:

1. Open Settings dialog
2. Click **"🔄 Reset to Defaults"**
3. Review the default values
4. Click **"💾 Save Settings"** to apply

**Warning:** This cannot be undone. Current settings will be lost.

---

## Settings File Location

Settings are stored in:
```
interview-whisperer/data/settings.json
```

You can:
- **Backup:** Copy this file before making changes
- **Share:** Share your settings with others
- **Edit manually:** Edit JSON directly (be careful!)
- **Delete:** Delete file to reset to defaults

---

## Validation

Settings dialog validates your input:

- **Errors** (red) - Must be fixed before saving
- **Warnings** (yellow) - Can save, but may cause issues

Common validations:
- Chunk overlap must be less than chunk size
- Transparency must be between 0.1 and 1.0
- Temperature typically 0.0-2.0
- Display size within reasonable bounds

---

## Performance Tips

### For Best Performance:

**Audio:**
- Use `base` or `small` Whisper model
- Keep chunk duration at 5 seconds
- Adjust sensitivity to avoid false triggers

**Display:**
- Keep overlay size moderate (400x350)
- Use 0.9+ transparency for better readability
- Position away from main work area

**Documents:**
- Use 500-word chunks for balanced performance
- 50-word overlap is optimal
- Don't enable auto-process if you have 20+ documents

**LLM:**
- `llama3.1:8b` is best balance
- Keep max tokens at 250-300
- Use 3-4 context chunks
- Temperature 0.7 for interviews

---

## Troubleshooting

### Settings not saving?
- Check file permissions on `data/` directory
- Ensure `data/settings.json` is writable
- Look for validation errors in dialog

### Changes not taking effect?
- **Must restart Interview Mode** after saving settings
- Some changes (like Whisper model) require full app restart
- Check logs in `data/logs/` for errors

### Overlay not appearing?
- Check "Always on Top" is enabled
- Verify position isn't off-screen
- Try `center` position
- Increase transparency if too transparent

### Audio not sensitive enough?
- Lower silence threshold to 0.005-0.008
- Check microphone input level in system settings
- Try `small` Whisper model for better detection

---

## Best Practices

### For Job Interviews:

```json
{
  "audio": {
    "whisper_model": "base",
    "silence_threshold": 0.015,
    "chunk_duration": 5.0
  },
  "display": {
    "width": 400,
    "height": 350,
    "transparency": 0.95,
    "position": "top-right"
  },
  "llm": {
    "temperature": 0.7,
    "max_tokens": 250,
    "n_results": 3
  }
}
```

### For Technical Interviews:

```json
{
  "audio": {
    "whisper_model": "small",
    "silence_threshold": 0.01
  },
  "llm": {
    "temperature": 0.5,
    "max_tokens": 300,
    "n_results": 4
  }
}
```

### For Noisy Environments:

```json
{
  "audio": {
    "silence_threshold": 0.03,
    "silence_duration": 2.0
  }
}
```

---

## FAQ

**Q: Do I need to reprocess documents after changing chunk settings?**
A: Yes, chunk size changes require reprocessing. Go to Document Manager → Clear Database → Process Documents.

**Q: Can I use different LLM models?**
A: Yes! Any Ollama model works. Install with `ollama pull <model-name>`.

**Q: Will my settings be lost on update?**
A: No, `data/settings.json` persists across updates.

**Q: Can I share my settings?**
A: Yes! Copy `data/settings.json` to share with others.

**Q: What happens if I delete settings.json?**
A: App will recreate it with default values on next launch.

---

## Support

For issues or questions:
- Check logs: `data/logs/interview_whisperer_*.log`
- Verify settings.json is valid JSON
- Try resetting to defaults
- Check Ollama status: `ollama list`

---

**Last Updated:** November 13, 2025
**Version:** 2.0.0 (Settings System)
