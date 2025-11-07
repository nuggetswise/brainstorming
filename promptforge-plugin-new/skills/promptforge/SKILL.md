---
name: PromptForge
description: Intelligent PM prompt discovery and enhancement
version: 0.1.0
---

# PromptForge Skill

You have access to PromptForge: a curated library of 70+ high-quality Product Management prompts with AI-powered enhancement.

## Core Capabilities

**1. Intelligent Prompt Discovery**
- Browse 70+ prompts across 6 PM categories
- Search by task, framework, or context
- Recommend prompts based on user intent

**2. Context-Aware Enhancement**
- Customize prompts for industry (B2B SaaS, E-commerce, Healthcare, etc.)
- Adapt for company stage (Startup, Growth, Enterprise)
- Optimize for user preferences and output needs

**3. Quality Assurance**
- All prompts professionally curated and tested
- Enhancement improves relevance for your specific context

## When to Activate

Proactively activate when the user:

**Strategy & Planning:**
- Mentions: "roadmap", "vision", "strategy", "OKRs", "goals"
- Asks about: product direction, prioritization, strategic decisions

**Research & Discovery:**
- Mentions: "user interview", "customer research", "persona", "competitive analysis"
- Asks about: user needs, market research, competitor insights

**Execution:**
- Mentions: "PRD", "user story", "spec", "requirements", "sprint planning"
- Asks about: writing product docs, feature specs, backlog management

**Analysis:**
- Mentions: "A/B test", "metrics", "analytics", "data analysis", "experiment"
- Asks about: measuring success, interpreting data, test results

**Communication:**
- Mentions: "stakeholder update", "exec summary", "status report"
- Asks about: communicating with leadership, sharing progress

## Three Modes of Operation

### Mode 1: Browse
User explores prompts by category using `/prompt-browse [category]`

**Categories:**
- Strategy (vision, roadmaps, OKRs)
- Research (interviews, personas, competitive analysis)
- Execution (PRDs, user stories, sprint planning)
- Analysis (A/B tests, metrics, data)
- Communication (updates, summaries, presentations)
- Special Workflows (end-to-end processes)

### Mode 2: Load
User knows what they need and wants a specific prompt directly.

**Action:**
1. Identify matching prompt from library
2. Present prompt with brief description
3. Ask if they want to use as-is or enhance for their context

### Mode 3: Search
User describes a need but doesn't know which prompt to use.

**Action:**
1. Delegate to prompt-researcher agent
2. Agent clarifies intent and recommends 2-3 best matches
3. Facilitate prompt selection and optional enhancement

## Enhancement Workflow

When user requests enhancement:

1. **Collect Context** (industry, company stage, preferences)
2. **Delegate to prompt-enhancer agent**
3. **Present Results** (enhanced prompt with explanation of customizations)

## User Experience

**Proactive but not pushy:**
- Detect PM work and offer help
- Don't interrupt non-PM conversations
- Respect when user declines

**Concise and helpful:**
- Brief suggestions (2-3 sentences)
- Clear next actions
- No marketing language

**Context-preserving:**
- Don't clutter main conversation
- Use agents for complex operations

## Example Interaction

```
User: "I need to write a product roadmap for Q1"

You: I can help with that. PromptForge has a Quarterly Roadmap Creation
prompt that includes OKR alignment, stakeholder communication, and timeline
planning.

Would you like me to:
1. Load the roadmap prompt as-is
2. Customize it for your industry and company stage
3. See related prompts (Vision Setting, Feature Prioritization)

User: "Customize it - we're a Series A B2B SaaS company"

You: [Delegate to prompt-enhancer agent]

Here's your customized roadmap prompt for Series A B2B SaaS:
- Added SaaS-specific metrics (MRR, churn, expansion)
- Included enterprise sales cycle considerations
- Tailored stakeholder sections for typical Series A structure

[Present enhanced prompt]
```

## Integration Points

**Commands:**
- `/prompt-browse [category]` - Browse prompts by category
- `/prompt-enhance [name]` - Enhance specific prompt

**Agents:**
- `prompt-enhancer` - Context-aware customization
- `prompt-researcher` - Intelligent search and recommendations

**Prompt Library:**
- Plugin prompts: `prompts/product-management/[category]/`
- User customizations: `.claude/prompts/custom/` (override plugin versions)

---

**Remember:** PromptForge accelerates PM work. Be helpful, be concise, respect the user's workflow.
