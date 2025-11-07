---
name: Customer Interview Guide
category: research
description: Conduct effective user interviews to uncover pain points, needs, and opportunities

# Internal Quality
prime_score: 9.1
last_validated: 2025-11-07
peer_reviewed: true

# Context
industry: [All]
company_stage: [All]
audience: Product Managers, User Researchers, Founders
prerequisites:
  - Identified target user segment
  - Clear research goals
  - Note-taking tool or recording capability

# Characteristics
time_estimate: 45-60 minutes per interview
difficulty: Medium
frameworks: [Jobs-to-be-Done, Customer Development, Five Whys]
output_format: Interview transcript with thematic notes

tags: [research, interviews, discovery, user-research, qualitative]
related_prompts:
  - Feedback Synthesis & Theming
  - User Persona Development
  - Jobs-to-be-Done Research
version: 1.0
last_updated: 2025-11-07
---

# Customer Interview Guide

Conduct structured user interviews that uncover genuine user needs, pain points, and motivations—not just feature requests or surface-level feedback.

## When to Use

**Use this prompt when:**
- Exploring problem-solution fit for new products
- Understanding user workflows and pain points
- Validating assumptions before building features
- Conducting discovery research for roadmap planning
- Building user personas from real data

**Don't use when:**
- You need quantitative data (use surveys instead)
- Validating specific UI designs (use usability testing)
- You haven't defined what you're trying to learn

**Typical timing:**
- Early stage: Before building MVP or new features
- Growth stage: Regular cadence (monthly or quarterly)
- Ongoing: After major releases or pivots

## Prerequisites

Before conducting interviews:

1. **Research Goals Defined**
   - What specific questions are you trying to answer?
   - What decisions will this inform?

2. **Target Users Identified**
   - Clear user segment (e.g., "Enterprise procurement managers")
   - Recruitment criteria documented

3. **Logistics Ready**
   - Recording tool or note-taker
   - Consent forms (if recording)
   - 45-60 minute time blocks scheduled

## Target Audience

**Primary:** Product Managers, Founders conducting discovery research

**Experience Level:** All levels (guide provides structure for beginners, depth for experienced)

## Frameworks Incorporated

**Jobs-to-be-Done (JTBD)**
- Focus on the "job" users are hiring your product to do
- Understand context, motivations, and desired outcomes

**Customer Development**
- Problem interviews before solution interviews
- Learn, don't sell

**Five Whys**
- Dig beneath surface answers to root causes
- Understand true motivations

## Interview Structure

### Before the Interview (10 min prep)

**Review your research goals:**
- What are the top 3 questions you need answered?
- What assumptions are you testing?

**Prepare your mindset:**
- You're here to learn, not validate
- Users will be polite—dig for the truth
- Feature requests are symptoms, not root causes

### Opening (5 min)

**Set the stage:**
```
"Thanks for taking the time. I'm [name] from [company]. We're working on
[problem space] and want to understand how people like you currently
handle [situation].

This isn't a sales call—I genuinely want to learn about your experience,
including what's frustrating or not working well. There are no wrong
answers, and honest feedback helps us build better products.

I'd like to record this so I can focus on our conversation instead of
frantically taking notes. Is that okay? Everything you share stays
confidential."
```

**Icebreaker:**
"Tell me a bit about your role and what a typical day looks like for you."

### Discovery Questions (30-40 min)

**Current State (10-15 min)**

Understand how they solve the problem today:

1. "Walk me through the last time you needed to [do relevant task]"
   - Listen for: actual behavior, not aspirational
   - Follow up: "What happened next?" (get the full story)

2. "What tools or processes do you currently use for this?"
   - Listen for: workarounds, manual steps, multiple tools
   - Follow up: "Why that tool specifically?"

3. "What's most frustrating about how you handle this today?"
   - Listen for: real pain points, not feature wishlists
   - Follow up: "Can you give me a specific example?"

**Pain Points (10-15 min)**

Dig into problems and their impact:

4. "What would happen if you couldn't solve this problem?"
   - Listen for: consequences, business impact, emotional response
   - Follow up: "How often does this come up?"

5. "Have you tried to solve this differently? What happened?"
   - Listen for: failed attempts, why they didn't stick
   - Follow up: "What would need to be true for that to work?"

6. "On a scale of 1-10, how painful is this problem?"
   - If <7: "What makes it tolerable?"
   - If ≥7: "Why haven't you solved it yet?"

**Context & Motivation (10 min)**

Understand the "job" they're trying to get done:

7. "What are you ultimately trying to accomplish when you [do this task]?"
   - Listen for: higher-level goals, not just task completion
   - Follow up with "Why?" 2-3 times (Five Whys)

8. "What does success look like in this situation?"
   - Listen for: metrics, outcomes, feelings
   - Follow up: "How do you know when you've succeeded?"

9. "Who else is involved or affected by this?"
   - Listen for: stakeholders, dependencies, organizational context

**Solution Exploration (Optional, 5 min)**

Only if there's time and you've built rapport:

10. "If you could wave a magic wand and fix this, what would change?"
    - Listen for: outcomes, not features
    - Follow up: "Why would that matter?"

### Closing (5 min)

**Wrap up:**
```
"This has been really helpful. Before we finish:

1. Is there anything important about [topic] that I didn't ask about?
2. Can I follow up if I have clarifying questions?
3. Do you know others in similar situations who might be willing to talk?"
```

**Thank them:**
- Offer incentive if promised (gift card, early access, etc.)
- Send thank you email within 24 hours

## Interview Techniques

