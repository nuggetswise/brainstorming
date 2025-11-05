---
description: Load a saved prompt from your library
---

You are helping the user load a saved prompt.

## Steps:

1. **Check if they provided a name:**
   - If yes: Load that specific prompt
   - If no: Show list and ask which one to load

2. **Read the prompt file:**
   - Load from `.claude/prompts/{name}.md`
   - If not found: "Prompt '{name}' not found. Run `/prompt-list` to see available prompts."

3. **Display the prompt:**
   - Show the full prompt text
   - Show metadata (category, tags, version)

4. **Offer actions:**
   - "Copy this prompt to use it"
   - "Or run `/prompt-test {name}` to test it with examples"
   - "Run `/prompt-edit {name}` to modify it"

## Example Output:

```
Prompt: code-review (v1.0)
Category: code
Tags: code, review, security, performance
Created: 2025-11-05
═══════════════════════════════════════════════════════════

Review the following code for:
1. Security vulnerabilities
2. Performance issues
3. Best practices
4. Edge cases
5. Documentation quality

Provide specific, actionable feedback with code examples.

═══════════════════════════════════════════════════════════

✓ Prompt loaded! Copy the text above to use it.
```
