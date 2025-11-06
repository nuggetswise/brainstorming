# PromptForge: Best Practices Guide

**Purpose:** Guide AI and Prompt Engineers on coding standards, quality requirements, and best practices for building PromptForge

**Audience:** Engineers working on PromptForge plugin development

**Scope:** Technical standards, not project management

---

## 📋 Project Context

PromptForge is a Claude Code plugin providing 70+ world-class PM prompts (PRIME 8.5+) with AI-powered enhancement.

**Key Components:**
- Plugin-based distribution (Claude Code marketplace or GitHub releases)
- Skills-first architecture (auto-activation)
- 2 specialized subagents (Prompt Enhancer + Prompt Researcher)
- 3 custom commands (/prompt-browse, /prompt-enhance, /prompt-score)
- 70 prompts across 6 categories (Strategy, Research, Execution, Analysis, Communication, Special Workflows)
- Two-tier system (plugin prompts + user customizations)

---

## 🎯 Coding Standards

### General Principles

1. **Markdown-First**
   - All plugin components written in Markdown (.md files)
   - YAML frontmatter for metadata
   - No JSON indices (single source of truth)
   - Git-friendly, human-readable

2. **Quality Over Quantity**
   - Every prompt must score 8.5+ on PRIME framework
   - Peer review required before merge
   - Test enhancement on all prompts
   - Document edge cases thoroughly

3. **User Experience First**
   - Skills auto-activate (proactive, not reactive)
   - Subagents preserve main conversation context
   - Error messages are helpful, not technical
   - Performance: <3 seconds per operation

4. **Privacy & Security**
   - All data stored locally
   - No telemetry without explicit opt-in
   - User prompts never sent to external services
   - Document data handling in README

5. **Conciseness in Prompts**
   - Target 200-300 lines for conversational prompts
   - Remove verbose examples and redundant explanations
   - Focus on clarity over comprehensiveness
   - One excellent example > multiple verbose examples

---

## 📐 PRIME Framework (Quality Standard)

**All prompts MUST be scored using PRIME framework before inclusion:**

```
PRIME Score = (P × 0.25) + (R × 0.20) + (I × 0.20) + (M × 0.15) + (E × 0.20)

P - Precision (25%): Instructions are unambiguous and specific
R - Richness (20%): Appropriate detail for task complexity
I - Instruction (20%): Explicit output format and success criteria
M - Metadata (15%): Target audience, prerequisites, and context
E - Examples (20%): Concrete examples demonstrating desired output
```

**Quality Thresholds:**
- 🏆 9.0-10.0 = WORLD-CLASS (P0 prompts, publish immediately)
- ⭐ 8.5-8.9 = EXCELLENT (P1 prompts, minor polish)
- ✅ 8.0-8.4 = GOOD (needs iteration)
- ⚠️ 7.0-7.9 = ACCEPTABLE (significant rework)
- ❌ <7.0 = REJECT (start over)

**Minimum for inclusion: 8.5 PRIME score**

### Why PRIME (Not CLEAR)?

Dr. Leo S. Lo published the "CLEAR Framework" in 2023 for teaching how to WRITE prompts to AI (Concise, Logical, Explicit, Adaptive, Reflective). To avoid confusion, we use PRIME to SCORE prompt quality.

**Using Both Frameworks:**
- **Lo's CLEAR:** Writing guidance when creating prompts
- **Our PRIME:** Quality scoring for library inclusion

*Credit: Lo, L. S. (2023). "The CLEAR path: A framework for enhancing information literacy through prompt engineering." Journal of Academic Librarianship, 49(4), 102720.*

---

## 🏗️ Architecture Conventions

### File Structure

