# Quality Standards (Internal - Contributors Only)

**Audience:** Engineers and contributors building PromptForge
**Purpose:** Define objective quality criteria for prompt validation

---

## Overview

This document is for **internal use only** - not exposed to end users. All PromptForge prompts must meet quality standards measured by the PRIME framework.

**Minimum Threshold:** PRIME ≥8.5/10

---

## PRIME Framework (Internal Validation Only)

```
PRIME = (P × 0.25) + (R × 0.20) + (I × 0.20) + (M × 0.15) + (E × 0.20)

P - Precision (25%): Instructions unambiguous
R - Richness (20%): Appropriate detail
I - Instruction (20%): Explicit output format
M - Metadata (15%): Audience, prerequisites
E - Examples (20%): Concrete examples
```

**Thresholds (Internal Use):**
- 9.0-10.0 = World-class (P0)
- 8.5-8.9 = Excellent (P1)
- 8.0-8.4 = Good (needs iteration)
- <8.0 = Reject

---

## Scoring Dimensions

### Precision (25%)

**10/10:** Zero ambiguity, specific scope, no vague language
**7-9/10:** Mostly clear, minor vague areas
**4-6/10:** Some ambiguity, multiple interpretations
**1-3/10:** Very vague, unclear

**Avoid:** "good", "appropriate", "several", "some"
**Use:** Specific numbers, clear definitions

### Richness (20%)

**10/10:** Perfect detail balance, 200-300 lines
**7-9/10:** Good detail, minor gaps or slight verbosity
**4-6/10:** Too sparse or too verbose
**1-3/10:** Severely imbalanced

**Target:** 200-300 lines for most prompts

### Instruction (20%)

**10/10:** Exact output format, clear success criteria, steps provided
**7-9/10:** Good format guidance, mostly clear criteria
**4-6/10:** Some format guidance, incomplete
**1-3/10:** No clear output definition

**Required:** Template or structure examples

### Metadata (15%)

**10/10:** Complete (audience, prerequisites, context, time, difficulty)
**7-9/10:** Most metadata present
**4-6/10:** Some metadata, incomplete
**1-3/10:** Little to no metadata

### Examples (20%)

**10/10:** 1-2 excellent, concrete examples
**7-9/10:** Good examples, minor issues
**4-6/10:** Weak or generic examples
**1-3/10:** No examples or placeholders only

**No Lorem Ipsum!** Use realistic scenarios.

---

## User-Facing vs. Internal

**❌ Don't mention PRIME to users:**
- No "/prompt-score" command
- No "PRIME 9.2" in descriptions
- No score comparisons in enhancement output

**✅ Keep PRIME internal:**
- Quality validation during creation
- Peer review process
- Internal documentation only

**✅ Say instead (user-facing):**
- "High-quality, professionally curated"
- "Tested with real PM use cases"
- "Improved for your context"

---

## Validation Checklist

Before adding any prompt:

- [ ] PRIME score ≥8.5 (calculated internally)
- [ ] Peer reviewed
- [ ] No vague language
- [ ] Output format defined
- [ ] 1-2 concrete examples
- [ ] Target audience specified
- [ ] Prerequisites listed
- [ ] 200-300 lines
- [ ] Tested with real use case

---

**Note:** This framework is for quality control, not user communication. Users see "professionally curated" - we use PRIME internally to ensure that's true.

**Last Updated:** November 7, 2025
