---
description: Browse PromptForge PM prompt library by category
---

# Browse PromptForge Prompts

Help users explore the prompt library organized by category.

## Categories

**1. Strategy** (10-12 prompts)
Vision, roadmaps, OKRs, goal setting, strategic planning

**2. Research** (12-15 prompts)
User interviews, personas, competitive analysis, market research

**3. Execution** (12-15 prompts)
PRDs, user stories, sprint planning, backlog management

**4. Analysis** (10-12 prompts)
A/B testing, metrics, data analysis, experiment design

**5. Communication** (8-10 prompts)
Stakeholder updates, exec summaries, presentations

**6. Special Workflows** (8-10 prompts)
Launch plans, end-to-end processes, cross-functional workflows

## Behavior

**If category specified:**
- Show all prompts in that category
- Include: name, one-line description, time estimate
- Offer to load or enhance any prompt

**If no category:**
- List all 6 categories with descriptions
- Suggest relevant category based on context

## Interactive Flow

```
User: /prompt-browse strategy

You: # Strategy Prompts (10 available)

**1. Product Vision Statement**
Create compelling vision statements that align teams
⏱️ 15-20 min | Frameworks: Vision, North Star

**2. Quarterly Roadmap Creation**
Build quarterly roadmaps with OKR alignment
⏱️ 30-45 min | Frameworks: OKRs, Now-Next-Later

[... more prompts]

What would you like to do?
- Load a prompt ("show me #2")
- Customize for your context ("enhance #2 for Series A SaaS")
- Browse another category
```

## User Customizations

Check `.claude/prompts/custom/` for user versions and show those with `[Custom]` marker when available.
