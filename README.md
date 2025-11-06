# PromptForge: Product Manager Prompt Library

**World-class PM prompt library with AI-powered enhancement - Native Claude Code Plugin**

> 70+ prompts scored 8.5+ on CLEAR framework | Free & Open Source | One-command install

---

## 🎯 Current Status: Sprint 0 - Implementation Ready

**Timeline:** 14 days (2 weeks)
**Start Date:** [TBD]
**Team:** Prompt Engineer + AI Engineer

### Sprint 0 Goals

Build the foundation for PromptForge v1.0:
- ✅ Plugin infrastructure & marketplace integration
- ✅ PromptForge Skill (auto-activation, browse, load, search)
- ✅ 2 specialized subagents (Prompt Enhancer + Prompt Researcher)
- ✅ 3 custom commands (/prompt-browse, /prompt-enhance, /prompt-score)
- ✅ 3 prompts migrated to new format (CLEAR ≥9.0)
- ✅ All 10 edge cases handled gracefully

**Success Criteria:** Working plugin demonstrating AI-powered enhancement that improves CLEAR scores by +0.3

---

## 📚 Sprint 0 Documentation

**Essential Reading (In Order):**

1. **[PROMPTFORGE_PRODUCT_PLAN_V2.md](PROMPTFORGE_PRODUCT_PLAN_V2.md)** ⭐
   - The definitive product plan
   - 70 prompts across 6 categories
   - Plugin architecture & subagent system
   - CLEAR framework explained
   - 8.5-week roadmap (Sprint 0-4)
   - **Read this first**

2. **[PROMPTFORGE_TEAM_ONBOARDING.md](PROMPTFORGE_TEAM_ONBOARDING.md)**
   - Complete onboarding for both engineers
   - CLEAR framework deep dive
   - Role-specific responsibilities
   - All 10 edge cases documented
   - Enhancement methodology
   - Collaboration protocols

3. **[PROMPTFORGE_SPRINT0_KICKOFF.md](PROMPTFORGE_SPRINT0_KICKOFF.md)**
   - Pre-sprint checklist
   - Day 1 kickoff meeting agenda
   - Daily tasks for Week 1
   - Troubleshooting guide

4. **[PROMPTFORGE_SPRINT0_TASKS.md](PROMPTFORGE_SPRINT0_TASKS.md)**
   - 14-day day-by-day breakdown
   - Hour-by-hour task estimates
   - Clear deliverables per day
   - Daily standup templates

5. **[PROMPTFORGE_QUICK_REFERENCE.md](PROMPTFORGE_QUICK_REFERENCE.md)**
   - One-page cheat sheet
   - CLEAR formula & thresholds
   - Project structure diagram
   - Edge cases summary
   - Keep this open while working

6. **[PROMPTFORGE_REPO_TEMPLATE.md](PROMPTFORGE_REPO_TEMPLATE.md)**
   - Copy-paste setup script for Day 1
   - Complete directory structure
   - plugin.json template
   - Verification checklist

---

## 🏗️ What is PromptForge?

### The Problem

Product Managers waste 5-10 hours per week:
- Crafting prompts from scratch for common tasks (PRDs, roadmaps, user stories)
- Tweaking generic prompts that "almost work"
- Losing good prompts across Slack, Notion, emails
- Paying $49 for static Gumroad PDFs that don't fit their context

### Our Solution

**PromptForge = 70 world-class prompts + AI-powered customization**

- **70 pre-made prompts** (CLEAR score 8.5+) covering:
  - Strategy (vision, roadmaps, OKRs)
  - Research (interviews, personas, competitive analysis)
  - Execution (PRDs, user stories, sprint planning)
  - Analysis (A/B tests, metrics, data analysis)
  - Communication (stakeholder updates, exec summaries)

- **AI enhancement** adapts prompts to:
  - Your industry (B2B SaaS, E-commerce, Healthcare, etc.)
  - Your stage (Startup, Growth, Enterprise)
  - Your preferences (detail level, output format, team context)

- **Native Claude Code plugin** - One-command install: `/plugin install promptforge`

- **Free and open source** (MIT license)

---

## 🎨 Key Features

### 1. Auto-Activation
Skill detects when you need PM help and proactively suggests prompts

### 2. Quality Guaranteed
All prompts scored 8.5+ using CLEAR framework:
- **C**larity (25%) - Unambiguous instructions
- **L**ength (20%) - Appropriate detail
- **E**xamples (20%) - Concrete output examples
- **A**udience (15%) - Target user explicit
- **R**esult (20%) - Output format defined

### 3. AI-Powered Enhancement
Two specialized subagents:
- **Prompt Enhancer** - Customizes prompts for your context
- **Prompt Researcher** - Searches and recommends prompts

Target improvement: +0.3 to +0.5 CLEAR score

### 4. Intelligent Edge Handling
10 edge cases handled gracefully:
- Enhancement makes score worse → Recommends original
- Impossible combination → Suggests alternatives
- User abandons mid-flow → Saves progress, allows resume
- Already optimized → Explains, offers other dimensions
- Timeout → Chunks work, saves partial results
- [+ 5 more edge cases for search/discovery]