```
promptforge-plugin/
├── .claude-plugin/
│   └── plugin.json              # MUST: Valid JSON, all components listed
├── skills/promptforge/
│   └── SKILL.md                 # MUST: Concise (200-250 lines), auto-activation triggers
├── agents/
│   ├── prompt-enhancer.md       # MUST: All 5 edge cases handled
│   └── prompt-researcher.md     # MUST: All 5 edge cases handled
├── commands/
│   ├── prompt-browse.md         # SHOULD: Interactive, user-friendly
│   ├── prompt-enhance.md        # SHOULD: Delegates to subagent
│   └── prompt-score.md          # SHOULD: Shows PRIME breakdown
├── prompts/product-management/
│   ├── 01-strategy/             # MUST: All P0 prompts ≥9.0 PRIME
│   ├── 02-research/             # MUST: All P0 prompts ≥9.0 PRIME
│   ├── 03-execution/            # MUST: All P0 prompts ≥9.0 PRIME
│   ├── 04-analysis/             # MUST: All P0 prompts ≥9.0 PRIME
│   ├── 05-communication/        # MUST: All P0 prompts ≥9.0 PRIME
│   └── 06-special-workflows/    # SHOULD: All P1 prompts ≥8.5 PRIME
└── docs/
    ├── QUALITY_STANDARDS.md     # MUST: PRIME framework explained
    ├── ENHANCEMENT_GUIDE.md     # MUST: How to customize prompts
    └── EXAMPLES.md              # SHOULD: Real usage examples
```

### Two-Tier Customization System

**Problem:** Plugin updates overwrite user customizations.

**Solution:**

**Tier 1: Plugin Prompts (Read-Only)**
```
~/.claude-code/plugins/promptforge/prompts/
├── feature-prioritization.md  ← Official version, gets updates
```

**Tier 2: User Customizations**
```
.claude/prompts/custom/
├── my-feature-prioritization.md  ← User version, safe from updates
```

**Skill Priority Logic:**
1. Check `.claude/prompts/custom/` first (user versions)
2. Fall back to `plugins/promptforge/prompts/` (official versions)
3. User versions override official

**Benefits:**
- ✅ User customizations survive plugin updates
- ✅ Users still receive official prompt updates
- ✅ Clear separation of concerns

### Naming Conventions

**Files:**
- Prompt files: `kebab-case.md` (e.g., `feature-prioritization.md`)
- Category directories: `01-category-name/` (numbered for order)
- Documentation: `SCREAMING_SNAKE_CASE.md` (e.g., `QUALITY_STANDARDS.md`)

**Frontmatter Fields:**
- `name`: Title Case (e.g., "Feature Prioritization")
- `category`: lowercase (e.g., "execution")
- `tags`: kebab-case array (e.g., `[prioritization, roadmap, strategy]`)

**Branch Names:**
- MUST start with `claude/` and end with session ID
- Format: `claude/descriptive-name-{sessionId}`

---

## ✅ Code Review Criteria

### For Prompt Files

**MUST have:**
- [ ] YAML frontmatter with all required fields
- [ ] PRIME score ≥8.5 documented
- [ ] 1-2 concrete examples (not 3-4)
- [ ] 200-300 lines total (conversational length)
- [ ] Explicit audience and context
- [ ] Defined output format and success criteria
- [ ] Framework references (RICE, JTBD, OKRs, etc.)
- [ ] Top 5 tips (not 10+)
- [ ] Common pitfalls section (2-3 key ones)

**SHOULD have:**
- [ ] Related prompts linked
- [ ] Step-by-step instructions
- [ ] Visual formatting (tables, bullets, headers)

**MUST NOT have:**
- [ ] Vague language ("good", "appropriate", "several")
- [ ] Lorem Ipsum or placeholder examples
- [ ] Unclear scope ("analyze data" without context)
- [ ] Missing metadata fields
- [ ] PRIME score <8.5
- [ ] Verbose examples (700-1000 lines)

### For Skill/Agent Files

**MUST have:**
- [ ] Clear activation/invocation triggers
- [ ] Concise (200-250 lines for Skills)
- [ ] All edge cases handled gracefully
- [ ] Fallback behavior defined
- [ ] Error messages are user-friendly
- [ ] 1 brief example interaction (not 4 detailed ones)

