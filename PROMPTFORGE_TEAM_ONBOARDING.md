# PromptForge: Team Onboarding Guide

**Purpose:** Get both engineers up to speed quickly on PromptForge architecture, responsibilities, and best practices.

**Read time:** 30 minutes

**Target audience:** New team members joining Sprint 0

---

## 🎯 What is PromptForge?

### The Problem We're Solving

**Product Managers waste 5-10 hours per week:**
- Crafting prompts from scratch for common tasks
- Tweaking prompts that "almost work but not quite"
- Losing good prompts in Slack/Notion/emails
- Copying static prompts from $49 Gumroad PDFs that don't fit their context

### Our Solution

**PromptForge = World-class PM prompt library + AI-powered customization**

- 70 pre-made prompts (CLEAR score 8.5+)
- Native Claude Code plugin (one-command install)
- AI enhancement adapts prompts to your industry, stage, team
- Free and open source

### The Vision

**Monday morning scenario:**

**Without PromptForge:**
- PM has 47 Slack messages about user feedback
- Spends 2 hours manually synthesizing
- Creates mediocre summary
- Stakeholders confused

**With PromptForge:**
- PM starts working in Claude Code
- Claude auto-suggests: "Use Feedback Synthesis prompt (9.0 CLEAR)"
- Prompt enhanced for their B2B SaaS context
- 5 minutes → prioritized insights with themes
- **Saved: 1h 55min**

**That's the experience we're building.**

---

## 👥 Team Structure

### You're Part of a 2-Person Team

**AI Engineer (Infrastructure & Intelligence)**
- Builds plugin architecture
- Creates 2 specialized subagents
- Implements 3 custom commands
- Handles edge cases and error handling
- Ensures technical excellence

**Prompt Engineer (Content & Quality)**
- Writes all 70 prompts
- Scores prompts using CLEAR framework
- Designs enhancement templates
- Ensures content excellence
- Documents quality standards

**Collaboration is critical.** You'll pair on:
- Enhancement feature design
- Quality validation
- User testing
- Documentation

---

## 🏗️ Architecture Overview

### The Big Picture

```
User in Claude Code
    ↓
PromptForge Plugin (installed via /plugin install)
    ↓
PromptForge Skill (auto-activates when user needs PM help)
    ↓
[Option 1] Browse → Load Prompt → Use
[Option 2] Browse → Enhance (Subagent) → Use Enhanced Version
[Option 3] Search (Subagent) → Find → Load → Enhance → Use
```

### Component Breakdown

#### 1. Plugin (`plugin.json`)
- **What:** Metadata telling Claude Code what PromptForge contains
- **Who builds:** AI Engineer
- **Key info:** Name, version, components (skills, agents, commands)
- **Marketplace:** Submitted to official Claude Code marketplace

#### 2. Skill (`skills/promptforge/SKILL.md`)
- **What:** Main intelligence, auto-activates when user needs PM prompts
- **Who builds:** AI Engineer (with Prompt Engineer input)
- **Capabilities:**
  - Detect when user needs PM help
  - Browse prompt library
  - Load specific prompts
  - Delegate to subagents (enhancement, search)
  - Show CLEAR scores

#### 3. Subagent: Prompt Enhancer (`agents/prompt-enhancer.md`)
- **What:** Specialist that customizes prompts for user's context
- **Who builds:** AI Engineer (with Prompt Engineer templates)
- **Capabilities:**
  - Gather context (industry, stage, detail level, etc.)
  - Transform prompt based on context
  - Calculate CLEAR scores (before/after)
  - Handle edge cases gracefully
  - Target: +0.3 to +0.5 score improvement

#### 4. Subagent: Prompt Researcher (`agents/prompt-researcher.md`)
- **What:** Specialist that searches and recommends prompts
- **Who builds:** AI Engineer
- **Capabilities:**
  - Semantic search across 70 prompts
  - Compare similar prompts
  - Recommend workflows (multi-prompt sequences)
  - Explain quality differences
  - Handle ambiguous queries

