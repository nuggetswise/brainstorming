# Feedback Synthesis

Synthesize insights from multiple feedback sources (interviews, surveys, support tickets, reviews) to identify patterns and priorities.

**Replaces:** Dovetail synthesis features, manual spreadsheet analysis

## Instructions

You are an expert at synthesizing qualitative and quantitative feedback from multiple sources.

### Step 1: Data Collection
Gather all feedback sources provided:
- Interview transcripts
- Survey responses
- Support tickets
- App reviews
- User comments
- Feature requests
- Sales feedback

### Step 2: Cross-Source Analysis
Identify patterns across sources:
- What themes appear in multiple sources?
- Are there contradictions between sources?
- What's the frequency of each theme?
- What's the sentiment (positive/negative/neutral)?
- Who is reporting this (segment, role, company size)?

### Step 3: Pattern Recognition
Group related feedback into clusters:
- Similar pain points
- Common feature requests
- Recurring use cases
- Consistent objections
- Shared frustrations

### Step 4: Prioritization
For each cluster, calculate:
- **Frequency Score**: How many people mentioned this? (1-5)
- **Impact Score**: How significant is this issue? (1-5)
- **Evidence Quality**: How concrete is the feedback? (1-5)
- **Urgency**: How time-sensitive? (1-5)
- **Priority Score**: Average of above (1-5)

### Step 5: Synthesis Report
Generate comprehensive synthesis with:
- Overall themes
- Top priorities
- Segment differences
- Actionable recommendations
- Supporting evidence

## Input

Provide feedback sources as:
```bash
/pm/feedback-synthesis [file1] [file2] [file3] ...
```

Or specify a directory:
```bash
/pm/feedback-synthesis feedback/january-2025/*
```

Arguments: $ARGUMENTS

## Output Format

```markdown
# Feedback Synthesis Report

**Date**: [Today's date]
**Sources Analyzed**: [Number] sources across [types]
**Total Feedback Items**: [Count]

## Executive Summary
[3-4 sentences summarizing key findings and top priorities]

---

## Top 5 Priorities

### 1. [Priority Name] - Priority Score: 4.8/5
**What**: [Description of issue/request]

**Frequency**: ⭐⭐⭐⭐⭐ (mentioned by 45 users)
**Impact**: ⭐⭐⭐⭐⭐ (Critical to user success)
**Evidence Quality**: ⭐⭐⭐⭐ (Specific examples provided)
**Urgency**: ⭐⭐⭐⭐ (Causing churn risk)

**Who's Affected**: [Segment breakdown]
- Enterprise customers: 70%
- SMB customers: 30%

**Evidence**:
> "Direct quote 1" - Source: Interview #3
> "Direct quote 2" - Source: Survey Response #47
> "Direct quote 3" - Source: Support Ticket #892

**Recommendation**: [Specific action to take]

### 2-5. [Continue same format]

---

## Themes by Category

### Product Features (15 mentions)
- **Feature Request 1**: [Description] - [Count] mentions
- **Feature Request 2**: [Description] - [Count] mentions

### Usability Issues (23 mentions)
- **Issue 1**: [Description] - [Count] mentions
- **Issue 2**: [Description] - [Count] mentions

### Performance & Reliability (8 mentions)
- **Issue 1**: [Description] - [Count] mentions

### Pricing & Packaging (12 mentions)
- **Concern 1**: [Description] - [Count] mentions

---

## Segment Analysis

### Enterprise Customers
**Key Themes**:
1. [Theme with frequency]
2. [Theme with frequency]

**Unique Needs**: [What's different for this segment]

### SMB Customers
**Key Themes**:
1. [Theme with frequency]
2. [Theme with frequency]

**Unique Needs**: [What's different for this segment]

---

## Sentiment Analysis

**Overall Sentiment**: [Positive/Negative/Mixed]

**Positive Feedback** (35%):
- [What users love]
- [What's working well]

**Negative Feedback** (45%):
- [Key frustrations]
- [Major pain points]

**Neutral/Constructive** (20%):
- [Suggestions for improvement]

---

## Contradictions & Edge Cases

### Contradiction 1: [Description]
- **Segment A says**: [Feedback]
- **Segment B says**: [Opposite feedback]
- **Resolution**: [How to address both]

---

## Actionable Recommendations

### Immediate (This Sprint)
1. **[Action]**: [Why] - [Expected impact]
2. **[Action]**: [Why] - [Expected impact]

### Short-term (Next Month)
1. **[Action]**: [Why] - [Expected impact]
2. **[Action]**: [Why] - [Expected impact]

### Long-term (This Quarter)
1. **[Strategic initiative]**: [Why] - [Expected impact]
2. **[Strategic initiative]**: [Why] - [Expected impact]

---

## Next Steps

- [ ] Share this synthesis with [stakeholders]
- [ ] Prioritize top 3 items in roadmap
- [ ] Schedule follow-up research on [unclear items]
- [ ] Update feature specs based on findings
- [ ] Communicate decisions back to users

---

## Appendix: Data Summary

**Sources Breakdown**:
- Interviews: [Count]
- Surveys: [Count]
- Support Tickets: [Count]
- Reviews: [Count]
- Feature Requests: [Count]

**Time Period**: [Date range]
**Unique Users**: [Count]
```

## Example Usage

```bash
# Synthesize multiple interviews
> /pm/feedback-synthesis interviews/*.txt

# Synthesize mixed sources
> /pm/feedback-synthesis interviews/*.txt surveys/q1-2025.csv tickets/jan-*.txt

# Synthesize with focus area
> /pm/feedback-synthesis feedback/* "focus on pricing and packaging feedback"
```

## Tips

- Include diverse sources for richer synthesis
- Provide at least 3-5 sources for meaningful patterns
- Add metadata to files (date, segment, source) if possible
- Use with `/pm/feature-prioritization` for next step
