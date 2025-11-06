# PromptForge: Claude Code Configuration

**Project:** PromptForge - Product Manager Prompt Library with AI Enhancement
**Status:** Sprint 0 - Implementation Ready
**Team:** Prompt Engineer + AI Engineer
**Timeline:** 8.5 weeks (14-day Sprint 0 + 6-week implementation)

---

## 📋 Project Overview

PromptForge is a Claude Code plugin providing 70+ world-class PM prompts (CLEAR 8.5+) with AI-powered enhancement that adapts prompts to user's industry, company stage, and team context.

**Key Components:**
- Plugin-based distribution (official Claude Code marketplace)
- Skills-first architecture (auto-activation)
- 2 specialized subagents (Prompt Enhancer + Prompt Researcher)
- 3 custom commands (/prompt-browse, /prompt-enhance, /prompt-score)
- 70 prompts across 6 categories (Strategy, Research, Execution, Analysis, Communication, Special Workflows)

---

## 🎯 Coding Standards

### General Principles

1. **Markdown-First**
   - All plugin components written in Markdown (.md files)
   - YAML frontmatter for metadata
   - No JSON indices (single source of truth)
   - Git-friendly, human-readable

2. **Quality Over Quantity**
   - Every prompt must score 8.5+ on CLEAR framework
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

---

## 📐 CLEAR Framework (Quality Standard)

**All prompts MUST be scored using CLEAR framework before inclusion:**

```
CLEAR Score = (C × 0.25) + (L × 0.20) + (E × 0.20) + (A × 0.15) + (R × 0.20)

C - Clarity (25%): Instructions are unambiguous and specific
L - Length (20%): Appropriate detail for task complexity
E - Examples (20%): Concrete examples illustrate desired output
A - Audience (15%): Target user and context explicit
R - Result (20%): Desired output format and success criteria defined
```

**Quality Thresholds:**
- 🏆 9.0-10.0 = WORLD-CLASS (P0 prompts, publish immediately)
- ⭐ 8.5-8.9 = EXCELLENT (P1 prompts, minor polish)
- ✅ 8.0-8.4 = GOOD (needs iteration)
- ⚠️ 7.0-7.9 = ACCEPTABLE (significant rework)
- ❌ <7.0 = REJECT (start over)

**Minimum for inclusion: 8.5 CLEAR score**

---

## 🏗️ Architecture Conventions

### File Structure

```
promptforge-plugin/
├── .claude-plugin/
│   └── plugin.json              # MUST: Valid JSON, all components listed
├── skills/promptforge/
│   └── SKILL.md                 # MUST: Auto-activation triggers defined
├── agents/
│   ├── prompt-enhancer.md       # MUST: All 5 edge cases handled
│   └── prompt-researcher.md     # MUST: All 5 edge cases handled
├── commands/
│   ├── prompt-browse.md         # SHOULD: Interactive, user-friendly
│   ├── prompt-enhance.md        # SHOULD: Delegates to subagent
│   └── prompt-score.md          # SHOULD: Shows CLEAR breakdown
├── prompts/product-management/
│   ├── 01-strategy/             # MUST: All P0 prompts ≥9.0 CLEAR
│   ├── 02-research/             # MUST: All P0 prompts ≥9.0 CLEAR
│   ├── 03-execution/            # MUST: All P0 prompts ≥9.0 CLEAR
│   ├── 04-analysis/             # MUST: All P0 prompts ≥9.0 CLEAR
│   ├── 05-communication/        # MUST: All P0 prompts ≥9.0 CLEAR
│   └── 06-special-workflows/    # SHOULD: All P1 prompts ≥8.5 CLEAR
└── docs/
    ├── QUALITY_STANDARDS.md     # MUST: CLEAR framework explained
    ├── ENHANCEMENT_GUIDE.md     # MUST: How to customize prompts
    └── EXAMPLES.md              # SHOULD: Real usage examples
```

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
- Example: `claude/review-product-plan-011CUr1GxHrvVy5WmuZEyQov`

---

## ✅ Code Review Criteria

### For Prompt Files

**MUST have:**
- [ ] YAML frontmatter with all required fields
- [ ] CLEAR score ≥8.5 documented
- [ ] At least 2 concrete examples
- [ ] Explicit audience and context
- [ ] Defined output format and success criteria
- [ ] Framework references (RICE, JTBD, OKRs, etc.)
- [ ] Tips & common pitfalls section
- [ ] Customization options described

