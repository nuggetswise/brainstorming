# PromptForge: Repository Structure Template

**Purpose:** Copy-paste commands for AI Engineer on Day 1
**Use:** Create the full directory structure and initial files

---

## 🚀 Day 1 Setup Script

### Step 1: Create Directory Structure

```bash
# Create main project directory
mkdir promptforge-plugin
cd promptforge-plugin

# Initialize Git
git init

# Create all directories
mkdir -p .claude-plugin
mkdir -p skills/promptforge
mkdir -p agents
mkdir -p commands
mkdir -p prompts/product-management/01-strategy
mkdir -p prompts/product-management/02-research
mkdir -p prompts/product-management/03-execution
mkdir -p prompts/product-management/04-analysis
mkdir -p prompts/product-management/05-communication
mkdir -p prompts/product-management/06-special-workflows
mkdir -p docs
mkdir -p scripts

# Confirm structure
ls -R
```

---

### Step 2: Create plugin.json

**File:** `.claude-plugin/plugin.json`

```json
{
  "name": "promptforge",
  "version": "0.1.0",
  "description": "World-class Product Manager prompt library with AI-powered enhancement. 70+ prompts scored 8.5+ on CLEAR framework.",
  "author": "PromptForge Team",
  "license": "MIT",
  "homepage": "https://github.com/YOUR-ORG/promptforge-plugin",
  "repository": "https://github.com/YOUR-ORG/promptforge-plugin",
  "keywords": [
    "prompts",
    "product-management",
    "pm",
    "enhancement",
    "prd",
    "roadmap",
    "user-stories",
    "prioritization",
    "clear-framework"
  ],
  "components": {
    "skills": ["promptforge"],
    "agents": ["prompt-enhancer", "prompt-researcher"],
    "commands": ["prompt-browse", "prompt-enhance", "prompt-score"]
  },
  "requirements": {
    "claude-code": ">=1.0.0"
  },
  "category": "productivity",
  "tags": ["product", "management", "prompts", "ai-enhancement"]
}
```

---

### Step 3: Create .gitignore

**File:** `.gitignore`

```
# OS files
.DS_Store
Thumbs.db
.AppleDouble
.LSOverride

# IDE
.vscode/
.idea/
*.swp
*.swo
*.swn
*~

# Logs
*.log
logs/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Temp files
*.tmp
*.temp
.cache/

# Node (if adding scripts)
node_modules/
dist/
build/

# Python (if adding scripts)
__pycache__/
*.py[cod]
*$py.class
.venv/
venv/

# Testing
.coverage
*.cover
.pytest_cache/

# Environment
.env
.env.local

# Don't ignore these important directories
!.claude-plugin/
!skills/
!agents/
!commands/
!prompts/
!docs/
```

---

### Step 4: Create README.md

**File:** `README.md`

```markdown
# PromptForge

> World-class Product Manager prompt library with AI-powered enhancement

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CLEAR Framework](https://img.shields.io/badge/CLEAR-8.5%2B-brightgreen)]()

## What is PromptForge?

PromptForge is a curated library of 70+ PM prompts, each scored 8.5+ on the CLEAR quality framework, with AI-powered enhancement that adapts prompts to your specific context (industry, company stage, team structure).

### The Problem

Product Managers waste 5-10 hours per week:
- Crafting prompts from scratch for common tasks
- Tweaking generic prompts that "almost work"
- Losing good prompts across Slack, Notion, emails
- Paying $49 for static Gumroad PDFs that don't fit their context

### Our Solution

- **70 world-class prompts** (CLEAR score 8.5+) covering:
  - Strategy, Research, Execution, Analysis, Communication
- **AI-powered enhancement** adapts to:
  - Your industry (B2B SaaS, E-commerce, Healthcare, etc.)
  - Your stage (Startup, Growth, Enterprise)
  - Your preferences (detail level, output format, team context)
- **Native Claude Code integration** - one-command install
- **Free and open source** (MIT license)

## Installation

```bash
/plugin install promptforge
```

That's it! PromptForge will auto-activate when you need PM help.

## Quick Start

[TO BE ADDED - After Sprint 0]

## Features

- ✅ **Auto-Activation** - Detects when you need PM prompts
- ✅ **Browse Library** - Explore 70+ prompts by category
- ✅ **AI Enhancement** - Customize prompts for your context
- ✅ **Semantic Search** - Find prompts by use case
- ✅ **Quality Guaranteed** - All prompts scored 8.5+ CLEAR
- ✅ **Always Updated** - New prompts added regularly

## Documentation

- [Quality Standards (CLEAR Framework)](docs/QUALITY_STANDARDS.md)
- [Enhancement Guide](docs/ENHANCEMENT_GUIDE.md)
- [Prompt Template](docs/PROMPT_TEMPLATE.md)
- [Examples](docs/EXAMPLES.md)

## Contributing

[TO BE ADDED - After v1.0 launch]

## License

MIT © PromptForge Team

## Acknowledgments

Built with [Claude Code](https://code.claude.com/)
```

---

### Step 5: Create LICENSE

**File:** `LICENSE`

