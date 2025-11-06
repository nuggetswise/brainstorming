# PromptForge: Product Planning Session
**Strategic Planning Meeting**

**Date:** November 6, 2025
**Duration:** 2.5 hours
**Attendees:**
- **Engineering Lead** (Architecture & Implementation)
- **Prompt Engineer** (Quality & Frameworks)
- **Claude Code Expert** (Platform Integration)

---

## 🎯 Meeting Objectives

1. ✅ Align on product vision: Pre-made prompt library (NOT prompt management system)
2. ✅ Define quality framework and standards
3. ✅ Design technical architecture using Claude Code best practices
4. ✅ Establish content taxonomy and creation methodology
5. ✅ Plan interactive enhancement feature (our competitive moat)
6. ✅ Create detailed sprint plan with milestones

---

## 📋 Executive Summary

### The Big Pivot

**Previous Direction** ❌: Prompt Management System
- Users save their own prompts
- Version control for user prompts
- JSON indices, complex state management
- Similar to: Git for prompts

**New Direction** ✅: Pre-Made Prompt Library
- We provide 50-100 BEST prompts
- Users browse and use our curated collection
- No user-generated content in v1
- Similar to: Gumroad product bundle

### Why This Is Better

| Aspect | Old Approach | New Approach |
|--------|-------------|--------------|
| **Value Prop** | "Manage your prompts" | "Use our world-class prompts" |
| **Barrier to Entry** | High (must create prompts) | Zero (use immediately) |
| **Quality Control** | User's responsibility | Our guarantee (CLEAR 8.5+) |
| **Time to Value** | Days/weeks | Seconds |
| **Competitive Edge** | Incremental vs tools | 10× better than Gumroad PDFs |

### Decision

**APPROVED**: Pivot to Pre-Made Prompt Library model

---

## 🏗️ Technical Architecture

### Claude Code Expert's Assessment

#### Current State Analysis

**What Exists:**
- ✅ PM research suite with 3 excellent prompts
- ✅ Skills architecture documentation
- ✅ CLEAR quality framework defined
- ✅ Research analyst agent example
- ❌ Implementation focused on wrong model (prompt management)

**What We Need:**
- ✅ Browse prompts by category
- ✅ Load and use prompts instantly
- ✅ Interactive enhancement (customize prompts)
- ✅ Quality scoring display
- ✅ Semantic search across library

#### Architecture Decision: Skills-First + Pure Markdown

**Recommended Structure:**

```
promptforge/
├── .claude/
│   ├── skills/
│   │   └── promptforge/
│   │       └── SKILL.md                    # Core intelligence
│   └── claude.md                           # Project context
│
├── prompts/
│   ├── product-management/
│   │   ├── 01-strategy/
│   │   │   ├── product-vision.md
│   │   │   ├── roadmap-planning.md
│   │   │   ├── okr-setting.md
│   │   │   ├── market-sizing.md
│   │   │   └── business-case.md
│   │   │
│   │   ├── 02-research/
│   │   │   ├── user-interview-guide.md
│   │   │   ├── interview-analysis.md
│   │   │   ├── survey-design.md
│   │   │   ├── competitive-analysis.md
│   │   │   ├── persona-development.md
│   │   │   └── customer-journey-map.md
│   │   │
│   │   ├── 03-execution/
│   │   │   ├── prd-writing.md
│   │   │   ├── feature-prioritization.md
│   │   │   ├── user-story-writing.md
│   │   │   ├── sprint-planning.md
│   │   │   ├── backlog-grooming.md
│   │   │   └── launch-planning.md
│   │   │
│   │   ├── 04-analysis/
│   │   │   ├── feedback-synthesis.md
│   │   │   ├── data-analysis.md
│   │   │   ├── ab-test-design.md
│   │   │   ├── funnel-analysis.md
│   │   │   └── metrics-definition.md
│   │   │
│   │   ├── 05-communication/
│   │   │   ├── stakeholder-update.md
│   │   │   ├── executive-summary.md
│   │   │   ├── product-announcement.md
│   │   │   ├── meeting-facilitation.md
│   │   │   └── decision-documentation.md
│   │   │
│   │   └── README.md                       # Category overview
│   │
│   └── README.md                            # Library homepage
│
├── docs/
│   ├── QUALITY_STANDARDS.md                # CLEAR framework explained
│   ├── ENHANCEMENT_GUIDE.md                # How to customize prompts
│   ├── CONTRIBUTION_GUIDE.md               # For community (future)
│   └── EXAMPLES.md                         # Real usage examples
│
├── README.md                                # Project homepage
└── LICENSE                                  # MIT
```

#### Why This Architecture Wins

**1. Skills > Slash Commands**

```yaml
# OLD (Slash Commands - Manual)
User: /prompt-browse
User: /prompt-load feature-prioritization
User: /prompt-enhance

# NEW (Skills - Automatic)
User: "I need to prioritize features"
Claude: [Automatically invokes PromptForge skill]
        "I have a world-class feature prioritization prompt!
         Scored 9.2/10 on CLEAR. Want to use it or customize?"
```

**Why:** Seamless UX, no commands to remember, proactive help

**2. Pure Markdown > JSON Indices**

```markdown
---
name: Feature Prioritization
category: Execution
clear_score: 9.2
industry: all
time_estimate: 30-45 min
difficulty: medium
frameworks: [RICE, ICE, Priority Matrix]
tags: [prioritization, roadmap, strategy]
related: [roadmap-planning, sprint-planning]
---

# Feature Prioritization Using RICE/ICE

[Prompt content following CLEAR framework]
```

**Why:** Git-friendly diffs, single source of truth, no sync issues

**3. Category-Based File Organization**

```
prompts/product-management/03-execution/feature-prioritization.md
```

**Why:** Discoverable, browsable, logical hierarchy

#### Technical Implementation Details

**SKILL.md Capabilities:**