**SHOULD have:**
- [ ] Related prompts linked
- [ ] Multiple scenarios shown in examples
- [ ] Step-by-step instructions
- [ ] Visual formatting (tables, bullets, headers)

**MUST NOT have:**
- [ ] Vague language ("good", "appropriate", "several")
- [ ] Lorem Ipsum or placeholder examples
- [ ] Unclear scope ("analyze data" without context)
- [ ] Missing metadata fields
- [ ] CLEAR score <8.5

### For Skill/Agent Files

**MUST have:**
- [ ] Clear activation/invocation triggers
- [ ] All edge cases handled gracefully
- [ ] Fallback behavior defined
- [ ] Error messages are user-friendly
- [ ] Performance considerations documented
- [ ] Example interactions shown

**SHOULD have:**
- [ ] Progress indicators for long operations
- [ ] Helpful suggestions when things go wrong
- [ ] Context preservation strategies
- [ ] Testing scenarios documented

### For Documentation

**MUST have:**
- [ ] Clear, concise language (8th grade reading level)
- [ ] Code examples where applicable
- [ ] Screenshots or diagrams (if helpful)
- [ ] Up-to-date information
- [ ] Consistent formatting

**SHOULD have:**
- [ ] Quick start section (2-5 min)
- [ ] Troubleshooting guide
- [ ] FAQ for common questions
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
- Log for debugging (if applicable)

---

## 🧪 Testing Standards

### Before Committing

**For Prompts:**
- [ ] Score calculated using CLEAR framework
- [ ] Peer reviewed by other engineer
- [ ] Tested with real use case
- [ ] Enhancement works (if P0/P1 prompt)
- [ ] No spelling/grammar errors

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

### Sprint 0 Success Criteria

- [ ] Plugin installs successfully (>95% success rate)
- [ ] Skill auto-activates appropriately
- [ ] Enhancement improves CLEAR scores by +0.3 avg
- [ ] Search finds relevant prompts (>80% accuracy)
- [ ] All 10 edge cases handled gracefully
- [ ] 3 prompts migrated and scored (CLEAR ≥9.0)
- [ ] Zero critical bugs

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

<optional footer with issue references>
```

### Types
- `feat:` - New feature (prompt, command, etc.)
- `fix:` - Bug fix
- `docs:` - Documentation only
- `refactor:` - Code restructuring (no functionality change)
- `test:` - Adding or fixing tests
- `chore:` - Maintenance tasks
- `perf:` - Performance improvements

### Examples

**Good:**
```
feat: Add feature prioritization prompt (CLEAR 9.2)

Created feature-prioritization.md with:
- RICE/ICE framework scoring
- B2B SaaS examples
- Priority matrix visualization
- 9.2 CLEAR score (peer reviewed)

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

**Current Default Branch:** `claude/review-product-plan-011CUr1GxHrvVy5WmuZEyQov`
- This is the clean, Sprint 0-ready branch
- Contains: 7 core docs + archive/ with 19 legacy files
- Should be set as default on GitHub (Settings → Branches)

**Feature Branches:**
- Create from current default branch
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
- CLEAR scores documented
- No merge conflicts

### Pull Request Template

```markdown
## Summary
[Brief description of changes]

## Type of Change
- [ ] New prompt (CLEAR score: X.X)
- [ ] Skill/Agent improvement
- [ ] Documentation update
- [ ] Bug fix

## Testing
- [ ] Manual testing completed
- [ ] Edge cases verified
- [ ] Performance acceptable

## CLEAR Score (if prompt)
- Clarity: X/10
- Length: X/10
- Examples: X/10
- Audience: X/10
- Result: X/10
- **Total: X.X/10**

## Checklist
- [ ] Peer reviewed
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
- [ ] Commit messages follow format
```

---

## 📚 Documentation Requirements

### Required Documentation

**For Each Prompt:**
- Inline documentation (via frontmatter and content sections)
- Quality score justification
- Enhancement test results

**For Skills/Agents:**
- Activation triggers documented
- Edge cases listed with handling
- Example interactions shown
- Performance characteristics noted

**For Repository:**
- README.md (Sprint 0 focus, getting started)
- QUALITY_STANDARDS.md (CLEAR framework explained)
- ENHANCEMENT_GUIDE.md (how to customize)
- PROMPTFORGE_PRODUCT_PLAN_V2.md (definitive plan)
- Sprint 0 guides (kickoff, tasks, onboarding, quick ref, repo template)

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

## 🚀 Sprint 0 Specific Rules

