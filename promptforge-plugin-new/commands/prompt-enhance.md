---
description: Enhance a PromptForge prompt for your specific context
---

# Enhance Prompt for Your Context

Customize a PromptForge prompt to match your industry, company stage, and preferences using AI.

## Purpose

Transform high-quality generic prompts into context-specific versions optimized for your situation.

## How It Works

Delegates to the **Prompt Enhancer** agent:

1. **Collects context** (industry, stage, team, preferences)
2. **Customizes the prompt** (examples, metrics, stakeholders, frameworks)
3. **Validates quality** (ensures improvement)
4. **Presents results** (enhanced prompt + explanation)

## Usage

**With prompt name:**
```
/prompt-enhance "Feature Prioritization Matrix"
/prompt-enhance PRD Writing Guide
```

**With context:**
```
/prompt-enhance "Roadmap Creation" for Series A B2B SaaS
```

## What Gets Customized

**Examples**: Generic → Industry-specific
- B2B SaaS: MRR, churn, enterprise sales
- E-commerce: Conversion, cart abandonment
- Healthcare: Compliance, patient outcomes

**Metrics**: Universal → Industry KPIs
- SaaS: ARR, NRR, CAC, LTV
- Marketplace: GMV, take rate
- Consumer: DAU, retention

**Stakeholders**: Generic → Your org structure
- Seed: CEO, co-founders
- Growth: CPO, engineering leads
- Enterprise: VPs, directors

**Tone**: Neutral → Cultural fit
- Startup: Fast-paced, bias to action
- Corporate: Process-oriented
- Technical: Data-driven

## Expected Timeline

- Simple enhancement: 30-60 seconds
- Full enhancement: 1-2 minutes
- Complex prompts: 2-3 minutes with progress updates

## After Enhancement

You'll receive:
- Full enhanced prompt
- Explanation of key customizations
- Recommendation (enhanced vs. original)
- Option to iterate

## Tips

- Be specific: "Series A B2B SaaS" > "startup"
- Mention constraints: Solo PM, enterprise sales, healthcare compliance
- You can iterate if first attempt isn't perfect
