# PromptForge: Best Practices Alignment Analysis
**Comparing our MVP plan against Claude Code plugin best practices**
**Date:** November 5, 2025

---

## Key Claude Code Best Practices (2025)

### 1. **Architecture Options**

**Slash Commands:**
- Simple markdown files in `.claude/commands/`
- User-invoked (type `/command-name`)
- Good for: Repeated workflows, templates, guided processes
- Example: `/prompt-save`, `/prompt-list`

**Skills:**
- More powerful, placed in `.claude/skills/`
- **Model-invoked** (Claude autonomously uses based on context)
- Include `SKILL.md` file per skill
- Good for: Background capabilities Claude should always have
- Example: A skill that automatically detects when user is working with prompts

**MCP Servers:**
- Full TypeScript/Python tools
- External API calls, complex logic, performance-critical
- Good for: Heavy computation, external integrations
- Example: Vector database for semantic search

### 2. **File Structure Best Practices**

```
your-project/
├── .claude/
│   ├── claude.md              # Project context (what Claude should know)
│   ├── commands/              # User-invoked slash commands
│   │   ├── command1.md
│   │   └── command2.md
│   ├── skills/                # Model-invoked capabilities
│   │   └── skill-name/
│   │       └── SKILL.md
│   ├── data/                  # Local data storage (gitignored)
│   │   └── app-data.json
│   └── prompts/               # Stored prompts (user content)
└── README.md
```

### 3. **Command Design Best Practices**

**Frontmatter:**
```yaml
---
description: One-line description (shows in slash menu)
---
```

**Command Structure:**
1. Clear role statement ("You are helping the user...")
2. Step-by-step instructions
3. Examples (show expected format)
4. Suggest next steps (guide user journey)
5. Use $ARGUMENTS for parameters

**Data Storage:**
- Store in `.claude/data/` (gitignored)
- Use JSON for structured data
- Keep prompts as markdown files (git-friendly)

---

## Our Current Plan Analysis

### ✅ What We're Doing RIGHT

#### 1. **Correct File Structure**
Our plan uses proper structure:
```
promptforge/
├── .claude/
│   ├── commands/
│   │   ├── prompt-save.md      ✅ Correct location
│   │   ├── prompt-list.md      ✅ Correct location
│   │   ├── prompt-load.md      ✅ Correct location
│   ├── data/
│   │   └── prompts.json        ✅ Gitignored data
│   └── prompts/
│       └── (user prompts)      ✅ Git-friendly markdown
```

#### 2. **Following Command Conventions**
- ✅ Using frontmatter with `description`
- ✅ Clear step-by-step instructions
- ✅ Providing examples
- ✅ Suggesting next steps

#### 3. **Local-First Data Storage**
- ✅ All data in `.claude/data/` (proper location)
- ✅ Prompts as markdown files (git-friendly)
- ✅ JSON for indexing (searchable)

#### 4. **Git-Friendly Design**
- ✅ Markdown files can be version controlled
- ✅ Data directory gitignored
- ✅ No binary formats

---

## ⚠️ GAPS: What We're MISSING

### Gap 1: No `claude.md` Project Context File

**What it is:**
A `claude.md` file tells Claude about the project, available commands, and how things work.

**Why we need it:**
Without it, Claude has to figure out PromptForge structure every time. With it, Claude knows:
- What PromptForge is
- Where data is stored
- How commands work together
- Data schema/format

**Example `.claude/claude.md` we should add:**

```markdown
# PromptForge

A personal AI prompt management tool. Save, version, test, and improve your prompts.

## Data Structure

**Prompt Index:** `.claude/data/prompts.json`
```json
{
  "prompts": [
    {
      "name": "email-campaign",
      "category": "marketing",
      "description": "Write email campaigns",
      "tags": ["email", "marketing"],
      "created": "2025-11-05",
      "version": "1.2",
      "clear_score": 8.5
    }
  ]
}
```

**Prompt Files:** `.claude/prompts/{name}.md`
- Markdown files with YAML frontmatter
- Includes metadata (name, category, tags, version)
- Content is the prompt text

**Version History:** `.claude/data/prompt-history.json`
- Tracks all versions of each prompt
- Used by /prompt-history and /prompt-compare

## Available Commands

- `/prompt-save` - Save a new prompt
- `/prompt-list` - View all saved prompts
- `/prompt-load <name>` - Load a specific prompt
- `/prompt-search <query>` - Search prompts
- `/prompt-delete <name>` - Delete a prompt
- `/prompt-edit <name>` - Edit a saved prompt
- `/prompt-history <name>` - View version history
- `/prompt-compare <name> v1 v2` - Compare versions
- `/prompt-test <name>` - Test a prompt
- `/prompt-score <name>` - Get quality score

## When Working With Prompts

- Auto-version on every save (increment version number)
- Calculate CLEAR score automatically
- Store full version history
- Preserve metadata across versions
```

