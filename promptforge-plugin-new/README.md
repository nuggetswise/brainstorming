# PromptForge

**70+ world-class Product Management prompts with AI-powered enhancement**

> Native Claude Code plugin | Free & Open Source | PRIME 8.5+ Quality

Complete plugin structure created following Claude Code specifications.

## Status

**Version:** 0.1.0 (Sprint 0 - Infrastructure Complete)

**Completed:**
- ✅ Plugin manifest (plugin.json)
- ✅ PromptForge Skill (auto-activation, 3 modes)
- ✅ Prompt Enhancer agent (5 edge cases)
- ✅ Prompt Researcher agent (5 edge cases)
- ✅ 3 commands (/prompt-browse, /prompt-enhance, /prompt-score)
- ✅ 6 category structures with READMEs
- ✅ Quality standards documentation (PRIME framework)
- ✅ Prompt template for contributors

**Next Steps:**
- Sprint 1: Migrate 20 P0 prompts (PRIME 9.0+)
- Sprint 2: Enhancement refinement
- Sprint 3: Add 50 P1 prompts (PRIME 8.5+)
- Sprint 4: Polish and launch

## Installation

```bash
# Via Claude Code marketplace (when published)
/plugin install promptforge

# Manual install (development)
cd ~/.claude-code/plugins/
git clone https://github.com/nuggetswise/promptforge
```

## Quick Start

```
/prompt-browse [category]    # Explore prompts
/prompt-enhance [name]       # Customize prompt
/prompt-score [text]         # Calculate PRIME score
```

## Documentation

- [Quality Standards](docs/QUALITY_STANDARDS.md) - PRIME framework explained
- [Prompt Template](docs/PROMPT_TEMPLATE.md) - How to create prompts

## License

MIT