#### 5. Custom Commands
- **What:** Explicit slash commands for power users
- **Who builds:** AI Engineer
- **Commands:**
  - `/prompt-browse` - Interactive library exploration
  - `/prompt-enhance` - Trigger enhancement explicitly
  - `/prompt-score` - Score any prompt using CLEAR

#### 6. Prompts (70 files in `prompts/product-management/`)
- **What:** The actual prompt content
- **Who builds:** Prompt Engineer
- **Structure:**
  - YAML frontmatter (metadata)
  - Markdown content (the prompt itself)
  - Examples, frameworks, tips

---

## 📐 CLEAR Framework (Quality Standard)

### The Non-Negotiable Quality Bar

**Every prompt must score 8.5+ on CLEAR framework.**

### The 5 Dimensions (Scored 0-10 each)

#### C - Clarity (25% weight)
**What:** Instructions are unambiguous and specific

**10/10 Example:**
> "Analyze exactly 5 competitors, listing: product name, pricing model (e.g., $99/mo subscription), 3-5 key features per competitor, and market position (leader/challenger/niche)"

**3/10 Example:**
> "Look at some competitors and describe them"

**Red flags:** Vague adjectives ("good", "appropriate"), unclear scope ("some", "several")

---

#### L - Length & Specificity (20% weight)
**What:** Appropriate detail level for task complexity

**Guidelines:**
- Simple task: 50-150 words
- Medium task: 150-400 words
- Complex task: 400-800 words
- Never exceed 800 words (break into multi-step)

**10/10 Example:**
```
Generate 3 user personas:
- Demographics: age range, role, company size, industry
- Goals: 3 primary objectives they want to achieve
- Pain points: 3 current frustrations with existing solutions
- Behaviors: how they currently solve the problem
- Success metrics: what "success" looks like to them
```

**3/10 Example:**
> "Create some personas"

---

#### E - Examples (20% weight)
**What:** Concrete examples illustrate desired output

**10/10 Example:**
```
Example Output for Feature: "Dark Mode Toggle"

User Story:
As a [mobile app user who works late nights]
I want [to enable dark mode with one tap]
So that [I can reduce eye strain and save battery]

Acceptance Criteria:
- Given user is on Settings screen
  When they tap "Dark Mode" toggle
  Then entire UI switches to dark theme within 200ms
- Given dark mode is enabled
  When app restarts
  Then dark mode persists (saved to local storage)
```

**3/10 Example:**
> "Here's a user story example: As a user, I want dark mode"

**Best practices:** Show format explicitly, use realistic content, cover 2-3 scenarios

---

#### A - Audience (15% weight)
**What:** Target audience and context explicit

**10/10 Example:**
```
Audience: B2B SaaS Product Managers at growth-stage companies (50-200 employees)
Context: You're prioritizing features for Q2 roadmap with limited engineering capacity
Assumptions:
- You have user research data available
- Engineering team uses 2-week sprints
- You're familiar with RICE scoring
```

**4/10 Example:** No audience mentioned, assumes PM knowledge

**Requirements:** State target role, provide context, list assumptions, define scope

---

#### R - Result (20% weight)
**What:** Desired output format and success criteria defined

**10/10 Example:**
```
Deliverable:
- Format: Markdown document
- Length: 800-1200 words
- Structure:
  1. Executive Summary (2-3 sentences)
  2. Top 5 Features (200 words each with RICE scores)
  3. Recommendation (1 paragraph)
  4. Next Steps (bulleted action items)
- Success Criteria:
  - All scores justified with data
  - Clear winner identified
  - Stakeholder-ready (no jargon)
```

**3/10 Example:**
> "Give me a prioritization report"

**Checklist:** Output format, length, structure, success criteria, constraints

---

### CLEAR Score Calculation

```
CLEAR Score = (C × 0.25) + (L × 0.20) + (E × 0.20) + (A × 0.15) + (R × 0.20)
```