### Days 1-7 (Week 1)

**AI Engineer Focus:**
- Repository setup and structure
- plugin.json configuration
- PromptForge Skill (browse, load, search modes)
- Category READMEs
- Basic testing framework

**Prompt Engineer Focus:**
- Prompt template design
- QUALITY_STANDARDS.md
- Enhancement templates
- Migrate 3 existing prompts
- Score all 3 using CLEAR

### Days 8-14 (Week 2)

**AI Engineer Focus:**
- Prompt Enhancer subagent + 5 edge cases
- Prompt Researcher subagent + 5 edge cases
- 3 custom commands
- Integration testing

**Prompt Engineer Focus:**
- Enhancement quality testing
- Search test cases
- Command documentation
- User workflow documentation

### Daily Standup Format

```
What I completed yesterday:
- [Specific accomplishment]
- [Specific accomplishment]

What I'm doing today:
- [Specific task from sprint plan]
- [Specific task from sprint plan]

Blockers:
- [Specific blocker] or "None"
```

---

## ⚠️ Common Pitfalls to Avoid

### For Prompts
❌ Vague adjectives ("good", "nice", "better", "appropriate")
❌ Unclear scope ("analyze some competitors")
❌ Missing examples or using Lorem Ipsum
❌ No audience context
❌ Undefined output format
✅ Specific, measurable, concrete instructions

### For Skills/Agents
❌ Assuming user intent without confirmation
❌ Cluttering main conversation context
❌ No fallback for edge cases
❌ Technical error messages
❌ No progress indicators for long operations
✅ Clear activation, isolated context, graceful handling

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
- [ ] CLEAR score ≥8.5 (calculated and peer reviewed)
- [ ] Tested with real use case
- [ ] Enhancement tested (improves score by ≥0.3)
- [ ] Committed with proper message
- [ ] Added to category README

### For a Skill/Agent
- [ ] All activation triggers documented
- [ ] All 5 edge cases handled
- [ ] Manual testing completed (3+ scenarios)
- [ ] Performance acceptable (<3 sec or progress shown)
- [ ] Example interactions documented
- [ ] Committed with tests documented

### For Sprint 0
- [ ] Plugin installs locally without errors
- [ ] Skill auto-activates on PM-related requests
- [ ] Enhancement improves 3 test prompts by +0.3 avg
- [ ] Search returns relevant results >80% of time
- [ ] All 10 edge cases handled gracefully
- [ ] 3 prompts migrated (interview-analysis, feature-prioritization, feedback-synthesis)
- [ ] Demo successful in Sprint 0 retrospective
- [ ] Zero critical bugs
- [ ] All documentation complete

---

## 🔧 Tools & Resources

### Required Tools
- Git (version control)
- Text editor (VS Code recommended)
- Claude Code (for testing)
- Markdown linter (optional but recommended)

### Key Resources
- **Product Plan:** PROMPTFORGE_PRODUCT_PLAN_V2.md
- **Onboarding:** PROMPTFORGE_TEAM_ONBOARDING.md
- **Sprint Tasks:** PROMPTFORGE_SPRINT0_TASKS.md
- **Quick Ref:** PROMPTFORGE_QUICK_REFERENCE.md
- **Setup:** PROMPTFORGE_REPO_TEMPLATE.md
- **Claude Code Docs:** https://code.claude.com/docs/en/plugin-marketplaces

### Sprint 0 Schedule
- **Day 1:** Kickoff + setup
- **Day 7:** Mid-sprint review
- **Day 14:** Demo + retrospective
- **Daily:** 15-min standup (same time every day)

---

## 📞 Getting Help

### Blockers
1. Try to solve independently (30 min)
2. Ask teammate for help (30 min)
3. Research documentation (30 min)
4. Escalate to Product Lead
5. Consider scope adjustment if critical

### Questions
- Technical: Pair with other engineer
- Product: Check Product Plan v2.0
- Process: Check Sprint 0 guides
- Urgent: Escalate to Product Lead

---

## ✅ Pre-Commit Checklist

Before every commit:
- [ ] Code/content follows conventions above
- [ ] CLEAR score documented (if prompt)
- [ ] Edge cases handled (if skill/agent)
- [ ] Tested manually
- [ ] Documentation updated
- [ ] Commit message follows format
- [ ] No spelling/grammar errors
- [ ] No broken links

---

**Last Updated:** November 6, 2025
**Version:** 1.0 (Sprint 0)
**Owner:** Product Team
**Status:** ✅ Active Configuration
