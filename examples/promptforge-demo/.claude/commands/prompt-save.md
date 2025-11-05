---
description: Save a prompt to your library for reuse
---

You are helping the user save a prompt to their prompt library.

## Steps:

1. **Ask for the prompt name:**
   - Should be descriptive (e.g., "code-review", "summarize-meeting")
   - Use kebab-case format

2. **Ask them to provide the prompt:**
   - They can paste it or describe what it does
   - If they describe it, help them write a good prompt

3. **Ask for metadata:**
   - Category (code, writing, analysis, etc.)
   - Description (one sentence)
   - Tags (comma-separated)

4. **Save the prompt:**
   - Create file: `.claude/prompts/{name}.md`
   - Include metadata at the top
   - Add to index: `.claude/data/prompt-index.json`

5. **Confirm:**
   - Show the saved location
   - Suggest: "Run `/prompt-list` to see all your saved prompts"

## Example Prompt File:

```markdown
---
name: code-review
category: code
description: Comprehensive code review with security and performance checks
tags: code, review, security, performance
created: 2025-11-05
version: 1.0
---

Review the following code for:
1. Security vulnerabilities
2. Performance issues
3. Best practices
4. Edge cases
5. Documentation quality

Provide specific, actionable feedback with code examples.
```