**Example:**
```
Clarity:    9.0 × 0.25 = 2.25
Length:     8.5 × 0.20 = 1.70
Examples:   9.0 × 0.20 = 1.80
Audience:   8.0 × 0.15 = 1.20
Result:     9.0 × 0.20 = 1.80
──────────────────────────────
Total:      8.75/10 ⭐ EXCELLENT
```

### Quality Thresholds

```
🏆 9.0-10.0 = WORLD-CLASS (Publish immediately)
⭐ 8.5-8.9  = EXCELLENT (Minor polish, then publish)
✅ 8.0-8.4  = GOOD (Needs iteration)
⚠️ 7.0-7.9  = ACCEPTABLE (Significant rework)
❌ <7.0     = REJECT (Start over)
```

**PromptForge minimum: 8.5 for inclusion**

---

## 🎨 Enhancement Dimensions

### The 5 Ways to Customize Prompts

When a user wants to enhance a prompt, they can customize along these dimensions:

#### 1. Industry
- B2B SaaS, E-commerce, Consumer Apps, Enterprise Software
- Healthcare, FinTech, Marketplace

**What changes:**
- Metrics (ARR for SaaS, GMV for marketplace, patient outcomes for healthcare)
- Examples become industry-specific
- Terminology matches domain
- Compliance considerations added (HIPAA for healthcare, SOX for finance)

**Example:**
- Generic: "Define success metrics"
- B2B SaaS: "Define success metrics (ARR, MRR, churn rate, expansion revenue)"

---

#### 2. Company Stage
- Early-stage startup (Pre-seed to Seed)
- Growth stage (Series A-B)
- Late stage (Series C+)
- Enterprise/Public

**What changes:**
- Resource constraints (startup = lean, enterprise = robust)
- Process maturity (startup = informal, enterprise = formal)
- Stakeholder complexity (startup = 2-3 people, enterprise = committees)
- Risk tolerance (startup = move fast, enterprise = careful)

**Example:**
- Startup: "Create 1-page PRD, share with co-founder, ship in 2 weeks"
- Enterprise: "Create comprehensive PRD, present to product council, get legal/security/compliance sign-off, plan 3-month rollout"

---

#### 3. Detail Level
- Quick (15 min) - High-level, essentials only
- Standard (30-45 min) - Balanced, recommended
- Comprehensive (60+ min) - Deep-dive, thorough

**What changes:**
- Number of steps (Quick: 3-5, Comprehensive: 10-15)
- Number of examples (Quick: 1, Comprehensive: 3-5)
- Depth of analysis (Quick: surface-level, Comprehensive: edge cases)
- Supporting frameworks (Quick: 1 framework, Comprehensive: 3-4 frameworks)

---

#### 4. Output Format
- Executive Brief (1 page)
- Standard Report (3-5 pages)
- Detailed Analysis (10+ pages)
- Presentation (Slides outline)
- Dashboard (Metrics table)

**What changes:**
- Structure and sections
- Length constraints
- Visual elements
- Audience formality

---

#### 5. Team Context
- Solo PM
- PM with designer
- PM with data analyst
- Full product trio (PM/Eng/Design)
- Cross-functional team

**What changes:**
- Collaboration steps
- Delegation points
- Stakeholder involvement
- Review cycles

---

## 🎓 Role-Specific Deep Dive

---

## 🤖 AI Engineer: Your Responsibilities

### What You're Building (Sprint 0)

**Week 1: Foundation**
1. Project repository and structure
2. plugin.json configuration
3. PromptForge Skill (auto-activation, browse, load, search)
4. Category READMEs
5. CLEAR scoring automation

**Week 2: Intelligence**
1. Prompt Enhancer subagent + 5 edge cases
2. Prompt Researcher subagent + 5 edge cases
3. 3 custom commands
4. Integration testing

### Technical Stack

- **Language:** Markdown (for skill/agent definitions)
- **Config:** JSON (plugin.json)
- **Tools:** Git, Claude Code, text editor
- **Testing:** Manual testing via Claude Code interface
- **Optional:** Node.js/Python for validation scripts