**Impact:** HIGH - This makes all commands work better together

---

### Gap 2: Should We Use Skills Instead of Some Commands?

**The Question:**
Some of our features might work better as **Skills** (model-invoked) rather than slash commands (user-invoked).

**Current Plan (All Slash Commands):**
- `/prompt-save` - User types this
- `/prompt-score` - User types this
- `/prompt-test` - User types this

**Alternative (Skills for Background Intelligence):**

**Skill: "Prompt Quality Assistant"**
- Claude automatically detects when user is writing/editing a prompt
- Proactively suggests: "This looks like a prompt. Want to save it with /prompt-save?"
- Auto-scores prompts in the background
- Surfaces quality issues without being asked

**Example `.claude/skills/prompt-quality-assistant/SKILL.md`:**

```markdown
# Prompt Quality Assistant

You are a background assistant that helps users improve their prompts.

## When to Activate

Detect when the user is:
- Writing a long, structured instruction to Claude
- Editing a file in .claude/prompts/
- Asking "is this prompt good?"
- Struggling with prompt quality

## What to Do

1. **Proactive Saving:**
   If user writes a good prompt (100+ words, clear instructions):
   > "That's a well-structured prompt! Want to save it? Run /prompt-save"

2. **Quality Feedback:**
   If user asks about prompt quality:
   - Quickly analyze using CLEAR framework
   - Suggest specific improvements
   - Offer to run /prompt-score for detailed analysis

3. **Version Reminders:**
   If user is editing a saved prompt:
   > "Editing email-campaign (v1.2). Your changes will be saved as v1.3"

## Don't

- Don't interrupt focused work
- Don't score every message (only actual prompts)
- Don't be pushy about saving
```

**Pros of Skills Approach:**
- ✅ More seamless UX (Claude helps proactively)
- ✅ Users don't need to remember all commands
- ✅ Feels more "AI native"

**Cons:**
- ⚠️ More complex to build
- ⚠️ Harder to test/debug
- ⚠️ Can be annoying if too aggressive

**Recommendation:**
- **MVP (Week 1-2):** Start with slash commands only (simpler, testable)
- **V2 (Month 2):** Add a prompt quality skill for proactive help

---

### Gap 3: Missing `$ARGUMENTS` for Parameters

**Current Plan:**
```bash
/prompt-load code-review     # Hardcoded in command
```

**Best Practice (Use $ARGUMENTS):**

**File: `.claude/commands/prompt-load.md`**
```markdown
---
description: Load a specific prompt by name
---

You are loading a saved prompt for the user.

## Steps:

1. **Get the prompt name:**
   - If provided via $ARGUMENTS, use that: `$ARGUMENTS`
   - If not provided, ask: "Which prompt do you want to load?"

2. **Load the prompt:**
   - Read `.claude/prompts/$ARGUMENTS.md`
   - If not found, list available prompts and ask again

3. **Display the prompt:**
   Show the full prompt content with metadata:
   ```
   Prompt: $ARGUMENTS (v1.2, CLEAR: 8.5)
   ════════════════════════════════════

   [prompt content here]

   ════════════════════════════════════
   Copy the prompt above to use it!
   ```

4. **Suggest next steps:**
   - `/prompt-test $ARGUMENTS` - Test this prompt
   - `/prompt-edit $ARGUMENTS` - Edit this prompt
```

**Impact:** MEDIUM - Cleaner UX, follows best practices

---

### Gap 4: No README.md at Project Root

**Current Plan:**
Has README in `/home/user/brainstorming/examples/promptforge-demo/README.md`

**Best Practice:**
Should be at **project root** (`/home/user/brainstorming/promptforge/README.md`)

**Why:**
- First thing users see on GitHub
- Installation instructions
- Quick start guide

**Impact:** HIGH - Critical for GitHub launch

---

### Gap 5: Should Testing Be MCP vs Slash Command?

**Current Plan:**
`/prompt-test` as a slash command

**Alternative:**
If testing becomes complex (running many variations, statistical analysis), consider MCP server.

**When to use MCP:**
- Need to call external APIs (e.g., vector database for embeddings)
- Performance-critical (running 50+ test cases in parallel)
- Complex computation (Bayesian A/B testing)

**When to stick with slash commands:**
- Simple testing (3-5 test cases, synchronous)
- No external dependencies
- Fast enough with Claude API

**Recommendation for MVP:**
- ✅ Start with slash command (simpler)
- ⚠️ If testing is slow or hits API rate limits, consider MCP in V2

**Impact:** LOW (for MVP) - Can defer to V2

---

## Revised MVP Plan (Aligned with Best Practices)

### Week 1: Core Commands + Context