```markdown
# PromptForge Skill

## When to Activate

Activate when user:
- Asks for help with PM tasks ("I need to write a PRD")
- Mentions prompt-related keywords ("show me prompts")
- Is in promptforge directory
- Requests specific workflow ("feature prioritization")

## What to Do

### 1. Detect Intent
Parse user request to identify:
- Task category (strategy, research, execution, etc.)
- Specificity (general browsing vs specific prompt)
- Customization needs (industry, stage, detail level)

### 2. Browse Mode
When user wants to explore:
- Show category tree
- Display top prompts per category
- Highlight CLEAR scores
- Suggest popular starting points

### 3. Load Mode
When user requests specific prompt:
- Read markdown file
- Display formatted prompt
- Show metadata (CLEAR score, time, difficulty)
- Offer enhancement options

### 4. Enhancement Mode (KEY FEATURE)
When user wants customization:
- Ask clarifying questions (industry, stage, context)
- Generate enhanced version using Claude intelligence
- Score both versions (original vs enhanced)
- Explain improvements
- Offer to save to workspace

### 5. Search Mode
When user searches:
- Semantic search across all prompts
- Match on: name, description, tags, content
- Rank by relevance
- Show top 5 results with excerpts
```

---

## 📐 Prompt Engineering Framework

### Prompt Engineer's Quality Methodology

#### The CLEAR Framework (Enhanced)

**Scoring Matrix (0-10 for each dimension):**

##### C - Clarity (25% weight)
**What:** Instructions are unambiguous and specific

**Scoring Criteria:**
- **9-10**: Every instruction crystal clear, no interpretation needed
- **7-8**: Mostly clear with minor ambiguities
- **5-6**: Some vague language, needs clarification
- **3-4**: Significant ambiguity, unclear expectations
- **0-2**: Confusing, contradictory, or vague

**Examples:**
- ✅ 10/10: "Analyze exactly 5 competitors, listing product name, pricing model, key features (max 5 per competitor), and market position"
- ❌ 5/10: "Look at competitors and describe them"

**Red Flags to Avoid:**
- Vague adjectives: "good", "nice", "better", "appropriate"
- Unclear scope: "some", "several", "a few"
- Missing details: "analyze data" (what data? how?)

##### L - Length & Specificity (20% weight)
**What:** Appropriate detail level for task complexity

**Scoring Criteria:**
- **9-10**: Perfect balance, every detail serves a purpose
- **7-8**: Slightly too verbose or terse, but functional
- **5-6**: Missing key details or excessive fluff
- **3-4**: Significantly under/over-specified
- **0-2**: Way too short (useless) or long (overwhelming)

**Examples:**
- ✅ 10/10:
  ```
  Generate 3 user personas:
  - Demographics: age range, role, company size, industry
  - Goals: 3 primary objectives they want to achieve
  - Pain points: 3 current frustrations with existing solutions
  - Behaviors: how they currently solve the problem
  - Success metrics: what "success" looks like to them
  ```
- ❌ 3/10: "Create some personas"

**Guidelines:**
- Simple task: 50-150 words
- Medium task: 150-400 words
- Complex task: 400-800 words
- Don't exceed 800 words (break into multi-step instead)

##### E - Examples (20% weight)
**What:** Concrete examples illustrate desired output

**Scoring Criteria:**
- **9-10**: Multiple examples showing ideal output, edge cases, formats
- **7-8**: Good examples but missing edge cases or variety
- **5-6**: Generic examples, not enough detail
- **3-4**: Examples present but not helpful
- **0-2**: No examples provided

**Examples:**
- ✅ 10/10:
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
- ❌ 3/10: "Here's a user story example: As a user, I want dark mode"

**Best Practices:**
- Show format/structure explicitly
- Include realistic content (not Lorem Ipsum)
- Cover 2-3 scenarios if possible
- Use markdown formatting for clarity

##### A - Audience (15% weight)
**What:** Target audience and context explicit

**Scoring Criteria:**
- **9-10**: Audience, context, assumptions all clearly stated
- **7-8**: Audience implied, mostly clear
- **5-6**: Some context missing
- **3-4**: Unclear who this is for
- **0-2**: No audience consideration

**Examples:**
- ✅ 10/10:
  ```
  Audience: B2B SaaS Product Managers at growth-stage companies (50-200 employees)
  Context: You're prioritizing features for Q2 roadmap with limited engineering capacity
  Assumptions:
  - You have user research data available
  - Engineering team uses 2-week sprints
  - You're familiar with RICE scoring
  ```
- ❌ 4/10: No audience mentioned, assumes PM knowledge

**Requirements:**
- State target role/persona
- Provide relevant context
- List key assumptions
- Define scope boundaries

##### R - Result (20% weight)
**What:** Desired output format and success criteria defined

**Scoring Criteria:**
- **9-10**: Output format, length, structure, success metrics all specified
- **7-8**: Good output definition, minor gaps
- **5-6**: Vague output expectations
- **3-4**: Unclear what success looks like
- **0-2**: No result specification

**Examples:**
- ✅ 10/10:
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
- ❌ 3/10: "Give me a prioritization report"

**Checklist:**
- [ ] Output format specified (doc, table, slides, etc.)
- [ ] Length/size constraints defined
- [ ] Structure/sections outlined
- [ ] Success criteria stated
- [ ] Constraints noted (time, scope, audience)

#### Overall CLEAR Score Calculation

```
CLEAR Score = (C × 0.25) + (L × 0.20) + (E × 0.20) + (A × 0.15) + (R × 0.20)
```

**Example:**
```
Clarity: 9.0 × 0.25 = 2.25
Length: 8.5 × 0.20 = 1.70
Examples: 9.0 × 0.20 = 1.80
Audience: 8.0 × 0.15 = 1.20
Result: 9.0 × 0.20 = 1.80
─────────────────────────
CLEAR Score = 8.75/10 ⭐ Excellent
```

#### Quality Thresholds

```
🏆 9.0-10.0 = WORLD-CLASS (Publish immediately)
⭐ 8.5-8.9  = EXCELLENT (Minor polish, then publish)
✅ 8.0-8.4  = GOOD (Needs iteration)
⚠️ 7.0-7.9  = ACCEPTABLE (Significant rework needed)
❌ <7.0     = REJECT (Start over)
```

