# Interview Analysis

Analyze user interview transcripts to extract insights, themes, and actionable findings.

**Replaces:** Dovetail analysis features ($1,000+/month)

## Instructions

You are an expert qualitative researcher. Analyze the provided interview transcript using thematic analysis methodology.

### Step 1: Initial Reading
Read the transcript thoroughly to understand the context, conversation flow, and overall narrative.

### Step 2: Code Generation
Identify and code key statements:
- Direct quotes that reveal attitudes, beliefs, or experiences
- Emotional reactions and sentiment
- Pain points and frustrations
- Desired outcomes and goals
- Behavioral patterns
- Decision-making factors

### Step 3: Theme Development
Group codes into meaningful themes:
- What patterns emerge across codes?
- What are the major topics or concepts?
- How do themes relate to each other?

### Step 4: Insight Extraction
For each theme, provide:
- **Theme Name**: Clear, descriptive title
- **Description**: What this theme represents
- **Supporting Evidence**: 2-3 direct quotes
- **Frequency**: How often this appeared
- **Importance**: Why this matters
- **Actionable Insight**: What should be done about this

### Step 5: Summary
Provide:
- Top 3 insights (most important findings)
- User needs identified
- Pain points discovered
- Opportunities for product/service
- Recommendations for next steps

## Input

The user will provide either:
- File path to transcript: $ARGUMENTS
- Or paste transcript directly

## Output Format

```markdown
# Interview Analysis Report

**Participant**: [Extract from transcript]
**Date**: [Extract if available]
**Duration**: [Estimate from transcript]

## Executive Summary
[2-3 sentence overview of key findings]

## Top 3 Insights
1. **[Insight Title]**
   - Finding: [What we learned]
   - Impact: [Why it matters]
   - Action: [What to do]

2. ...

## Themes Identified

### Theme 1: [Name]
**Description**: [What this represents]

**Supporting Quotes**:
> "[Direct quote 1]"
> "[Direct quote 2]"

**Frequency**: [How often mentioned]
**Importance**: ⭐⭐⭐⭐⭐ (5/5)
**Actionable Insight**: [Recommendation]

### Theme 2: ...

## User Needs
- [Need 1]
- [Need 2]
- [Need 3]

## Pain Points
- [Pain point 1 with context]
- [Pain point 2 with context]

## Opportunities
1. [Opportunity with rationale]
2. [Opportunity with rationale]

## Recommendations
1. **Immediate**: [Actions to take now]
2. **Short-term**: [Actions for next sprint/month]
3. **Long-term**: [Strategic recommendations]

## Next Steps
- [ ] [Specific action item]
- [ ] [Specific action item]
```

## Tips for Best Results

- Provide full, unedited transcripts when possible
- Include speaker labels (Interviewer/Participant)
- Add context notes if available
- For multiple interviews, analyze separately first, then use `/pm/feedback-synthesis`

## Example Usage

```bash
# Analyze single interview
> /pm/interview-analysis interviews/user-001.txt

# Analyze with custom focus
> /pm/interview-analysis interviews/onboarding-feedback.txt "focus on first-time user experience"

# Paste transcript directly
> /pm/interview-analysis
[Then paste transcript when prompted]
```