---

## 🚀 Getting Started (Post-Launch)

```bash
# Install PromptForge
/plugin install promptforge

# That's it! Auto-activates when needed
```

**Usage Examples:**
```
You: "I need to write a PRD"
→ Claude suggests PRD Writing prompt (9.2 CLEAR)
→ Offers to enhance for your context

You: "Customize for B2B SaaS, Growth stage"
→ Enhanced prompt with SaaS metrics, stakeholders, examples
→ CLEAR score improved: 9.2 → 9.5
```

---

## 📐 Architecture Overview

```
promptforge-plugin/
├── .claude-plugin/
│   └── plugin.json              # Marketplace metadata
├── skills/promptforge/
│   └── SKILL.md                 # Main auto-activation skill
├── agents/
│   ├── prompt-enhancer.md       # Customization specialist
│   └── prompt-researcher.md     # Search & discovery
├── commands/
│   ├── prompt-browse.md         # /prompt-browse
│   ├── prompt-enhance.md        # /prompt-enhance
│   └── prompt-score.md          # /prompt-score
├── prompts/product-management/
│   ├── 01-strategy/             # 10 prompts
│   ├── 02-research/             # 15 prompts
│   ├── 03-execution/            # 15 prompts
│   ├── 04-analysis/             # 12 prompts
│   ├── 05-communication/        # 10 prompts
│   └── 06-special-workflows/    # 8 prompts
└── docs/
```

---

## 📅 Roadmap

### Sprint 0 (Week 1-2) - **CURRENT**
- Plugin infrastructure
- 2 subagents with edge cases
- 3 prompts migrated

### Sprint 1 (Week 3-4)
- 20 P0 prompts (CLEAR 9.0+)

### Sprint 2 (Week 5)
- Enhancement refinement

### Sprint 3 (Week 6-7)
- 50 P1 prompts (CLEAR 8.5+)

### Sprint 4 (Week 8)
- Polish, documentation, launch

**Target Launch:** 8 weeks from Sprint 0 start

---

## 🏆 Competitive Advantages

**vs Gumroad PM Prompt Library ($49):**

| Feature | Gumroad | PromptForge |
|---------|---------|-------------|
| Format | Static CSV/Notion | Dynamic plugin |
| Customization | None (manual editing) | AI-powered enhancement |
| Quality Metrics | "Battle-tested" (vague) | CLEAR 8.5+ (objective) |
| Updates | None after purchase | Auto-notify, git-based |
| Price | $49 | Free (open source) |
| Integration | Copy/paste manually | Native Claude Code |
| Context Awareness | None | Adapts to industry/stage |
| Team Sharing | Buy per user | Free, repo-based |

**Our moat:** AI enhancement + objective quality metrics + native integration

---

## 📊 Success Metrics

**Sprint 0:**
- [ ] Plugin installs successfully (>95% success rate)
- [ ] Enhancement improves CLEAR scores by +0.3 avg
- [ ] All 10 edge cases handled gracefully
- [ ] Zero critical bugs

**Launch (Week 1):**
- 50+ plugin installs
- 4.5/5 marketplace rating
- 20+ enhancement sessions

**Month 1:**
- 200+ plugin installs
- 100+ active users
- Featured in Claude Code marketplace

**Month 3:**
- 1,000+ plugin installs
- 500+ active users
- Featured in PM newsletter

---

## 📞 Team & Contact

**Current Team:**
- Product Lead
- AI Engineer (infrastructure, subagents, commands)
- Prompt Engineer (content, quality, enhancement)

**Status:** Ready for Sprint 0 kickoff
**Documentation:** 100% complete
**Timeline:** 8.5 weeks to launch

---

## 📁 Archive

**Looking for legacy documents?**

See **[archive/](archive/)** directory:
- `archive/promptforge-legacy/` - Earlier planning iterations
- `archive/other-projects/` - Other project research

All insights from archived docs have been incorporated into Product Plan v2.0.

See **[archive/ARCHIVE_README.md](archive/ARCHIVE_README.md)** for details.

---

## 📝 License

MIT © PromptForge Team

---

## 🎯 Next Steps

1. **Review Documentation** (Today)
   - Read Product Plan v2.0 (60 min)
   - Skim Team Onboarding (30 min)
   - Review Sprint 0 Kickoff (15 min)

2. **Team Alignment** (This Week)
   - Get engineer commitments
   - Schedule kickoff meeting
   - Set up repository & tools

3. **Sprint 0 Kickoff** (Next Week)
   - Day 1: Kickoff meeting + initial setup
   - Week 1: Foundation (repo, skill, 3 prompts)
   - Week 2: Intelligence (2 subagents + commands)
   - Day 14: Demo & retrospective

**Ready to build something amazing? Let's go! 🚀**

---

**Last Updated:** November 6, 2025
**Version:** 1.0 (Sprint 0 Ready)
**Status:** ✅ Implementation Ready