**PromptForge Standard: Minimum 8.5 CLEAR score**

#### Prompt Template Structure

Every PromptForge prompt follows this structure:

```markdown
---
name: [Descriptive name]
category: [strategy|research|execution|analysis|communication]
subcategory: [specific area]
description: [One-line description]
clear_score: [X.X]
industry: [all|b2b-saas|ecommerce|enterprise|consumer]
company_stage: [all|startup|growth|enterprise]
time_estimate: [X-Y min]
difficulty: [beginner|intermediate|advanced]
frameworks: [List of frameworks used]
tags: [keyword, tags]
related_prompts: [Related prompt names]
version: 1.0
last_updated: YYYY-MM-DD
---

# [Prompt Title]

**Purpose:** [What this prompt helps you achieve]

**Best For:** [Specific use cases]

**Time Required:** [X-Y minutes]

---

## Context & Audience

**Target User:** [Who should use this]

**When to Use:** [Situations where this is valuable]

**Prerequisites:**
- [What data/info user needs]
- [What knowledge is assumed]

---

## Instructions

### Step 1: [Clear step name]

[Specific, actionable instructions]

**What to do:**
- [Bullet point 1]
- [Bullet point 2]
- [Bullet point 3]

**What to avoid:**
- ❌ [Common mistake 1]
- ❌ [Common mistake 2]

### Step 2: [Next step]

[Continue pattern...]

---

## Expected Output

**Format:** [Markdown, table, slides, etc.]

**Structure:**
1. [Section 1]: [Description]
2. [Section 2]: [Description]
3. [Section 3]: [Description]

**Length:** [Word/page count]

**Success Criteria:**
- ✅ [Criterion 1]
- ✅ [Criterion 2]
- ✅ [Criterion 3]

---

## Example Output

```
[Show realistic example following exact format]

This example demonstrates:
- [Key aspect 1]
- [Key aspect 2]
```

---

## Frameworks Reference

**[Framework Name]:**
- [Brief explanation]
- [When to use]
- [How to interpret results]

---

## Tips & Best Practices

💡 **Pro Tips:**
- [Tip 1]
- [Tip 2]
- [Tip 3]

⚠️ **Common Pitfalls:**
- [Pitfall 1 and how to avoid]
- [Pitfall 2 and how to avoid]

🔗 **Related Prompts:**
- [Prompt name]: [When to use instead/additionally]

---

## Customization Options

This prompt can be enhanced for:
- **Industry:** [Industry-specific variations available]
- **Company Stage:** [Stage-specific considerations]
- **Detail Level:** [Quick vs comprehensive options]
- **Output Format:** [Alternative formats]

💬 **Want a customized version?** Ask Claude to enhance this prompt for your specific needs!
```

---

## 🎨 Content Taxonomy

### Product Manager Prompt Library (v1.0)

**Target:** 50-70 world-class PM prompts

#### Category 1: Strategy (10 prompts)

| # | Prompt Name | Description | Priority | CLEAR Target |
|---|-------------|-------------|----------|--------------|
| 1 | Product Vision Statement | Define compelling product vision | P0 | 9.0 |
| 2 | Roadmap Planning (Now/Next/Later) | Create strategic roadmap | P0 | 9.0 |
| 3 | OKR Setting & Tracking | Define measurable objectives | P0 | 8.8 |
| 4 | Market Sizing (TAM/SAM/SOM) | Calculate addressable market | P1 | 8.7 |
| 5 | Business Case Development | Justify product investment | P1 | 8.8 |
| 6 | Go-to-Market Strategy | Plan product launch | P1 | 8.7 |
| 7 | Pricing Strategy | Determine optimal pricing | P1 | 8.6 |
| 8 | Product Positioning | Define market position | P2 | 8.6 |
| 9 | Competitive Strategy | Analyze competitive landscape | P2 | 8.5 |
| 10 | Product-Market Fit Assessment | Measure PMF | P2 | 8.7 |

#### Category 2: Research & Discovery (15 prompts)

| # | Prompt Name | Description | Priority | CLEAR Target |
|---|-------------|-------------|----------|--------------|
| 1 | User Interview Guide | Create interview script | P0 | 9.0 |
| 2 | Interview Analysis (Thematic) | ✅ Already exists | P0 | 9.2 |
| 3 | Survey Design | Create effective surveys | P0 | 8.8 |
| 4 | Survey Analysis | Analyze survey results | P1 | 8.7 |
| 5 | Competitive Analysis | Analyze competitors | P0 | 8.9 |
| 6 | Market Research Report | Synthesize market data | P1 | 8.6 |
| 7 | Persona Development | Create user personas | P0 | 9.0 |
| 8 | Jobs-to-be-Done Analysis | JTBD framework | P1 | 8.7 |
| 9 | Customer Journey Mapping | Map user journey | P1 | 8.8 |
| 10 | Empathy Mapping | Build empathy maps | P2 | 8.5 |
| 11 | Problem Space Exploration | Define problem space | P1 | 8.6 |
| 12 | Opportunity Assessment | Evaluate opportunities | P1 | 8.6 |
| 13 | User Segmentation | Segment users | P2 | 8.5 |
| 14 | Usability Test Planning | Plan usability tests | P2 | 8.5 |
| 15 | Usability Analysis | Analyze test results | P2 | 8.5 |

#### Category 3: Execution & Delivery (15 prompts)