**SHOULD have:**
- [ ] Progress indicators for long operations
- [ ] Helpful suggestions when things go wrong
- [ ] Context preservation strategies

**MUST NOT have:**
- [ ] Extensive example dialogs (Skills are behavior specs, not documentation)
- [ ] Verbose style guides (keep concise)
- [ ] Redundant explanations

### For Documentation

**MUST have:**
- [ ] Clear, concise language (8th grade reading level)
- [ ] Code examples where applicable
- [ ] Up-to-date information
- [ ] Consistent formatting

**SHOULD have:**
- [ ] Quick start section (2-5 min)
- [ ] Troubleshooting guide
- [ ] Links to related docs

---

## 🛡️ Edge Case Handling

### Required Edge Cases (Must Handle)

**Prompt Enhancer (5 cases):**
1. Enhancement makes score worse → Show comparison, recommend original
2. Impossible combination → Explain conflict, suggest alternatives
3. User abandons mid-flow → Save state, allow resume
4. Already industry-specific → Explain optimization, offer other dimensions
5. Timeout (>2 min) → Chunk work, save partial results

**Prompt Researcher (5 cases):**
1. No results found → Suggest related, broader search, or enhancement
2. Too many results → Group by category, ask clarification
3. Vague request → Interactive Q&A to determine need
4. Unrelated comparison → Clarify intent, suggest logical alternatives
5. Handoff to enhancer → Detect context, delegate appropriately

**All edge cases MUST:**
- Detect condition before it becomes a problem
- Provide clear, actionable user response
- Offer 2-3 options (not just error message)
- Include fallback to safe default

---

## 🧪 Testing Standards

### Before Committing

**For Prompts:**
- [ ] Score calculated using PRIME framework
- [ ] Peer reviewed by other engineer
- [ ] Tested with real use case
- [ ] Enhancement works (if P0/P1 prompt)
- [ ] No spelling/grammar errors
- [ ] Length check (200-300 lines target)

**For Skills/Agents:**
- [ ] Manual testing with 3+ scenarios
- [ ] All 5 edge cases tested
- [ ] Performance <3 sec (or shows progress)
- [ ] Error handling verified
- [ ] Subagent delegation works correctly

**For Commands:**
- [ ] Interactive flow tested end-to-end
- [ ] Help text is clear
- [ ] Integration with skills/agents works
- [ ] Error messages are helpful

---

## 📝 Commit Message Format

### Structure
```
<type>: <short summary> (max 50 chars)

<detailed description>
- What changed
- Why it changed
- Any breaking changes
- Testing done
```

### Types
- `feat:` - New feature (prompt, command, etc.)
- `fix:` - Bug fix
- `docs:` - Documentation only
- `refactor:` - Code restructuring (no functionality change)
- `test:` - Adding or fixing tests
- `chore:` - Maintenance tasks

### Examples

**Good:**
```
feat: Add feature prioritization prompt (PRIME 9.2)

Created feature-prioritization.md with:
- RICE/ICE framework scoring
- B2B SaaS examples
- 233 lines (streamlined from 536)
- 9.2 PRIME score (peer reviewed)

Tested with real product roadmap scenario.
```

**Bad:**
```
added prompt

updated the files
```

---

## 🔄 Git Workflow

### Branch Strategy

**Feature Branches:**
- Name format: `claude/feature-name-{sessionId}`
- Push regularly (at least daily)
- Merge via pull request when complete

**Commits:**
- Commit frequently (every significant change)
- Write clear commit messages (see format above)
- Push at end of each day minimum

**Merging:**
- Requires peer review
- All tests must pass
- PRIME scores documented
- No merge conflicts

### Pull Request Template

