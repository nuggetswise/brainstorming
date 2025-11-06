# PromptForge: Quick Reference Card

**Sprint 0 Duration:** 14 days
**Goal:** Plugin + 2 Subagents + 3 Prompts
**Minimum Quality:** CLEAR 8.5+

---

## 📐 CLEAR Framework (Quick)

**C - Clarity (25%):** Instructions specific and unambiguous
**L - Length (20%):** Appropriate detail (50-800 words)
**E - Examples (20%):** Concrete output examples (2-3 scenarios)
**A - Audience (15%):** Target user and context explicit
**R - Result (20%):** Output format and success criteria defined

**Formula:**
```
CLEAR = (C×0.25) + (L×0.20) + (E×0.20) + (A×0.15) + (R×0.20)
```

**Thresholds:**
- 🏆 9.0-10.0 = WORLD-CLASS
- ⭐ 8.5-8.9 = EXCELLENT
- ✅ 8.0-8.4 = GOOD (iterate)
- ⚠️ <8.0 = NEEDS WORK

---

## 🏗️ Project Structure

```
promptforge-plugin/
├── .claude-plugin/
│   └── plugin.json                # Marketplace metadata
├── skills/promptforge/
│   └── SKILL.md                   # Main auto-activation skill
├── agents/
│   ├── prompt-enhancer.md         # Customization specialist
│   └── prompt-researcher.md       # Search & discovery
├── commands/
│   ├── prompt-browse.md           # /prompt-browse
│   ├── prompt-enhance.md          # /prompt-enhance
│   └── prompt-score.md            # /prompt-score
├── prompts/product-management/
│   ├── 01-strategy/
│   ├── 02-research/
│   ├── 03-execution/
│   ├── 04-analysis/
│   ├── 05-communication/
│   └── 06-special-workflows/
└── docs/
    ├── PROMPT_TEMPLATE.md
    ├── QUALITY_STANDARDS.md
    ├── ENHANCEMENT_GUIDE.md
    └── ENHANCEMENT_TEMPLATES.md
```

---

## 🎯 Enhancement Dimensions

**1. Industry** (7 options)
- B2B SaaS, E-commerce, Consumer Apps, Enterprise
- Healthcare, FinTech, Marketplace

**2. Company Stage** (4 options)
- Startup, Growth, Late-stage, Enterprise

**3. Detail Level** (3 options)
- Quick (15 min), Standard (30-45 min), Comprehensive (60+ min)

**4. Output Format** (5 options)
- Executive Brief, Standard Report, Detailed Analysis, Presentation, Dashboard

**5. Team Context** (5 options)
- Solo PM, PM+Designer, PM+Analyst, Product Trio, Cross-functional

**Target:** +0.3 to +0.5 CLEAR score improvement

---

## 🛡️ Edge Cases (10 Total)

### Prompt Enhancer (5)
1. Enhancement makes score worse → Show comparison, recommend original
2. Impossible combination → Explain conflict, suggest alternatives
3. User abandons → Save state, allow resume
4. Already industry-specific → Explain, offer other dimensions
5. Timeout → Chunk work, save partial progress

### Prompt Researcher (5)
1. No results → Suggest related, broader search
2. Too many results → Group by category, clarify
3. Vague request → Interactive Q&A
4. Unrelated comparison → Clarify intent, suggest logical alternatives
5. Handoff to enhancer → Detect context, delegate

---

## 📋 Prompt Template (YAML Frontmatter)

```yaml
---
name: [Prompt Name]
category: strategy|research|execution|analysis|communication|special
subcategory: [specific area]
description: [One-line description]
clear_score: [X.X]
industry: all|b2b-saas|ecommerce|enterprise|consumer|healthcare|fintech|marketplace
company_stage: all|startup|growth|enterprise
time_estimate: [X-Y min]
difficulty: beginner|intermediate|advanced
frameworks: [Array of framework names]
tags: [Array of keywords]
related_prompts: [Array of related prompt names]
version: X.X
last_updated: YYYY-MM-DD
---
```

---

## 📋 Prompt Template (Content Structure)

```markdown
# [Prompt Title]

**Purpose:** [What this achieves]
**Best For:** [Specific use cases]
**Time Required:** [X-Y min]

---

## Context & Audience

**Target User:** [Who should use this]
**When to Use:** [Situations]
**Prerequisites:**
- [What data/info needed]
- [What knowledge assumed]

---

## Instructions

### Step 1: [Clear step name]
[Specific, actionable instructions]

**What to do:**
- [Bullet 1]
- [Bullet 2]

**What to avoid:**
- ❌ [Common mistake 1]
- ❌ [Common mistake 2]

[Repeat for each step...]

---

## Expected Output

**Format:** [Markdown, table, etc.]
**Structure:**
1. [Section 1]: [Description]
2. [Section 2]: [Description]

**Length:** [Word/page count]

**Success Criteria:**
- ✅ [Criterion 1]
- ✅ [Criterion 2]

---

## Example Output

```
[Show realistic example following exact format]
```

---

## Frameworks Reference

**[Framework Name]:**
- [Brief explanation]
- [When to use]

---

## Tips & Best Practices

💡 **Pro Tips:**
- [Tip 1]
- [Tip 2]

⚠️ **Common Pitfalls:**
- [Pitfall 1 and how to avoid]

🔗 **Related Prompts:**
- [Prompt name]: [When to use]

---

## Customization Options

This prompt can be enhanced for:
- **Industry:** [Variations available]
- **Company Stage:** [Considerations]
- **Detail Level:** [Options]
- **Output Format:** [Alternatives]

💬 **Want a customized version?** Ask Claude to enhance!
```