| # | Prompt Name | Description | Priority | CLEAR Target |
|---|-------------|-------------|----------|--------------|
| 1 | PRD Writing | Product requirements doc | P0 | 9.2 |
| 2 | Feature Prioritization | ✅ Already exists | P0 | 9.2 |
| 3 | User Story Writing | Write effective user stories | P0 | 9.0 |
| 4 | Acceptance Criteria | Define acceptance criteria | P0 | 8.8 |
| 5 | Sprint Planning | Plan effective sprints | P0 | 8.9 |
| 6 | Backlog Grooming | Maintain healthy backlog | P1 | 8.6 |
| 7 | Epic Definition | Define product epics | P1 | 8.7 |
| 8 | Technical Spec Review | Review tech specs | P1 | 8.6 |
| 9 | Dependency Mapping | Map dependencies | P2 | 8.5 |
| 10 | Release Planning | Plan releases | P1 | 8.7 |
| 11 | MVP Scope Definition | Define MVP scope | P0 | 9.0 |
| 12 | Feature Flag Strategy | Plan feature flags | P2 | 8.5 |
| 13 | Launch Checklist | Pre-launch checklist | P1 | 8.8 |
| 14 | Post-Launch Review | Review launches | P1 | 8.6 |
| 15 | Retrospective Facilitation | Run effective retros | P1 | 8.7 |

#### Category 4: Analysis & Insights (12 prompts)

| # | Prompt Name | Description | Priority | CLEAR Target |
|---|-------------|-------------|----------|--------------|
| 1 | Feedback Synthesis | ✅ Already exists | P0 | 9.0 |
| 2 | Data Analysis Report | Analyze product data | P0 | 8.8 |
| 3 | A/B Test Design | Design experiments | P0 | 9.0 |
| 4 | A/B Test Analysis | Analyze test results | P0 | 8.9 |
| 5 | Cohort Analysis | Analyze user cohorts | P1 | 8.7 |
| 6 | Funnel Analysis | Analyze conversion funnels | P1 | 8.8 |
| 7 | Churn Analysis | Understand churn | P1 | 8.7 |
| 8 | Feature Usage Analysis | Analyze feature adoption | P1 | 8.6 |
| 9 | SQL Query Generation | Generate analytics queries | P2 | 8.5 |
| 10 | Dashboard Design | Design PM dashboards | P2 | 8.5 |
| 11 | Metrics Definition (KPIs) | Define key metrics | P0 | 9.0 |
| 12 | Impact Assessment | Measure feature impact | P1 | 8.7 |

#### Category 5: Communication (10 prompts)

| # | Prompt Name | Description | Priority | CLEAR Target |
|---|-------------|-------------|----------|--------------|
| 1 | Stakeholder Update | Write stakeholder emails | P0 | 8.9 |
| 2 | Executive Summary | Create exec summaries | P0 | 9.0 |
| 3 | One-Pager Creation | Create product one-pagers | P0 | 8.8 |
| 4 | Presentation Outline | Structure presentations | P1 | 8.6 |
| 5 | Demo Script | Write demo scripts | P1 | 8.6 |
| 6 | Product Announcement | Write announcements | P1 | 8.7 |
| 7 | Change Management Comm | Communicate changes | P2 | 8.5 |
| 8 | Meeting Facilitation | Run effective meetings | P1 | 8.7 |
| 9 | Decision Documentation | Document decisions | P1 | 8.8 |
| 10 | Status Report | Write status reports | P2 | 8.5 |

#### Category 6: Special Workflows (8 prompts)

| # | Prompt Name | Description | Priority | CLEAR Target |
|---|-------------|-------------|----------|--------------|
| 1 | Crisis Response Plan | Handle product crises | P1 | 8.7 |
| 2 | Technical Debt Assessment | Evaluate tech debt | P1 | 8.6 |
| 3 | Feature Sunset Planning | Deprecate features | P2 | 8.5 |
| 4 | Pricing Change Analysis | Analyze pricing changes | P2 | 8.5 |
| 5 | Customer Advisory Board Prep | Prepare for CAB | P2 | 8.5 |
| 6 | Product Portfolio Review | Review product portfolio | P2 | 8.5 |
| 7 | Stakeholder Alignment | Align stakeholders | P1 | 8.6 |
| 8 | Problem Escalation | Escalate issues effectively | P1 | 8.6 |

**Total: 70 prompts**

**Priority Levels:**
- **P0** (Must-have for v1.0): 20 prompts
- **P1** (Should-have for v1.0): 30 prompts
- **P2** (Nice-to-have for v1.0): 20 prompts

### Content Creation Methodology

**Phase 1: Existing Prompts (Week 1)**
- ✅ Migrate 3 existing prompts to new format
- ✅ Score using CLEAR framework
- ✅ Validate template structure works

**Phase 2: P0 Prompts (Week 2-3)**
- Create 20 P0 prompts
- Target: 9.0+ CLEAR score
- Focus on most common PM workflows
- Get 5 PM beta testers to validate

**Phase 3: P1 Prompts (Week 4-5)**
- Create 30 P1 prompts
- Target: 8.5+ CLEAR score
- Expand coverage to complete workflows

**Phase 4: P2 Prompts (Week 6-7)**
- Create 20 P2 prompts
- Target: 8.5+ CLEAR score
- Cover edge cases and advanced workflows

---

## 🚀 Interactive Enhancement Feature

### The Competitive Moat

**Problem with Gumroad PDFs:**
- Static, one-size-fits-all
- Can't customize without manual editing
- No intelligence or adaptation

**Our Solution:**
- Dynamic, AI-powered customization
- Interactive enhancement through conversation
- Adapts to user's specific context

### User Experience Flow