### Key Technical Decisions

#### Decision 1: Skills vs. Slash Commands
**Choice:** Skills-first, commands optional

**Why:** Skills auto-activate (better UX), commands for power users

**Implementation:** Skill detects user intent, delegates to subagents or commands

---

#### Decision 2: Subagent Architecture
**Choice:** Separate subagents for enhancement and search

**Why:**
- Context isolation (don't pollute main conversation)
- Single responsibility (focused, simpler logic)
- Resumable (can continue later)
- Proper tool access (only what each needs)

**Implementation:** Main Skill delegates via Claude's subagent API

---

#### Decision 3: Pure Markdown for Prompts
**Choice:** YAML frontmatter + Markdown content, no JSON index

**Why:**
- Git-friendly diffs
- Single source of truth
- No sync issues
- Human-readable

**Implementation:** Parse YAML in skill, search via file reads

---

### Edge Cases You Must Handle

#### Prompt Enhancer Edge Cases

**1. Enhancement Makes Score Worse**
```
Problem: User requests customization that degrades quality
Detection: enhanced_score < original_score
Response: Explain why, recommend original, offer alternatives
Fallback: Always return original as option
```

**2. Impossible Combination**
```
Problem: "Comprehensive detail in 1-page brief"
Detection: Validate dimension compatibility before enhancement
Response: Explain conflict, suggest compatible combinations
Fallback: Offer closest possible match
```

**3. User Abandons Mid-Enhancement**
```
Problem: User stops responding during Q&A
Detection: 3 unanswered questions
Response: Offer pause/resume, default option, or original
Fallback: Save session state, allow /prompt-enhance --resume
```

**4. Already Industry-Specific**
```
Problem: User wants "B2B SaaS version" of already-B2B-SaaS prompt
Detection: Check frontmatter industry: field
Response: Explain already optimized, offer other dimensions
Fallback: Offer stage, detail, or team customization instead
```

**5. Enhancement Timeout**
```
Problem: Taking >2 minutes, risk of API timeout
Detection: Track elapsed time
Response: Chunk work, show progress, save partial results
Fallback: Return partial enhancement, allow continuation
```

#### Prompt Researcher Edge Cases

**1. No Results Found**
```
Problem: Search for "cryptocurrency wallet design" returns nothing
Detection: 0 results from search
Response: Suggest related prompts, broader search, or enhancement
Fallback: Always offer "create GitHub issue to request this"
```

**2. Too Many Results**
```
Problem: Search for "planning" returns 18 prompts
Detection: >10 results
Response: Group by category, ask for clarification
Fallback: Show top 5 by relevance + category menu
```

**3. User Doesn't Know What They Need**
```
Problem: "I have user feedback but not sure what to do"
Detection: Vague request without clear intent
Response: Interactive Q&A to determine need
Fallback: Show common workflows for that scenario
```

**4. Unrelated Comparison**
```
Problem: "Compare PRD Writing vs Email Campaign"
Detection: Prompts in different categories, different purposes
Response: Clarify intent, suggest logical comparisons
Fallback: Offer workflow that uses both
```

**5. Task Better Suited to Enhancer**
```
Problem: "Find prioritization prompt for B2B SaaS"
Detection: Search query includes enhancement context
Response: Find prompt, offer to enhance for context
Fallback: Hand off to enhancer subagent
```

### Your Success Criteria

By end of Sprint 0, you should have:

- [ ] Working plugin that installs locally
- [ ] Skill that auto-activates when user needs PM help
- [ ] Enhancement that improves CLEAR scores by +0.3 average
- [ ] Search that returns relevant results >80% of time
- [ ] All 10 edge cases handled gracefully
- [ ] Zero critical bugs
- [ ] Clean, documented code

### Resources for You

**Must Read:**
- Claude Code Plugin Docs: https://code.claude.com/docs/en/plugin-marketplaces
- Product Plan v2.0: PROMPTFORGE_PRODUCT_PLAN_V2.md
- This onboarding guide

**Reference During Development:**
- Enhancement Templates (from Prompt Engineer)
- CLEAR Framework scoring rubric
- Edge case handling guide (above)

**Questions?** Ask Prompt Engineer or Product Lead

---

## ✍️ Prompt Engineer: Your Responsibilities

### What You're Building (Sprint 0-3)

**Sprint 0 (Week 1-2):**
1. Design prompt template
2. Write quality standards documentation
3. Create enhancement templates
4. Migrate 3 existing prompts
5. Score prompts using CLEAR framework

**Sprint 1 (Week 3-4):**
1. Create 20 P0 prompts (CLEAR 9.0+)
2. Test enhancement on each prompt
3. Iterate until quality bar met

**Sprint 2 (Week 5):**
1. Refine enhancement based on P0 testing
2. Document enhancement best practices
3. Create enhancement examples

**Sprint 3 (Week 6-7):**
1. Create 50 P1 prompts (CLEAR 8.5+)
2. Complete library to 70 total prompts
3. Final quality review

### Your Toolkit

**Tools:**
- Text editor (VS Code, Sublime, etc.)
- CLEAR scoring spreadsheet (create one)
- Git for version control
- Claude (to test prompts and get help)

**Inputs:**
- Product Plan v2.0 (list of 70 prompts to create)
- CLEAR framework (your quality standard)
- Existing 3 prompts (reference examples)
- PM research (understand user needs)

**Outputs:**
- 70 prompt files (.md with YAML frontmatter)
- QUALITY_STANDARDS.md
- ENHANCEMENT_GUIDE.md
- ENHANCEMENT_TEMPLATES.md
- PROMPT_TEMPLATE.md

### Prompt Template Structure

**Every prompt follows this structure:**

```markdown
---
name: Feature Prioritization
category: execution
subcategory: roadmap
description: Prioritize features using RICE/ICE scoring frameworks
clear_score: 9.2
industry: all
company_stage: all
time_estimate: 30-45 min
difficulty: intermediate
frameworks: [RICE, ICE, Priority Matrix]
tags: [prioritization, roadmap, strategy, scoring]
related_prompts: [roadmap-planning, sprint-planning]
version: 1.0
last_updated: 2025-11-06
---

# Feature Prioritization Using RICE/ICE

**Purpose:** Systematically prioritize features to maximize value and impact

**Best For:** PMs with 5-20 feature ideas, limited engineering capacity

**Time Required:** 30-45 minutes

---

## Context & Audience

**Target User:** Product Managers at growth-stage companies

**When to Use:** Quarterly planning, roadmap reviews, backlog grooming

**Prerequisites:**
- List of feature ideas (minimum 5)
- Basic understanding of your user base
- Rough estimates of engineering effort

---

## Instructions

### Step 1: List All Features

[Clear, specific instructions]

**What to do:**
- List each feature idea (one line each)
- Include brief description (1 sentence max)
- Number each feature

**What to avoid:**
- ❌ Grouping similar features (keep separate for now)
- ❌ Editing or judging ideas (just list)

### Step 2: Score Using RICE

[Continue with detailed steps...]

---

## Expected Output

**Format:** Markdown table with scores

**Structure:**
1. Feature name and description
2. RICE scores (Reach, Impact, Confidence, Effort)
3. Final score (R × I × C / E)
4. Rank order
5. Recommendation (top 3-5 to prioritize)

**Length:** 1-2 pages

**Success Criteria:**
- ✅ All features scored objectively
- ✅ Scores justified with data/reasoning
- ✅ Clear top 5 identified
- ✅ Effort estimates realistic

---

## Example Output

[Show realistic, detailed example]

---

## Frameworks Reference

**RICE Framework:**
- Reach: How many users affected per time period
- Impact: How much it moves the needle (0.25 - 3.0 scale)
- Confidence: How sure are you (0-100%)
- Effort: Engineering person-months

[More details...]

---

## Tips & Best Practices

💡 **Pro Tips:**
- Involve engineering in Effort estimates
- Use data for Reach (not guesses)
- Don't inflate Impact scores (be honest)

⚠️ **Common Pitfalls:**
- Effort in hours (use person-months for consistency)
- Ignoring Confidence (leads to risky bets)

🔗 **Related Prompts:**
- Roadmap Planning: Once prioritized, plan releases
- Sprint Planning: Break top features into sprints

---

## Customization Options

This prompt can be enhanced for:
- **Industry:** B2B SaaS (add ARR impact), E-commerce (add GMV)
- **Company Stage:** Startup (faster scoring), Enterprise (governance)
- **Detail Level:** Quick (top 5 only), Comprehensive (all features + sensitivity analysis)
- **Output Format:** Executive brief, detailed report, slide deck

💬 **Want a customized version?** Ask Claude to enhance this prompt!
```

### CLEAR Scoring Process

**For each prompt you write:**

1. **Draft the prompt** following template
2. **Self-score** on each CLEAR dimension (0-10)
3. **Calculate total** using weights
4. **If <8.5:** Identify weak dimension(s) and iterate
5. **Repeat** until ≥8.5
6. **Peer review** with AI Engineer (optional but recommended)
7. **Document** scoring rationale

**Scoring Worksheet:**

```
Prompt Name: _______________________

Clarity (25%):     ___ / 10
  - Are instructions specific and unambiguous?
  - Any vague language?
  - Scope clear?

Length (20%):      ___ / 10
  - Appropriate detail for complexity?
  - Too verbose or too terse?
  - Follows length guidelines?

Examples (20%):    ___ / 10
  - Concrete examples present?
  - Show desired output format?
  - Realistic content (not Lorem Ipsum)?
  - Cover multiple scenarios?

Audience (15%):    ___ / 10
  - Target user explicit?
  - Context and prerequisites stated?
  - Assumptions documented?

Result (20%):      ___ / 10
  - Output format defined?
  - Success criteria clear?
  - Structure specified?
  - Length expectations set?

TOTAL: ___ / 10

Status: □ Draft  □ Review  □ Approved  □ Published
```

### Enhancement Template Creation

**You'll create transformation patterns for each dimension:**

**Example: B2B SaaS Industry Enhancement**

```
When industry = B2B SaaS:

TRANSFORM:
  Metrics:
    - Replace "user growth" → "ARR growth"
    - Add: MRR, churn rate, expansion revenue, CAC, LTV

  Examples:
    - Use SaaS product names (Slack, Notion, Figma)
    - B2B buying scenarios (demos, trials, contracts)

  Terminology:
    - "customers" → "accounts" or "logos"
    - "purchase" → "contract" or "subscription"

  Add Sections:
    - Stakeholder mapping (multiple decision-makers)
    - Sales cycle considerations (longer for B2B)

  Compliance:
    - Mention SOC 2, GDPR if relevant
```

**Create 20-30 of these patterns** across all dimensions.

### Your Success Criteria

**By end of Sprint 0:**
- [ ] 3 prompts migrated and scored (all ≥9.0)
- [ ] Prompt template documented
- [ ] Quality standards documented
- [ ] Enhancement templates created (20+ patterns)
- [ ] Enhancement guide drafted

**By end of Sprint 1:**
- [ ] 20 P0 prompts created (all ≥9.0 or ≥8.8 where targeted)
- [ ] Average CLEAR score ≥9.0
- [ ] All prompts tested with enhancement
- [ ] Beta tester validation positive

**By end of Sprint 3:**
- [ ] All 70 prompts created
- [ ] Average CLEAR score ≥8.7
- [ ] All prompts follow template exactly
- [ ] Library complete and ready to launch

### Resources for You

**Must Read:**
- Product Plan v2.0: PROMPTFORGE_PRODUCT_PLAN_V2.md
- CLEAR Framework (this document, review deeply)
- This onboarding guide

**Reference During Development:**
- Existing 3 prompts (quality examples)
- PM frameworks (RICE, JTBD, OKRs, etc.)
- Gumroad competitor prompts (see what to improve upon)

**Questions?** Ask AI Engineer or Product Lead

---

## 🤝 Collaboration Points

### Where Both Engineers Work Together

#### 1. Enhancement Feature Design (Sprint 0, Days 8-10)

**Prompt Engineer provides:**
- Enhancement templates for all dimensions
- Examples of good transformations
- Quality criteria for enhanced versions

**AI Engineer implements:**
- Context gathering workflow
- Transformation logic using templates
- CLEAR score calculation

**Together you:**
- Test enhanced prompts for quality
- Iterate on transformation patterns
- Validate score improvements

---

#### 2. Quality Validation (Throughout)

**Prompt Engineer creates:**
- Prompt content

**AI Engineer validates:**
- Prompt loads correctly in skill
- Metadata parsed properly
- Enhancement works on this prompt

**Together you:**
- Review CLEAR scores
- Test user workflows
- Identify improvements

---

#### 3. User Testing (Sprint 0 Day 14, Sprint 1 Day 14)

**Both engineers:**
- Run through user scenarios
- Identify UX issues
- Test edge cases
- Gather feedback
- Document findings
- Prioritize fixes

---

## 📞 Communication & Rituals

### Daily Standup (15 min, same time each day)

**Format:**
1. What I completed yesterday
2. What I'm doing today
3. Any blockers

**Keep it brief.** Detailed discussions happen after.

---

### Mid-Sprint Check-in (Day 7, 1 hour)

**Agenda:**
1. Demo: Show what works so far
2. Review: Are we on track for Sprint 0 goals?
3. Adjust: Any changes needed for Week 2?
4. Blockers: Anything preventing progress?

---

### Sprint Demo & Retro (Day 14, 2 hours)

**Demo (1 hour):**
- Show all deliverables working
- Walk through user scenarios
- Highlight edge case handling
- Demonstrate quality (CLEAR scores)

**Retro (1 hour):**
- What went well?
- What could be improved?
- Action items for Sprint 1

---

## 🎯 Working Agreements

### Code Review
- **All code/content reviewed before merging**
- AI Engineer reviews Prompt Engineer's prompts (quality check)
- Prompt Engineer reviews AI Engineer's skill/agent logic (UX check)
- Feedback within 24 hours

### Git Workflow
- Commit often (daily minimum)
- Clear commit messages
- Pull before push
- No force pushes to main

### Documentation
- Document as you build (not after)
- Update README.md as features complete
- Keep CHANGELOG.md current
- All decisions documented in Git

### Communication
- Slack/Discord for quick questions (<5 min)
- Video call for complex discussions (>15 min)
- Async by default, sync when needed
- Respond within 4 hours during work hours

---

## ✅ Onboarding Complete Checklist

**Both Engineers:**
- [ ] Read Product Plan v2.0 completely
- [ ] Understand the vision and why we're building this
- [ ] Know the competitive landscape (vs Gumroad)
- [ ] Understand CLEAR framework
- [ ] Understand enhancement dimensions
- [ ] Know your Sprint 0 responsibilities
- [ ] Development environment ready
- [ ] Access to repository
- [ ] Communication channel set up
- [ ] Daily standup time scheduled
- [ ] Questions answered

**AI Engineer Specific:**
- [ ] Read Claude Code plugin documentation
- [ ] Understand subagent architecture
- [ ] Reviewed all 10 edge cases
- [ ] Know your Day 1-2 tasks

**Prompt Engineer Specific:**
- [ ] Studied CLEAR framework deeply
- [ ] Reviewed prompt template structure
- [ ] Located 3 existing prompts to migrate
- [ ] Know your Day 1-2 tasks

---

**All boxes checked?**

✅ **YOU'RE READY FOR SPRINT 0!**

**Welcome to the team. Let's build something amazing.** 🚀

---

**Document Status:** v1.0
**Last Updated:** November 6, 2025
**Next Update:** After Sprint 0 (based on learnings)
**Owner:** Product Lead