---

## 🎯 Sprint 0 Deliverables Checklist

### Week 1 (Days 1-7)
- [ ] Repository with structure
- [ ] plugin.json configured
- [ ] PromptForge Skill (browse, load, search)
- [ ] 3 prompts migrated (CLEAR ≥9.0)
- [ ] Documentation (template, standards, enhancement)

### Week 2 (Days 8-14)
- [ ] Prompt Enhancer + 5 edge cases
- [ ] Prompt Researcher + 5 edge cases
- [ ] 3 custom commands
- [ ] Full integration tested
- [ ] Demo ready

---

## 🤖 AI Engineer - Quick Tasks

**Day 1-2:** Repository + plugin.json + Skill structure
**Day 3-4:** Test with 3 prompts + search
**Day 5-7:** Polish skill, prep for Week 2
**Day 8-10:** Prompt Enhancer + edge cases
**Day 11-12:** Prompt Researcher + edge cases
**Day 13:** Custom commands
**Day 14:** Integration + demo

**Key Outputs:**
- Working plugin that installs locally
- Auto-activating skill
- 2 subagents with 10 edge cases
- 3 commands
- Zero critical bugs

---

## ✍️ Prompt Engineer - Quick Tasks

**Day 1-2:** Template + Quality Standards + Enhancement Templates
**Day 3:** Migrate interview-analysis (CLEAR ≥9.0)
**Day 4:** Migrate feature-prioritization + feedback-synthesis (CLEAR ≥9.0 each)
**Day 5-7:** Test workflows, write examples
**Day 8-10:** Enhancement testing + template refinement
**Day 11-12:** Search testing + validation
**Day 13:** User workflows + command documentation
**Day 14:** Final docs + demo prep

**Key Outputs:**
- 3 prompts migrated (all CLEAR ≥9.0)
- Complete documentation
- Enhancement templates (20+ patterns)
- Quality validation

---

## 📞 Quick Contacts

**Daily Standup:** [TIME] (15 min)
**Mid-Sprint Review:** Day 7 (1 hour)
**Sprint Demo & Retro:** Day 14 (2 hours)

**Escalation:**
1. Try independently (30 min)
2. Ask teammate (30 min)
3. Research docs (30 min)
4. Escalate to Product Lead

---

## 🔗 Key Resources

**Must Read:**
- Product Plan v2.0: `PROMPTFORGE_PRODUCT_PLAN_V2.md`
- Team Onboarding: `PROMPTFORGE_TEAM_ONBOARDING.md`
- Day-by-Day Tasks: `PROMPTFORGE_SPRINT0_TASKS.md`

**External:**
- Claude Code Plugin Docs: https://code.claude.com/docs/en/plugin-marketplaces
- Marketplace Guide: https://code.claude.com/docs/en/plugin-marketplaces

---

## ✅ Success Criteria (Sprint 0)

By Day 14, you should have:

- [ ] Plugin installs successfully (>95% success rate)
- [ ] Skill auto-activates when user needs PM help
- [ ] Enhancement improves CLEAR scores by +0.3 avg
- [ ] Search returns relevant results (>80% accuracy)
- [ ] All 10 edge cases handled gracefully
- [ ] 3 prompts migrated and scored (CLEAR ≥9.0)
- [ ] Zero critical bugs
- [ ] Complete documentation
- [ ] Successful demo

**If all checked → Sprint 0 SUCCESS! ✅**

---

## 🚨 Common Issues

**Plugin won't install?**
→ Check plugin.json syntax, verify paths

**Skill doesn't activate?**
→ Check activation criteria, test with explicit triggers

**Subagent fails?**
→ Verify agent registered in plugin.json, check syntax

**Enhancement doesn't improve score?**
→ Review transformations, check if already optimized

**Performance slow?**
→ Add caching, optimize file I/O, chunk large operations

---

## 📊 Content Library (70 Prompts)

**Sprint 0:** 3 prompts (interview-analysis, feature-prioritization, feedback-synthesis)

**Sprint 1 (P0):** 20 prompts - CLEAR ≥9.0
- Strategy: 3
- Research: 5
- Execution: 6
- Analysis: 5
- Communication: 3

**Sprint 3 (P1):** 50 prompts - CLEAR ≥8.5
- Strategy: 7
- Research: 10
- Execution: 9
- Analysis: 7
- Communication: 7
- Special Workflows: 8

**Total:** 70 prompts

---

## 💡 Pro Tips

**For AI Engineer:**
- Start simple, add complexity gradually
- Test early, test often
- Edge cases matter more than features
- Document as you build

**For Prompt Engineer:**
- Examples are key to high CLEAR scores
- Be specific (vague = low Clarity score)
- Use frameworks (RICE, JTBD, OKRs, etc.)
- Test prompts yourself before scoring

**For Both:**
- Commit daily (minimum)
- Communicate blockers immediately
- Review each other's work
- Keep user experience in mind

---

**Print this card or keep it open while working!**

**Last Updated:** November 6, 2025