```
┌─────────────────────────────────────────────┐
│  User: "I need to prioritize features"     │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│  Claude (PromptForge Skill activated):      │
│                                             │
│  "I have a world-class Feature             │
│   Prioritization prompt! (CLEAR: 9.2/10)   │
│                                             │
│   It uses RICE/ICE scoring frameworks.     │
│                                             │
│   Want to:                                  │
│   1. Use it as-is                          │
│   2. Customize for your context            │
│   3. See example output first"             │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│  User: "Customize for B2B SaaS"            │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│  Claude: "Great! Let me enhance this       │
│   prompt for B2B SaaS. A few questions:    │
│                                             │
│   1. Company stage?                         │
│      □ Early-stage startup                 │
│      □ Growth stage (Series A-B)           │
│      □ Late stage/Enterprise               │
│                                             │
│   2. Customer type?                         │
│      □ SMB (1-50 employees)                │
│      □ Mid-market (50-500)                 │
│      □ Enterprise (500+)                   │
│                                             │
│   3. Detail level?                          │
│      □ Quick (15 min)                      │
│      □ Standard (30 min)                   │
│      □ Comprehensive (60 min)"             │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│  User: "Growth stage, mid-market, standard"│
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│  Claude: "✨ Enhanced version ready!        │
│                                             │
│   Original CLEAR: 9.2                      │
│   Enhanced CLEAR: 9.5                      │
│                                             │
│   Improvements made:                        │
│   ✓ Added B2B SaaS-specific metrics        │
│     (ARR impact, churn reduction)          │
│   ✓ Included buying committee scoring      │
│   ✓ Added integration complexity factor    │
│   ✓ Adjusted time estimates for your stage │
│                                             │
│   [Display enhanced prompt]                │
│                                             │
│   Actions:                                  │
│   📋 Use this enhanced version             │
│   💾 Save to workspace (.claude/prompts/)  │
│   🔄 Further customize                     │
│   ↩️  Show original                        │
│   📊 Compare side-by-side"                 │
└─────────────────────────────────────────────┘
```

### Enhancement Dimensions

**1. Industry Customization**
- B2B SaaS
- E-commerce
- Consumer Apps
- Enterprise Software
- Healthcare
- FinTech
- Marketplace

**Changes:**
- Industry-specific metrics
- Domain terminology
- Relevant examples
- Compliance considerations

**2. Company Stage**
- Early-stage startup (Pre-seed to Seed)
- Growth stage (Series A-B)
- Late stage (Series C+)
- Enterprise/Public

**Changes:**
- Resource constraints
- Process maturity
- Risk tolerance
- Stakeholder complexity

**3. Detail Level**
- Quick (15 min) - High-level, essential only
- Standard (30-45 min) - Balanced, recommended
- Comprehensive (60+ min) - Deep-dive, thorough

**Changes:**
- Depth of analysis
- Number of examples
- Supporting frameworks
- Deliverable scope

**4. Output Format**
- Executive Brief (1 page)
- Standard Report (3-5 pages)
- Detailed Analysis (10+ pages)
- Presentation (Slides outline)
- Dashboard (Metrics table)

**Changes:**
- Structure and sections
- Length constraints
- Visual elements
- Stakeholder audience

**5. Team Context**
- Solo PM
- PM with designer
- PM with data analyst
- Full product trio (PM/Eng/Design)
- Cross-functional team

**Changes:**
- Collaboration steps
- Delegation points
- Stakeholder involvement
- Review cycles

### Implementation in SKILL.md

```markdown
## Enhancement Engine

When user selects "customize":

### Step 1: Gather Context
Ask user:
- Industry type
- Company stage
- Detail level needed
- Output format preference
- Team structure

### Step 2: Generate Enhanced Prompt
Using Claude's intelligence:
- Read original prompt
- Apply customizations based on context
- Add industry-specific examples
- Adjust metrics and frameworks
- Modify structure for detail level
- Insert stage-appropriate considerations

### Step 3: Score Enhanced Version
- Calculate new CLEAR score
- Compare to original
- Explain what changed and why

### Step 4: Present Options
Show user:
- Enhanced prompt
- CLEAR score comparison
- Key improvements made
- Actions available

### Step 5: Iterate if Needed
Allow user to:
- Further refine
- Try different dimensions
- Combine with other prompts
- Save to workspace
```

---

## 📅 Sprint Plan

### Engineering Lead's Implementation Roadmap

#### Sprint 0: Foundation (Week 1)

**Goals:**
- Set up project structure
- Migrate existing prompts
- Create PromptForge Skill
- Validate architecture

**Tasks:**

**Day 1-2: Project Setup**
- [x] Create directory structure
- [x] Write .claude/claude.md (project context)
- [x] Set up docs/ folder with templates
- [x] Initialize git repo
- [x] Create README.md

**Day 3-4: Migrate Existing Prompts**
- [x] Migrate feature-prioritization.md to new format
- [x] Migrate interview-analysis.md to new format
- [x] Migrate feedback-synthesis.md to new format
- [x] Score all 3 using CLEAR framework
- [x] Validate template structure

**Day 5-7: Create PromptForge Skill**
- [x] Write .claude/skills/promptforge/SKILL.md
- [x] Implement Browse mode
- [x] Implement Load mode
- [x] Implement Search mode
- [x] Test skill activation
- [x] Iterate on skill instructions

**Deliverables:**
- ✅ Working project structure
- ✅ 3 prompts in new format
- ✅ Functional PromptForge Skill (basic)
- ✅ Documentation templates

**Success Criteria:**
- [x] User can browse prompts by category
- [x] User can load specific prompts
- [x] User can search across library
- [x] Skill activates automatically when appropriate

---

#### Sprint 1: P0 Content (Week 2-3)

**Goals:**
- Create 20 P0 (must-have) prompts
- Achieve 9.0+ CLEAR score on all
- Cover core PM workflows

**Content Creation Tasks:**

**Strategy (3 prompts):**
- [ ] Product Vision Statement
- [ ] Roadmap Planning (Now/Next/Later)
- [ ] OKR Setting & Tracking

**Research (4 prompts):**
- [x] Interview Analysis (migrated)
- [ ] User Interview Guide
- [ ] Survey Design
- [ ] Competitive Analysis
- [ ] Persona Development

**Execution (7 prompts):**
- [x] Feature Prioritization (migrated)
- [ ] PRD Writing
- [ ] User Story Writing
- [ ] Acceptance Criteria
- [ ] Sprint Planning
- [ ] MVP Scope Definition

**Analysis (4 prompts):**
- [x] Feedback Synthesis (migrated)
- [ ] Data Analysis Report
- [ ] A/B Test Design
- [ ] A/B Test Analysis
- [ ] Metrics Definition (KPIs)

**Communication (3 prompts):**
- [ ] Stakeholder Update
- [ ] Executive Summary
- [ ] One-Pager Creation

