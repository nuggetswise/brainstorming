# PromptForge Demo

A minimal Claude Code extension demonstrating how to build productivity tools that run entirely in Claude Code.

## What Is This?

This is a **working demo** of a Claude Code extension. It shows how you can create powerful tools using just markdown files - no coding required!

## Installation

```bash
cd examples/promptforge-demo
claude /prompt-save   # Start using it immediately!
```

## Available Commands

| Command | Description |
|---------|-------------|
| `/prompt-save` | Save a prompt to your library |
| `/prompt-list` | View all saved prompts |
| `/prompt-load [name]` | Load a specific prompt |

## How It Works

1. **Just Markdown Files** - Each command is a `.md` file with instructions for Claude
2. **Local Data Storage** - Prompts saved in `.claude/prompts/`, indexed in JSON
3. **No Deployment** - Runs entirely in Claude Code on your machine
4. **Git-Friendly** - Version control your prompts like code!

## Example Usage

### Save a Prompt
```bash
claude /prompt-save

> What do you want to name this prompt?
code-review

> Paste or describe the prompt:
Review code for security, performance, and best practices...

> What category? (code/writing/analysis)
code

> Description (one sentence):
Comprehensive code review with actionable feedback

✓ Saved to .claude/prompts/code-review.md
```

### List Your Prompts
```bash
claude /prompt-list

Your Prompt Library
═══════════════════════════════════════
NAME           CATEGORY    DESCRIPTION
───────────────────────────────────────
code-review    code        Comprehensive review
bug-fix        code        Debug and fix issues
meeting-notes  writing     Summarize meetings

Total: 3 prompts
```

### Load a Prompt
```bash
claude /prompt-load code-review

Prompt: code-review (v1.0)
═══════════════════════════════════════

Review the following code for:
1. Security vulnerabilities
2. Performance issues
...

✓ Copy the text above to use this prompt!
```

## Why This Matters

This demo shows that you can build **full-featured productivity tools** using Claude Code without:
- ❌ Writing any code
- ❌ Deploying servers
- ❌ Managing databases
- ❌ Charging subscription fees

Instead:
- ✅ Just markdown files
- ✅ Runs locally
- ✅ Free forever
- ✅ 100% open source

## The Full Vision

This is a minimal demo. The full **PromptForge** extension would include:
- Version control (like Git for prompts)
- A/B testing framework
- Prompt benchmarking
- Community library
- Advanced search

See [`MISSION_DRIVEN_PROJECTS.md`](../../MISSION_DRIVEN_PROJECTS.md) for the complete spec!

## Build Your Own

Want to create your own Claude Code extension?

1. Copy this structure
2. Modify the command files
3. Add your own commands
4. Share on GitHub!

It's that simple. No coding required! 🚀

## Learn More

- [Mission-Driven Projects](../../MISSION_DRIVEN_PROJECTS.md) - 8 project ideas
- [Claude Code Docs](https://docs.claude.com/en/docs/claude-code)
- [Creating Custom Commands](https://docs.claude.com/en/docs/claude-code/custom-commands)

---

**License:** MIT
**Created:** November 2025
**Purpose:** Demonstrate Claude Code extension development