```markdown
## Summary
[Brief description of changes]

## Type of Change
- [ ] New prompt (PRIME score: X.X)
- [ ] Skill/Agent improvement
- [ ] Documentation update
- [ ] Bug fix

## Testing
- [ ] Manual testing completed
- [ ] Edge cases verified
- [ ] Performance acceptable

## PRIME Score (if prompt)
- Precision: X/10
- Richness: X/10
- Instruction: X/10
- Metadata: X/10
- Examples: X/10
- **Total: X.X/10**

## Checklist
- [ ] Peer reviewed
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
- [ ] Commit messages follow format
```

---

## 📚 Documentation Standards

### Required Documentation

**For Each Prompt:**
- Inline documentation (via frontmatter and content sections)
- Quality score justification
- Enhancement test results

**For Skills/Agents:**
- Activation triggers documented
- Edge cases listed with handling
- Brief example interaction (1, not 4)
- Performance characteristics noted

**For Repository:**
- README.md (getting started, installation)
- QUALITY_STANDARDS.md (PRIME framework explained)
- ENHANCEMENT_GUIDE.md (how to customize)

### Documentation Style

**Tone:**
- Clear and concise
- Friendly but professional
- Action-oriented ("do this" not "you could do this")
- Assumes non-technical audience for user docs
- Assumes technical audience for contributor docs

**Formatting:**
- Use headers for structure (H1-H4)
- Use tables for comparisons
- Use code blocks for examples
- Use emoji sparingly (only for visual breaks)
- Use bullet points for lists
- Use checkboxes for tasks

---

## ⚠️ Common Pitfalls to Avoid

### For Prompts
❌ Vague adjectives ("good", "nice", "better", "appropriate")
❌ Unclear scope ("analyze some competitors")
❌ Missing examples or using Lorem Ipsum
❌ No audience context
❌ Undefined output format
❌ **Verbose prompts (700-1000 lines)**
✅ Specific, measurable, concrete instructions
✅ **Concise prompts (200-300 lines)**

### For Skills/Agents
❌ Assuming user intent without confirmation
❌ Cluttering main conversation context
❌ No fallback for edge cases
❌ Technical error messages
❌ **Extensive example dialogs (4 detailed examples)**
✅ Clear activation, isolated context, graceful handling
✅ **1 brief example interaction**

### For Documentation
❌ Outdated examples or screenshots
❌ Assuming too much prior knowledge
❌ No troubleshooting section
❌ Broken links to other docs
❌ Inconsistent formatting
✅ Current, accessible, helpful, linked

---

## 🎯 Definition of Done

### For a Prompt
- [ ] Written following template structure
- [ ] PRIME score ≥8.5 (calculated and peer reviewed)
- [ ] 200-300 lines (conversational length)
- [ ] 1-2 excellent examples (not 3-4 verbose ones)
- [ ] Tested with real use case
- [ ] Enhancement tested (improves score by ≥0.3)
- [ ] Committed with proper message
- [ ] Added to category README

### For a Skill/Agent
- [ ] All activation triggers documented
- [ ] 200-250 lines for Skills (not 500+)
- [ ] All 5 edge cases handled
- [ ] Manual testing completed (3+ scenarios)
- [ ] Performance acceptable (<3 sec or progress shown)
- [ ] 1 brief example documented (not 4 detailed)
- [ ] Committed with tests documented

### For Documentation
- [ ] Clear, concise language
- [ ] All links work
- [ ] Examples are current
- [ ] Follows formatting standards
- [ ] No spelling/grammar errors

---

## ✅ Pre-Commit Checklist

Before every commit:
- [ ] Code/content follows conventions above
- [ ] PRIME score documented (if prompt)
- [ ] Length check: 200-300 lines for prompts, 200-250 for Skills
- [ ] Edge cases handled (if skill/agent)
- [ ] Tested manually
- [ ] Documentation updated
- [ ] Commit message follows format
- [ ] No spelling/grammar errors
- [ ] No broken links

---

**Last Updated:** November 6, 2025
**Version:** 1.1 (Best Practices Focus)
**Purpose:** Guide AI and Prompt Engineers on technical standards
**Status:** ✅ Active Best Practices Guide
