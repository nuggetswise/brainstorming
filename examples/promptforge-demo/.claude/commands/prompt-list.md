---
description: List all saved prompts in your library
---

You are showing the user their prompt library.

## Steps:

1. **Read the prompt index:**
   - Load `.claude/data/prompt-index.json`
   - If it doesn't exist, say "No prompts saved yet. Run `/prompt-save` to add your first prompt!"

2. **Display prompts in a formatted table:**

```
Your Prompt Library
═══════════════════════════════════════════════════════════

NAME                  CATEGORY     DESCRIPTION
────────────────────────────────────────────────────────────
code-review           code         Comprehensive code review
meeting-summary       writing      Summarize meeting notes
bug-analysis          code         Analyze and fix bugs
email-draft           writing      Draft professional emails

Total: 4 prompts
```

3. **Provide helpful actions:**
   - `/prompt-load [name]` - Load a prompt
   - `/prompt-save` - Save a new prompt
   - `/prompt-search [query]` - Search prompts

4. **Suggest next steps:**
   - If they have 0 prompts: "Start by running `/prompt-save` to create your first prompt!"
   - If they have prompts: "Use `/prompt-load [name]` to use a saved prompt"
