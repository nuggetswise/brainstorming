# PromptForge Demo

A minimal demo of a Claude Code extension for managing AI prompts.

## What This Does

PromptForge helps you save, organize, and reuse your best AI prompts.

## Available Commands

- `/prompt-save` - Save a new prompt to your library
- `/prompt-list` - View all saved prompts
- `/prompt-load [name]` - Load a specific prompt

## How to Use

1. Save your first prompt:
   ```
   /prompt-save
   ```

2. List all saved prompts:
   ```
   /prompt-list
   ```

3. Load a saved prompt:
   ```
   /prompt-load code-review
   ```

## Data Storage

All prompts are stored locally in:
- `.claude/prompts/` - Individual prompt files
- `.claude/data/prompt-index.json` - Searchable index

## This is Just a Demo!

This demonstrates how simple Claude Code extensions can be:
- Just markdown files with prompts
- No code required
- All data stays local
- Git-friendly

For the full PromptForge extension with versioning, A/B testing, and more,
see the complete project spec in the main MISSION_DRIVEN_PROJECTS.md document.