**Quality Process:**
1. Write prompt using template
2. Score using CLEAR framework
3. Iterate until 9.0+ score
4. Peer review with PM
5. Add to library

**Deliverables:**
- ✅ 20 world-class P0 prompts
- ✅ All scored 9.0+ CLEAR
- ✅ Category READMEs updated

**Success Criteria:**
- [x] All P0 prompts complete
- [x] Average CLEAR score ≥ 9.0
- [x] Beta tester validation positive

---

#### Sprint 2: Enhancement Feature (Week 4)

**Goals:**
- Implement interactive enhancement
- Add customization dimensions
- Test enhancement quality

**Tasks:**

**Day 1-2: Enhancement Logic**
- [ ] Add Enhancement mode to SKILL.md
- [ ] Implement context gathering (industry, stage, etc.)
- [ ] Create enhancement templates
- [ ] Build comparison display

**Day 3-4: Customization Dimensions**
- [ ] Implement industry customization
- [ ] Implement stage customization
- [ ] Implement detail level adjustment
- [ ] Implement output format options

**Day 5: Scoring & Comparison**
- [ ] Auto-calculate CLEAR score for enhanced versions
- [ ] Build side-by-side comparison view
- [ ] Explain improvements made
- [ ] Add "save to workspace" functionality

**Day 6-7: Testing & Iteration**
- [ ] Test with all P0 prompts
- [ ] Ensure enhanced versions score higher
- [ ] Get user feedback on enhancement UX
- [ ] Iterate on enhancement prompts

**Deliverables:**
- ✅ Working enhancement feature
- ✅ All customization dimensions functional
- ✅ CLEAR scoring for enhanced versions
- ✅ User-friendly enhancement UX

**Success Criteria:**
- [x] Users can customize any prompt
- [x] Enhanced versions score 0.2-0.5 points higher
- [x] Enhancement takes <60 seconds
- [x] Improvements are actually valuable (user validation)

---

#### Sprint 3: P1 Content (Week 5-6)

**Goals:**
- Create 30 P1 prompts
- Achieve 8.5+ CLEAR score
- Complete core library coverage

**Content Creation Tasks:**
- [ ] Strategy category: 7 more prompts
- [ ] Research category: 10 more prompts
- [ ] Execution category: 8 more prompts
- [ ] Analysis category: 7 more prompts
- [ ] Communication category: 7 more prompts
- [ ] Special Workflows category: 8 prompts

**Week 5 Focus:**
- Mon-Tue: Strategy + Research (8 prompts)
- Wed-Thu: Execution + Analysis (8 prompts)
- Fri: Communication (4 prompts)

**Week 6 Focus:**
- Mon-Tue: Special Workflows (8 prompts)
- Wed-Thu: Quality review and iteration
- Fri: Documentation updates

**Deliverables:**
- ✅ 30 additional prompts (50 total)
- ✅ All scored 8.5+ CLEAR
- ✅ Complete library documentation

**Success Criteria:**
- [x] 50 total prompts in library
- [x] Average CLEAR score ≥ 8.7
- [x] All core PM workflows covered

---

#### Sprint 4: Polish & Launch Prep (Week 7)

**Goals:**
- Final quality pass
- Create marketing materials
- Prepare for public launch

**Tasks:**

**Day 1-2: Quality Review**
- [ ] Review all 50 prompts for consistency
- [ ] Ensure all follow template exactly
- [ ] Verify all CLEAR scores accurate
- [ ] Fix any formatting issues
- [ ] Update all cross-references

**Day 3: Documentation**
- [ ] Write comprehensive README.md
- [ ] Create QUALITY_STANDARDS.md
- [ ] Write ENHANCEMENT_GUIDE.md
- [ ] Add usage examples to EXAMPLES.md
- [ ] Create quick-start guide

**Day 4: Demo & Marketing**
- [ ] Record demo video (2-3 min)
- [ ] Create demo GIFs for README
- [ ] Write Product Hunt description
- [ ] Draft launch tweet thread
- [ ] Create comparison chart (vs Gumroad)

**Day 5: Beta Testing**
- [ ] Invite 10 PM beta testers
- [ ] Gather feedback
- [ ] Fix any critical issues
- [ ] Collect testimonials

**Day 6-7: Launch**
- [ ] Final testing
- [ ] Publish to GitHub
- [ ] Post on Product Hunt
- [ ] Share on Twitter, Reddit (r/ProductManagement)
- [ ] Send to PM communities

**Deliverables:**
- ✅ Production-ready library
- ✅ Complete documentation
- ✅ Marketing materials
- ✅ Public GitHub repo
- ✅ Successful launch

**Success Criteria:**
- [x] Zero critical bugs
- [x] Positive beta feedback
- [x] Product Hunt launch successful
- [x] 100+ GitHub stars in week 1

---

### Post-Launch Roadmap

#### Month 2: Community & Iteration

**Goals:**
- Gather user feedback
- Add most-requested prompts
- Build community

**Tasks:**
- [ ] Monitor GitHub issues and discussions
- [ ] Add 5-10 prompts based on requests
- [ ] Improve enhancement feature based on usage
- [ ] Create contribution guidelines
- [ ] Feature top community use cases

**Metrics:**
- Active users (GitHub clones)
- GitHub stars/forks
- Community engagement (issues, discussions)
- User testimonials

#### Month 3-4: P2 Content + Expansion

**Goals:**
- Complete 70-prompt library
- Explore new categories
- Build integrations

**Tasks:**
- [ ] Add remaining 20 P2 prompts
- [ ] Explore adjacent categories (Eng Manager, Designer?)
- [ ] Build MCP server for advanced features
- [ ] Create "Prompt Packages" (themed bundles)
- [ ] Add semantic search with embeddings

#### Month 5-6: Platform Evolution

**Goals:**
- Community contributions
- Multi-role expansion
- Ecosystem building

**Tasks:**
- [ ] Accept community-contributed prompts
- [ ] Launch Engineering Manager prompt library
- [ ] Launch Designer prompt library
- [ ] Build prompt marketplace concept
- [ ] Create PromptForge certification program