```
MIT License

Copyright (c) 2025 PromptForge Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

### Step 6: Create Placeholder Files

**Skill Placeholder:**
```bash
touch skills/promptforge/SKILL.md
```

**Agent Placeholders:**
```bash
touch agents/prompt-enhancer.md
touch agents/prompt-researcher.md
```

**Command Placeholders:**
```bash
touch commands/prompt-browse.md
touch commands/prompt-enhance.md
touch commands/prompt-score.md
```

**Documentation Placeholders:**
```bash
touch docs/PROMPT_TEMPLATE.md
touch docs/QUALITY_STANDARDS.md
touch docs/ENHANCEMENT_GUIDE.md
touch docs/ENHANCEMENT_TEMPLATES.md
touch docs/EXAMPLES.md
```

**Category READMEs:**
```bash
touch prompts/product-management/README.md
touch prompts/product-management/01-strategy/README.md
touch prompts/product-management/02-research/README.md
touch prompts/product-management/03-execution/README.md
touch prompts/product-management/04-analysis/README.md
touch prompts/product-management/05-communication/README.md
touch prompts/product-management/06-special-workflows/README.md
```

---

### Step 7: Initial Commit

```bash
# Add all files
git add .

# Create initial commit
git commit -m "Initial PromptForge plugin structure

- Set up directory structure
- Created plugin.json for marketplace
- Added README, LICENSE, .gitignore
- Created placeholder files for skills, agents, commands
- Ready for Sprint 0 development"

# Create remote (replace with your actual repo URL)
git remote add origin https://github.com/YOUR-ORG/promptforge-plugin.git

# Push to remote
git push -u origin main
```

---

### Step 8: Grant Access

```bash
# Add collaborator via GitHub UI or CLI
gh repo add-collaborator YOUR-ORG/promptforge-plugin PROMPT-ENGINEER-USERNAME
```

Or via GitHub web interface:
1. Go to repository Settings
2. Collaborators
3. Add PROMPT-ENGINEER-USERNAME

---

## 📋 Verification Checklist

After completing all steps, verify:

- [ ] Directory structure matches specification
- [ ] plugin.json is valid JSON (test with `cat .claude-plugin/plugin.json | python -m json.tool`)
- [ ] .gitignore includes all necessary patterns
- [ ] README.md has basic content
- [ ] LICENSE file exists (MIT)
- [ ] All placeholder files created
- [ ] Initial commit successful
- [ ] Remote repository set up
- [ ] Collaborator added (Prompt Engineer can access)
- [ ] No errors when running `git status`

---

## 🗂️ Expected Directory Tree

```
promptforge-plugin/
├── .claude-plugin/
│   └── plugin.json
├── .gitignore
├── LICENSE
├── README.md
├── agents/
│   ├── prompt-enhancer.md
│   └── prompt-researcher.md
├── commands/
│   ├── prompt-browse.md
│   ├── prompt-enhance.md
│   └── prompt-score.md
├── docs/
│   ├── ENHANCEMENT_GUIDE.md
│   ├── ENHANCEMENT_TEMPLATES.md
│   ├── EXAMPLES.md
│   ├── PROMPT_TEMPLATE.md
│   └── QUALITY_STANDARDS.md
├── prompts/
│   └── product-management/
│       ├── README.md
│       ├── 01-strategy/
│       │   └── README.md
│       ├── 02-research/
│       │   └── README.md
│       ├── 03-execution/
│       │   └── README.md
│       ├── 04-analysis/
│       │   └── README.md
│       ├── 05-communication/
│       │   └── README.md
│       └── 06-special-workflows/
│           └── README.md
├── scripts/
└── skills/
    └── promptforge/
        └── SKILL.md
```

---

## 🎯 Next Steps (After Day 1 Complete)

**Day 2:**
- Prompt Engineer: Fill in PROMPT_TEMPLATE.md, QUALITY_STANDARDS.md
- AI Engineer: Begin implementing SKILL.md

**Day 3-4:**
- Migrate first 3 prompts
- Test plugin installation

**Week 2:**
- Build subagents
- Add commands
- Complete integration

---

## 💡 Pro Tips

**For AI Engineer:**
1. Copy this entire script and run it in one go
2. Replace `YOUR-ORG` with actual organization name
3. Test plugin installation immediately after setup
4. Don't skip .gitignore - prevents accidental commits of temp files
5. Commit often, push daily

**Troubleshooting:**

**If `git push` fails:**
```bash
# Create repository on GitHub first, then:
git remote set-url origin https://github.com/YOUR-ORG/promptforge-plugin.git
git push -u origin main
```

**If directory creation fails:**
```bash
# Run commands one at a time instead of all at once
mkdir promptforge-plugin
cd promptforge-plugin
# ... etc
```

**If JSON validation fails:**
```bash
# Test plugin.json syntax
cat .claude-plugin/plugin.json | python -m json.tool

# Or use Node.js
node -e "JSON.parse(require('fs').readFileSync('.claude-plugin/plugin.json'))"
```

---

**Estimated Time:** 1-2 hours for complete setup

**Output:** Fully initialized repository ready for Sprint 0 development

**Last Updated:** November 6, 2025