**DO:**
- ✅ Ask about specific past experiences ("Tell me about the last time...")
- ✅ Follow up with "Why?" and "Tell me more about that"
- ✅ Embrace silence—let them think and elaborate
- ✅ Take notes on exact quotes (use their words)
- ✅ Observe their emotion and energy shifts

**DON'T:**
- ❌ Lead with your solution ("Would you use a product that...")
- ❌ Ask hypothetical questions ("Would you...?" "If we built...")
- ❌ Accept vague answers ("it's fine", "sometimes")
- ❌ Interrupt or finish their sentences
- ❌ Pitch your product or defend your ideas

## Success Criteria

You've conducted a successful interview when:

✅ You have 3+ specific stories about how they currently solve the problem
✅ You understand the pain level and consequences of the problem
✅ You identified underlying motivations (the "why" behind the "what")
✅ You discovered at least one thing you didn't expect
✅ You have direct quotes you can share with your team

## Example: B2B SaaS PM Interviewing Enterprise Buyer

**Context:** SaaS company building project management tool, interviewing IT procurement manager

**Opening:**
```
PM: "Thanks for your time, Sarah. I'm Alex from TaskFlow. We're exploring
how teams collaborate on projects and want to understand your experience.
This isn't a sales pitch—I genuinely want to learn about what works and
what doesn't. Cool if I record this?"

Sarah: "Sure, that's fine."

PM: "Great. Tell me about your role—what does a typical week look like?"
```

**Discovery:**
```
PM: "Walk me through the last time you had to evaluate and buy a new tool
for your team."

Sarah: "Oh, that was just last quarter. We needed a CRM. The sales team
had been using spreadsheets and it was a mess. I spent probably 40 hours
over two months evaluating options."

PM: "40 hours is a lot. What took so long?"

Sarah: "Well, first I had to gather requirements from sales, support, and
marketing. Everyone wanted different things. Then I had to research vendors,
set up demos, manage a pilot with 3 finalists, get security to approve,
negotiate pricing, and convince finance it was worth it."

PM: "What was the most frustrating part?"

Sarah: "Honestly? Getting everyone aligned on what we actually needed versus
nice-to-haves. And then after all that work, the tool we picked had terrible
implementation support, so I'm basically the internal help desk now."

PM: "What would have happened if you hadn't bought anything?"

Sarah: "Sales would have killed me. [laughs] But seriously, we were losing
deals because reps couldn't track follow-ups. And our customer data was all
over the place—huge compliance risk."

PM: "On a scale of 1-10, how painful was that buying process?"

Sarah: "Probably an 8. I put off other projects for two months."

PM: "Why is it so hard?"

Sarah: "There's no good way to compare tools side by side. Every vendor demo
shows the happy path, but I need to know: will this integrate with our SSO?
Can our security team audit it? What happens when 500 people start using it?
Nobody tells you that upfront."
```

**Key Insights Captured:**
- 40+ hours spent on tool evaluation (quantified pain)
- Real consequence: compliance risk, lost deals
- Workaround: manual spreadsheets causing problems
- Root problem: Hard to evaluate vendors on real criteria (not features)
- Emotional response: frustration, ongoing burden

## Top 5 Tips

1. **Ask About Past Behavior, Not Future Intent**
   People are terrible at predicting what they'll do. Ask "Tell me about the last time you..." not "Would you...?"

2. **Dig 3 Levels Deep with "Why?"**
   First answer is usually surface level. Keep asking why to uncover real motivations and root causes.

3. **Listen for Workarounds**
   When users say "I just..." or "The way I handle it is...", they're describing a workaround. These reveal real pain.

4. **Shut Up and Listen**
   You should talk 20% of the time max. Silence is powerful—let them fill it.

5. **Take Notes on Exact Words**
   Their phrases reveal mental models and priorities. "I have to babysit it" means something different than "I need to monitor it."

## Common Pitfalls

**Pitfall 1: Asking Leading Questions**
- ❌ **Problem:** "Don't you think it would be better if...?"
- ✅ **Solution:** "How do you currently handle...?" "What works/doesn't work about that?"
- **Why it matters:** Leading questions get you the answer you want to hear, not the truth.

**Pitfall 2: Accepting Feature Requests at Face Value**
- ❌ **Problem:** User says "I need a dashboard" and you write that down as a requirement
- ✅ **Solution:** Ask "What would you use that dashboard for? Tell me about a time you needed that information."
- **Why it matters:** Features are solutions. You need to understand the underlying problem.

**Pitfall 3: Interviewing the Wrong People**
- ❌ **Problem:** Talking to whoever volunteers or is easiest to reach
- ✅ **Solution:** Define your target user precisely and recruit accordingly
- **Why it matters:** Insights from non-target users will lead you astray.

## After the Interview

**Within 24 hours:**
- Send thank you email
- Write up key insights while fresh (don't just rely on recording)
- Tag themes and patterns
- Share direct quotes with team

**After 3-5 interviews:**
- Use Feedback Synthesis prompt to identify patterns
- Update assumptions document (what was validated/invalidated)
- Share learnings with stakeholders

**After 10+ interviews:**
- Build personas from real data
- Document common user journeys
- Prioritize problems by frequency and severity

## Related Prompts

**Before this prompt:**
- Define research goals and hypotheses

**After this prompt:**
- Feedback Synthesis & Theming (analyze multiple interviews)
- User Persona Development (build personas from insights)
- Jobs-to-be-Done Research (deep dive on user motivations)

**Alternatives:**
- User Testing Protocol (for evaluating solutions, not discovering problems)
- Competitive Analysis (for understanding market, not users)

---

**Questions or feedback?** Open an issue on GitHub.