---

## 🎯 Success Metrics & KPIs

### Launch Metrics (Week 1)

**Adoption:**
- 🎯 Target: 100 GitHub stars
- 🎯 Target: 50 unique clones
- 🎯 Target: 10 engaged community members

**Quality:**
- 🎯 Target: Average CLEAR score ≥ 8.7
- 🎯 Target: Zero critical bugs reported
- 🎯 Target: 90% positive feedback from beta testers

**Engagement:**
- 🎯 Target: 500 Product Hunt upvotes
- 🎯 Target: 20 Twitter shares
- 🎯 Target: 5 testimonials collected

### Month 1 Metrics

**Growth:**
- 🎯 Target: 500 GitHub stars
- 🎯 Target: 200 active users
- 🎯 Target: 50 community discussions

**Content:**
- 🎯 Target: 50 prompts live
- 🎯 Target: 5 new prompts from user requests
- 🎯 Target: 100% of P0 + P1 complete

**Engagement:**
- 🎯 Target: 10 community PRs
- 🎯 Target: 20 user testimonials
- 🎯 Target: Featured in 2 PM newsletters

### Month 3 Metrics

**Scale:**
- 🎯 Target: 2,000 GitHub stars
- 🎯 Target: 1,000 active users
- 🎯 Target: 100 community contributors

**Content:**
- 🎯 Target: 70 prompts live
- 🎯 Target: 10 community-contributed prompts
- 🎯 Target: 95% average CLEAR score

**Impact:**
- 🎯 Target: 5,000 hours saved (estimate)
- 🎯 Target: $50K+ in tool costs saved (vs commercial tools)
- 🎯 Target: Featured in major PM publication

---

## 💰 Business Model Considerations

### Phase 1: Pure Open Source (Months 1-6)

**Strategy:**
- 100% free, MIT license
- Focus on adoption and quality
- Build reputation and community

**Revenue:** $0 (intentional)

**Investment:**
- Time: 200-300 hours total
- Cost: $0 (uses Claude Pro subscription)

### Phase 2: Services Layer (Months 7-12)

**Optional Paid Services:**
- Custom prompt creation: $500-1,000 per prompt
- Team training workshops: $2,000-5,000
- Private prompt libraries: $5,000-10,000
- Consulting: $200-300/hour

**Keep Base Free:**
- All 70+ prompts remain free
- Enhancement feature remains free
- Community features remain free

### Phase 3: Ecosystem (Year 2)

**Potential Revenue Streams:**
- Premium prompt packages: $29-99
- Enterprise features (team sync): $10/user/mo
- PromptForge certification: $299
- Sponsored prompts: $1,000-5,000

**Core Commitment:**
- Base library always free
- No features behind paywall that hurt individual users
- Community-first approach

---

## 🛡️ Risk Mitigation

### Technical Risks

**Risk 1: Claude Code API Changes**
- **Likelihood:** Medium
- **Impact:** High
- **Mitigation:**
  - Follow official Claude Code best practices
  - Stay active in Claude community
  - Build on stable Skills API
  - Have fallback to slash commands

**Risk 2: CLEAR Scoring Inconsistency**
- **Likelihood:** Medium
- **Impact:** Medium
- **Mitigation:**
  - Document scoring methodology clearly
  - Have multiple reviewers
  - Use rubrics and examples
  - Iterate on framework based on usage

**Risk 3: Enhancement Quality Varies**
- **Likelihood:** High
- **Impact:** Medium
- **Mitigation:**
  - Test enhancement with real users
  - Add quality checks
  - Allow user to iterate
  - Provide "revert to original" option

### Market Risks

**Risk 1: Low Adoption**
- **Likelihood:** Low
- **Impact:** High
- **Mitigation:**
  - Validate with beta users first
  - Focus on quality over quantity
  - Active marketing and community building
  - Solve real PM pain points

**Risk 2: Gumroad Sellers Improve**
- **Likelihood:** Medium
- **Impact:** Low
- **Mitigation:**
  - Our interactive enhancement is unique
  - Native Claude Code integration can't be matched
  - Community-driven beats solo creators
  - We can move faster (no dependencies)

**Risk 3: Commercial Tool Copies Us**
- **Likelihood:** Low
- **Impact:** Medium
- **Mitigation:**
  - Open source = hard to compete with free
  - Community moat
  - Speed of iteration
  - Quality focus

### Execution Risks

**Risk 1: Content Creation Takes Too Long**
- **Likelihood:** Medium
- **Impact:** Medium
- **Mitigation:**
  - Start with 20 P0 prompts (achievable)
  - Use existing 3 prompts as foundation
  - Leverage Claude to draft prompts faster
  - Recruit PM contributors

**Risk 2: Quality Drops**
- **Likelihood:** Medium
- **Impact:** High
- **Mitigation:**
  - Strict CLEAR score minimum (8.5)
  - Peer review process
  - Beta tester validation
  - User feedback loops

**Risk 3: Scope Creep**
- **Likelihood:** High
- **Impact:** Medium
- **Mitigation:**
  - Stick to PM prompts only for v1
  - Resist adding features
  - MVP mindset
  - Launch fast, iterate

---

## 🎓 Lessons from Research

### From PromptForge Technical Architecture

**Key Takeaways:**
1. ✅ Skills > Slash Commands (seamless UX)
2. ✅ Pure Markdown > JSON (git-friendly, simple)
3. ✅ Proactive > Reactive (auto-invoke when helpful)
4. ✅ Single file operations > Complex state management

**Applied Decisions:**
- Using Skills-first architecture
- All prompts in markdown with YAML frontmatter
- No JSON indices (single source of truth)
- Auto-invoke PromptForge when user needs prompts

### From PM Research Suite Examples

**Key Takeaways:**
1. ✅ Framework-based prompts work best (RICE, JTBD, etc.)
2. ✅ Step-by-step structure reduces cognitive load
3. ✅ Examples are critical for clarity
4. ✅ Output format specification prevents ambiguity