#### Day 1: Project Setup (REVISED)
**Tasks:**
- [ ] Create proper project structure:
  ```
  promptforge/
  ├── .claude/
  │   ├── claude.md           # NEW: Project context
  │   ├── commands/
  │   ├── data/ (.gitignore)
  │   └── prompts/
  ├── README.md               # NEW: At root
  └── .gitignore
  ```
- [ ] Write `claude.md` with project context (data schema, commands, how it works)
- [ ] Create `/prompt-save` command (with $ARGUMENTS support)
- [ ] Create `/prompt-list` command
- [ ] Test: User can save and list prompts

**Owner:** PM (claude.md, README) + AI/ML Eng (commands)
**Success Criteria:** claude.md clearly explains PromptForge to Claude

---

#### Day 2: Load, Search, Delete (REVISED)
**Tasks:**
- [ ] Implement `/prompt-load <name>` with $ARGUMENTS
- [ ] Implement `/prompt-search <query>` with $ARGUMENTS
- [ ] Implement `/prompt-delete <name>` with $ARGUMENTS and confirmation
- [ ] Update claude.md with new commands
- [ ] Test: Full CRUD workflow

**Owner:** AI/ML Eng
**Success Criteria:** All commands use $ARGUMENTS correctly

---

#### Day 3-5: (Same as original plan)

---

### Week 2: AI Features + Consider Skills

#### Day 6-8: (Same as original plan)

#### Day 9: Evaluate Skills vs Commands (NEW)
**Tasks:**
- [ ] User test MVP with 3 people
- [ ] Observe: Do they forget to use /prompt-score? (Indicator for skill)
- [ ] Decide: Should we add a "Prompt Quality Assistant" skill for V2?
- [ ] Document findings

**Owner:** PM (user testing)
**Success Criteria:** Clear decision on skills for V2

---

#### Day 10: Polish + Documentation
**Tasks:**
- [ ] Ensure README.md is at project root (not in demo folder)
- [ ] Verify claude.md is comprehensive
- [ ] All commands have good descriptions
- [ ] Demo video
- [ ] Launch blog post

---

## Recommended Changes Summary

### MUST DO (Before MVP Launch):

1. **Add `claude.md` at `.claude/claude.md`**
   - Impact: HIGH
   - Effort: 2 hours
   - Why: Claude understands PromptForge context better

2. **Use `$ARGUMENTS` in commands**
   - Impact: MEDIUM
   - Effort: 1 hour
   - Why: Follows best practices, cleaner UX

3. **Move README.md to project root**
   - Impact: HIGH
   - Effort: 10 minutes
   - Why: Critical for GitHub launch

4. **Add .gitignore for `.claude/data/`**
   - Impact: MEDIUM
   - Effort: 5 minutes
   - Why: Don't commit user data to git

### NICE TO HAVE (Can defer to V2):

5. **Consider Skills for proactive help**
   - Impact: LOW (for MVP)
   - Effort: 4-6 hours
   - Why: Better UX but not critical for launch
   - Decision: Test MVP first, add in V2 if users struggle

6. **Evaluate MCP for testing**
   - Impact: LOW (for MVP)
   - Effort: 1-2 days
   - Why: Only needed if testing is slow/complex
   - Decision: Start with slash commands, migrate to MCP if needed

---

## Updated File Structure (Best Practices Aligned)

```
promptforge/
├── .claude/
│   ├── claude.md                    # NEW: Project context for Claude
│   ├── commands/
│   │   ├── prompt-save.md          # UPDATED: Use $ARGUMENTS
│   │   ├── prompt-list.md
│   │   ├── prompt-load.md          # UPDATED: Use $ARGUMENTS
│   │   ├── prompt-search.md        # UPDATED: Use $ARGUMENTS
│   │   ├── prompt-delete.md        # UPDATED: Use $ARGUMENTS
│   │   ├── prompt-edit.md          # UPDATED: Use $ARGUMENTS
│   │   ├── prompt-history.md       # UPDATED: Use $ARGUMENTS
│   │   ├── prompt-compare.md       # UPDATED: Use $ARGUMENTS
│   │   ├── prompt-test.md          # UPDATED: Use $ARGUMENTS
│   │   └── prompt-score.md         # UPDATED: Use $ARGUMENTS
│   ├── skills/                     # NEW: For V2 (optional)
│   │   └── prompt-quality-assistant/
│   │       └── SKILL.md
│   ├── data/                       # User data (gitignored)
│   │   ├── prompts.json
│   │   └── prompt-history.json
│   └── prompts/                    # User prompts (git-friendly)
│       ├── seed/                   # Our 10 seed prompts
│       │   ├── prd-template.md
│       │   ├── email-campaign.md
│       │   └── ...
│       └── (user prompts saved here)
├── README.md                        # MOVED: From demo folder to root
├── .gitignore                       # NEW: Ignore .claude/data/
└── LICENSE                          # NEW: MIT license
```

