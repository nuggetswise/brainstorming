# Feature Prioritization

Prioritize features using RICE, ICE, or custom scoring frameworks based on user feedback and business goals.

**Replaces:** Productboard prioritization ($70K/year), Aha! scoring ($7K/year)

## Instructions

You are an expert product manager skilled in feature prioritization frameworks.

### Step 1: Understand Context
Gather information about:
- Features to prioritize (from user input)
- Current product strategy
- Team capacity
- Business goals
- User feedback/requests

### Step 2: Gather Data
For each feature, collect:
- **Reach**: How many users will this impact?
- **Impact**: How much will it improve their experience?
- **Confidence**: How sure are we about reach and impact?
- **Effort**: How much work will this take?

### Step 3: Apply Framework

**RICE Scoring** (default):
- Reach: Number of users/period (e.g., 1000 users/quarter)
- Impact: 0.25 (minimal), 0.5 (low), 1 (medium), 2 (high), 3 (massive)
- Confidence: 50% (low), 80% (medium), 100% (high)
- Effort: Person-months (0.5, 1, 2, 5, 10)
- **RICE Score** = (Reach × Impact × Confidence) / Effort

**ICE Scoring** (simpler):
- Impact: 1-10 scale
- Confidence: 1-10 scale
- Ease: 1-10 scale
- **ICE Score** = (Impact + Confidence + Ease) / 3

### Step 4: Generate Priority Matrix
Create visual matrix showing:
- High Impact / Low Effort (Do First)
- High Impact / High Effort (Plan Carefully)
- Low Impact / Low Effort (Fill-ins)
- Low Impact / High Effort (Avoid)

### Step 5: Recommendations
Provide:
- Top 3-5 features to build next
- Rationale for prioritization
- Trade-offs considered
- Risk factors
- Success metrics

## Input

Provide features to prioritize:

**Option 1**: List features directly
```bash
/pm/feature-prioritization "Dark mode, Advanced filters, Export to PDF, Mobile app, API access"
```

**Option 2**: From feedback file
```bash
/pm/feature-prioritization --from feedback-synthesis.md
```

**Option 3**: Interactive (recommended)
```bash
/pm/feature-prioritization
[Claude will ask questions about each feature]
```

Arguments: $ARGUMENTS

## Output Format

```markdown
# Feature Prioritization Report

**Date**: [Today]
**Framework**: [RICE/ICE/Custom]
**Features Evaluated**: [Count]

## Executive Summary
Based on [framework] analysis, we recommend prioritizing [top features] because [rationale].

---

## Priority Matrix

### 🔥 Do First (High Impact, Low Effort)
1. **[Feature Name]** - RICE: 145
2. **[Feature Name]** - RICE: 98

### 📋 Plan Carefully (High Impact, High Effort)
1. **[Feature Name]** - RICE: 87
2. **[Feature Name]** - RICE: 72

### ⚡ Quick Wins (Low Impact, Low Effort)
1. **[Feature Name]** - RICE: 45
2. **[Feature Name]** - RICE: 38

### ⚠️ Avoid (Low Impact, High Effort)
1. **[Feature Name]** - RICE: 12
2. **[Feature Name]** - RICE: 8

---

## Detailed Scoring

### 1. [Feature Name] - RICE Score: 145 ⭐

**Description**: [What this feature does]

**Scoring**:
- **Reach**: 5,000 users/quarter
  - Rationale: [Why this many]
- **Impact**: 2.0 (High)
  - Rationale: [How it helps]
- **Confidence**: 80%
  - Rationale: [Evidence quality]
- **Effort**: 2 person-months
  - Rationale: [Complexity estimate]

**RICE Calculation**: (5,000 × 2.0 × 0.8) / 2 = 145

**User Evidence**:
> "Quote from user research"
> "Quote from support ticket"

**Business Impact**:
- Increase retention by [X]%
- Reduce churn in [segment]
- Enable upsell to [tier]

**Risks**:
- [Potential risk 1]
- [Potential risk 2]

**Success Metrics**:
- [Metric 1]: Target [X]
- [Metric 2]: Target [Y]

---

### 2-10. [Continue for all features]

---

## Recommended Roadmap

### Q1 2025 (Next 3 Months)
**Theme**: [Focus area]

**Must Have**:
1. ✅ [Feature] - RICE: 145 - 2 months
2. ✅ [Feature] - RICE: 98 - 1 month

**Should Have**:
3. [Feature] - RICE: 87 - If capacity allows

**Rationale**: [Why this ordering]

### Q2 2025
**Theme**: [Focus area]

1. [Feature] - RICE: 72
2. [Feature] - RICE: 68

---

## Trade-offs Considered

### Build [Feature A] vs [Feature B]?
**Decision**: Build [Feature A] first

**Reasoning**:
- Feature A has 2× the reach
- Feature B can wait until Q2
- Engineering prefers A (leverages existing work)

### Address Technical Debt?
**Decision**: Allocate 20% of Q1 to tech debt

**Reasoning**:
- Current debt slowing development by 15%
- Small investment now prevents bigger issues

---

## Assumptions & Risks

### Assumptions
1. [Assumption about reach]
2. [Assumption about effort]
3. [Assumption about impact]

### Risks
1. **High**: [Risk description]
   - Mitigation: [Strategy]
2. **Medium**: [Risk description]
   - Mitigation: [Strategy]

---

## Stakeholder Input

### From Engineering
- [Feedback on effort estimates]
- [Technical considerations]

### From Sales
- [Customer requests]
- [Deal blockers]

### From Support
- [Top support issues]
- [User pain points]

---

## Next Steps

- [ ] Review with leadership team
- [ ] Validate effort estimates with engineering
- [ ] Create specs for top 3 features
- [ ] Update roadmap in [tool]
- [ ] Communicate to stakeholders
- [ ] Set up success metrics tracking

---

## Appendix: Scoring Framework Details

**RICE Framework**:
- Reach: # users impacted per time period
- Impact: 0.25 (minimal), 0.5 (low), 1 (medium), 2 (high), 3 (massive)
- Confidence: 50% (low), 80% (medium), 100% (high)
- Effort: Person-months or story points

**When to Use RICE**:
- Comparing features across different areas
- Need quantitative justification
- Have usage data available

**When to Use ICE**:
- Quick prioritization needed
- Limited data available
- Early-stage products
```

## Example Usage

```bash
# Quick prioritization
> /pm/feature-prioritization "Dark mode, SSO, API rate limiting, Bulk actions"

# From synthesis file
> /pm/feature-prioritization --from feedback-synthesis.md

# Interactive (recommended for first use)
> /pm/feature-prioritization
```

## Tips

- Be honest about confidence levels (avoid overconfidence)
- Include engineering in effort estimates
- Revisit priorities monthly
- Track actual vs estimated effort for learning
- Consider strategic value beyond RICE score
- Don't ignore high-effort, high-impact features (plan for them)