**Applied Decisions:**
- Every prompt references established frameworks
- Step-by-step instruction format
- Minimum 2 examples per prompt
- Explicit output format in all prompts

### From Competitive Analysis

**Key Takeaways:**
1. ✅ Gumroad prompts are quantity over quality
2. ✅ Static PDFs can't adapt to context
3. ✅ No community/updates after purchase
4. ✅ Copy-paste friction is real

**Applied Decisions:**
- Focus on 50-70 EXCELLENT prompts (not 500 mediocre)
- Interactive enhancement feature (unique advantage)
- Git-based updates (users git pull for new prompts)
- Native Claude Code integration (zero friction)

### From CLEAR Framework Research

**Key Takeaways:**
1. ✅ 5-dimension scoring works well
2. ✅ 8.5+ CLEAR score = production-ready
3. ✅ Examples and specificity are most important
4. ✅ Audience context often missing in prompts

**Applied Decisions:**
- Adopted CLEAR framework as standard
- Minimum 8.5 score for inclusion
- Template enforces examples and specificity
- Mandatory audience/context section

---

## 🚀 Next Steps

### Immediate Actions (This Week)

**Engineering Lead:**
- [x] Create project structure (directories, files)
- [ ] Set up Git repo
- [ ] Write initial .claude/claude.md
- [ ] Create prompt template

**Prompt Engineer:**
- [ ] Finalize CLEAR scoring rubric
- [ ] Review 3 existing prompts
- [ ] Score existing prompts
- [ ] Identify improvements needed

**Claude Code Expert:**
- [ ] Write PromptForge SKILL.md (v1)
- [ ] Test skill activation
- [ ] Document skill behaviors
- [ ] Create enhancement prompt templates

### Week 1 Checkpoint (Friday)

**Deliverables to Review:**
- ✅ Complete project structure
- ✅ 3 prompts migrated and scored
- ✅ Working PromptForge Skill
- ✅ Documentation templates

**Review Questions:**
- Does skill activate appropriately?
- Are CLEAR scores accurate and consistent?
- Is prompt template complete?
- Are we ready for content creation?

### Week 2-3 Focus

**All Hands on Deck: P0 Content Creation**
- Target: 20 P0 prompts
- Quality bar: 9.0+ CLEAR
- Process: Draft → Score → Iterate → Review → Publish

### Month 1 Goal

**Shippable Product:**
- 50 world-class PM prompts
- Interactive enhancement feature
- Complete documentation
- Beta-tested and validated
- Ready for public launch

---

## 📊 Appendix: Template Examples

### Prompt File Template

See full template in "Prompt Engineering Framework" section above.

### SKILL.md Structure

```markdown
---
name: promptforge
description: Browse, load, and enhance world-class Product Manager prompts
---

# PromptForge Skill

## When to Activate
[Detailed activation criteria]

## Browse Mode
[How to show prompt library]

## Load Mode
[How to display specific prompts]

## Enhancement Mode
[How to customize prompts interactively]

## Search Mode
[How to find prompts semantically]

[Detailed implementation instructions...]
```

### Category README Template

```markdown
# [Category Name] Prompts

## Overview
[Description of this category]

## When to Use These Prompts
[Common scenarios]

## Available Prompts

### [Subcategory Name]
1. **[Prompt Name]** (CLEAR: X.X) - [Description]
2. **[Prompt Name]** (CLEAR: X.X) - [Description]

## Getting Started
[Quick start guide for this category]

## Related Categories
[Links to related prompt categories]
```

---

## ✅ Final Decisions Summary

### Architecture
- ✅ **Skills-first** (not slash commands)
- ✅ **Pure markdown** with YAML frontmatter (no JSON)
- ✅ **Category-based** file organization
- ✅ **Proactive** skill activation

### Content
- ✅ **50-70 prompts** for v1.0 (P0 + P1 + select P2)
- ✅ **Product Manager** focus only (v1)
- ✅ **9.0+ CLEAR** for P0, 8.5+ for P1/P2
- ✅ **Framework-based** prompts (RICE, JTBD, etc.)

### Features
- ✅ **Browse** by category
- ✅ **Load** specific prompts
- ✅ **Enhance** interactively (killer feature)
- ✅ **Search** semantically
- ✅ **No user prompt management** (v1)

### Quality
- ✅ **CLEAR framework** as standard
- ✅ **Peer review** process
- ✅ **Beta testing** with real PMs
- ✅ **Continuous improvement** via community

### Business
- ✅ **100% free** and open source (v1)
- ✅ **MIT license**
- ✅ **Community-driven**
- ✅ **Services layer** possible (future)

### Timeline
- ✅ **Week 1:** Foundation + Skill + 3 prompts
- ✅ **Week 2-3:** 20 P0 prompts
- ✅ **Week 4:** Enhancement feature
- ✅ **Week 5-6:** 30 P1 prompts
- ✅ **Week 7:** Polish + Launch

**Target Launch Date: 7 weeks from today**

---

## 🎉 Closing Remarks

### Engineering Lead

"This is a well-scoped MVP with clear technical architecture. The Skills-first approach leverages Claude Code's strengths perfectly. The enhancement feature is technically achievable and provides real differentiation. I'm confident we can ship this in 7 weeks with high quality."

**Confidence Level: 9/10**

### Prompt Engineer

"The CLEAR framework gives us objective quality standards. The template structure is comprehensive and repeatable. 50-70 world-class prompts is ambitious but achievable with the right process. The frameworks (RICE, JTBD, etc.) give us strong foundations to build on."

**Confidence Level: 8.5/10**

### Claude Code Expert

"Skills are the right abstraction for this use case. The user experience will feel magical - no commands to remember, just natural conversation. The markdown-only approach is clean and maintainable. Enhancement via Claude's intelligence is the killer feature."

**Confidence Level: 9/10**

---

**Team Consensus: APPROVED ✅**

**Let's build this! 🚀**

---

**Document Status:** FINAL
**Next Review:** End of Sprint 0 (Week 1)
**Owner:** Engineering Lead
**Last Updated:** November 6, 2025