---

## Comparison: Before vs After Best Practices

### Before (Original Plan)

```
✅ Commands in right location
✅ Data storage approach
❌ No claude.md (Claude doesn't understand context)
❌ No $ARGUMENTS (hardcoded parameters)
❌ README in wrong location
❌ No .gitignore for data
❌ No consideration of skills vs commands
```

### After (Best Practices Aligned)

```
✅ Commands in right location
✅ Data storage approach
✅ claude.md explains project context
✅ $ARGUMENTS for parameters
✅ README at project root
✅ .gitignore for user data
✅ Evaluated skills (deferred to V2)
✅ Considered MCP (slash commands sufficient for MVP)
```

---

## Key Insights from Best Practices Research

### 1. **Plugins = Commands + Skills + MCP + Hooks**
Full Claude Code plugins bundle multiple capabilities:
- **Commands:** User-invoked workflows (what we're building)
- **Skills:** Model-invoked background intelligence (V2 consideration)
- **MCP Servers:** External tools/APIs (if needed later)
- **Hooks:** React to events (future feature)

**Our MVP:** Focus on commands only (simplest, most testable)

### 2. **Context is King**
The `claude.md` file is critical:
- Claude reads it to understand your project
- Prevents re-explaining structure every time
- Can be hierarchical (project-level, directory-level)

**Impact:** Without claude.md, every command has to re-explain how PromptForge works

### 3. **Slash Commands = Controlled Prompt Injections**
Commands are essentially "pre-written prompts that get injected"
- Keep them focused and scoped
- Use clear role statements
- Provide examples
- Guide the user journey (suggest next steps)

**Our approach already does this well!**

### 4. **Skills are Powerful but Complex**
Skills let Claude proactively help:
- "I notice you're writing a prompt, want to save it?"
- Background quality scoring
- Automatic versioning reminders

**Trade-off:**
- ✅ Better UX (seamless, proactive)
- ❌ Harder to build/test
- ❌ Can be annoying if too aggressive

**Our decision:** Test MVP with commands first, add skills in V2 if users struggle

---

## Final Recommendation

### APPROVED: Our plan is 90% aligned with best practices! ✅

**What to change before starting Day 1:**

1. ✅ **Add claude.md** (2 hours) - MUST DO
2. ✅ **Use $ARGUMENTS in all commands** (1 hour) - MUST DO
3. ✅ **Move README to root** (10 minutes) - MUST DO
4. ✅ **Add .gitignore** (5 minutes) - MUST DO

**Total additional work:** ~3-4 hours (worth it for best practices alignment)

**What to defer to V2:**

1. ⏳ Skills for proactive help (evaluate after MVP launch)
2. ⏳ MCP server for testing (only if needed for performance)

---

## Updated Day 1 Plan (Best Practices Aligned)

### Day 1 (Revised): Project Setup + Core Commands

**Morning (4 hours):**

1. **Create proper structure** (30 min)
   ```bash
   mkdir -p promptforge/.claude/{commands,data,prompts/seed}
   cd promptforge
   ```

2. **Write `.claude/claude.md`** (90 min)
   - Explain what PromptForge is
   - Document data schema (prompts.json, prompt files)
   - List all commands
   - Show examples

3. **Write `README.md` at root** (60 min)
   - What is PromptForge?
   - Installation
   - Quick start
   - Commands reference

4. **Create `.gitignore`** (5 min)
   ```
   .claude/data/
   .claude/prompts/*
   !.claude/prompts/seed/
   ```

**Afternoon (4 hours):**

5. **Implement `/prompt-save`** (90 min)
   - Use $ARGUMENTS for optional name
   - Save to .claude/prompts/{name}.md
   - Update .claude/data/prompts.json
   - Auto-version (v1.0)

6. **Implement `/prompt-list`** (60 min)
   - Read prompts.json
   - Format as table
   - Suggest next steps

7. **Test full workflow** (30 min)
   - Save a prompt
   - List it
   - Verify claude.md helps Claude understand

**Success Criteria:**
- ✅ claude.md clearly explains PromptForge
- ✅ User can save and list prompts
- ✅ README is clear for new users
- ✅ Data is gitignored correctly

---

## Conclusion

**Our MVP plan is fundamentally sound and 90% aligned with best practices!**

**Key changes needed (3-4 hours):**
1. Add claude.md (project context)
2. Use $ARGUMENTS (parameter handling)
3. Move README to root (GitHub visibility)
4. Add .gitignore (data privacy)

**After these changes, we're 100% aligned with Claude Code best practices.** ✅

Ready to start Day 1 (revised)? 🚀
