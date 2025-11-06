# PromptForge: Skills-First Architecture (REVISED)
**Using Agent Skills + Markdown Files (No JSON)**
**Date:** November 5, 2025

---

## Major Architecture Change

### ❌ OLD APPROACH (Wrong)
- Slash commands (`/prompt-save`, `/prompt-list`)
- JSON index (`.claude/data/prompts.json`)
- Markdown files for storage
- User-invoked workflows

### ✅ NEW APPROACH (Correct)
- **Agent Skills** (Claude invokes automatically)
- **Pure markdown files** with YAML frontmatter (no JSON!)
- Skills detect when user is working with prompts
- Model-invoked, seamless UX

---

## What Are Skills? (Key Insights from Docs)

### Skills vs Slash Commands

**Slash Commands:**
- User types `/command`
- Explicit invocation
- Good for: Specific workflows user triggers

**Skills (What We Should Use):**
- **Claude decides when to use them**
- **Automatic invocation** based on context
- Good for: Capabilities Claude should always have
- Example: When user writes a prompt, Claude auto-detects and helps

### Skills Structure

```
.claude/skills/
└── prompt-management/          # Skill folder
    ├── SKILL.md               # Core instructions (REQUIRED)
    ├── scripts/               # Python/Bash scripts (optional)
    ├── references/            # Docs for context (optional)
    └── assets/                # Templates (optional)
```

### SKILL.md Format

```yaml
---
name: prompt-management
description: Help users save, organize, version, and improve their AI prompts. Activate when user is writing prompts, asking about prompt quality, or managing their prompt library.
---

# Prompt Management Skill

## When to Activate
- User writes a structured prompt (100+ words, clear instructions)
- User asks "how do I save this?"
- User mentions "prompt library" or "organize prompts"
- User asks about prompt quality

## What to Do
[Instructions for Claude...]
```

**Key:** The `description` field tells Claude **when to use this Skill**

---

## Revised Data Architecture (Markdown Only!)

### ❌ OLD (JSON-based)
```
.claude/
├── data/
│   ├── prompts.json           # Index (metadata)
│   └── prompt-history.json    # Version history
└── prompts/
    └── email-campaign.md      # Prompt content
```

### ✅ NEW (Markdown with YAML frontmatter)
```
.claude/
├── skills/
│   └── prompt-management/
│       └── SKILL.md           # All the logic
└── prompts/
    ├── email-campaign.md      # Prompt with metadata in frontmatter
    ├── prd-template.md
    └── blog-post.md
```

**Each prompt file contains ALL metadata in YAML frontmatter:**

```yaml
---
name: email-campaign
category: marketing
description: Write email marketing campaigns
tags: [email, marketing, sales]
created: 2025-11-05
updated: 2025-11-05
version: 1.0
clear_score: 8.5
versions:
  - version: 1.0
    date: 2025-11-05
    content_hash: abc123
    clear_score: 7.2
  - version: 1.1
    date: 2025-11-06
    content_hash: def456
    clear_score: 8.5
---

Write a compelling email marketing campaign with:
1. Attention-grabbing subject line
2. Personal opening
3. Clear value proposition
4. Social proof
5. Strong call-to-action

Target audience: [specify]
Product/service: [specify]
Goal: [specify - sales, signups, engagement]
```

**No JSON files needed!** Everything is in markdown with YAML frontmatter.

---

## Why This Is MUCH Better

### 1. **Seamless UX**
**Old (slash commands):**
```
User: [writes a great prompt]
User: Now I need to remember to type /prompt-save
User: /prompt-save
Claude: OK, what's the name?
User: email-campaign
Claude: Category?
User: marketing
...
```

**New (Skills):**
```
User: [writes a great prompt]
Claude: "I notice you've written a well-structured prompt!
        Would you like me to save it to your library?
        Suggested name: email-campaign
        Category: marketing (detected from context)"
User: Yes
Claude: [Saves immediately with smart defaults]
```

**Result:** 1 step vs 5+ steps!

### 2. **No Duplicate Data**
**Old:** Metadata in JSON + content in MD = sync issues

**New:** Everything in one MD file = single source of truth

### 3. **Git-Friendly**
**Old:** JSON diffs are ugly, hard to merge

**New:** Pure markdown, beautiful diffs, easy merges

### 4. **Discoverable**
**Old:** User has to know commands exist

**New:** Claude proactively helps when relevant

### 5. **Simpler Architecture**
**Old:** Manage JSON schema, handle updates, sync

**New:** Just write markdown files!

---

## Revised Skills Architecture

### Skill 1: Prompt Management (Core)

**File: `.claude/skills/prompt-management/SKILL.md`**

```yaml
---
name: prompt-management
description: Help users save, organize, version, test, and improve their AI prompts. Activate when user writes prompts, asks about quality, or manages their prompt library.
---

# Prompt Management Skill

You help users build and maintain a high-quality prompt library.

## When to Activate

Activate this Skill when:
1. User writes a structured prompt (100+ words with clear instructions)
2. User asks: "how do I save this?" or "organize my prompts"
3. User mentions "prompt library", "reuse", "version"
4. User asks "is this a good prompt?" or "how can I improve this?"
5. User is in .claude/prompts/ directory

## Core Capabilities

### 1. Save Prompts (Proactive)

When you detect a well-structured prompt in the conversation:

**Detect criteria:**
- 100+ words
- Has clear instructions or structure
- Looks reusable (not one-off question)

**Offer to save:**
"I notice you've written a well-structured prompt! Would you like me to save it to your library?

Suggested metadata:
- Name: [generate from content]
- Category: [detect: product-management, marketing, writing, analysis]
- Description: [one-sentence summary]

Say 'yes' to save, or provide custom metadata."

**If user agrees, create file:**
`.claude/prompts/{name}.md` with YAML frontmatter + content

**Auto-populate:**
- created: today's date
- version: 1.0
- clear_score: [calculate using CLEAR framework]
- tags: [extract from content]

### 2. List Prompts

When user asks: "what prompts do I have?" or "show my library"

**Read all files in .claude/prompts/**
**Display formatted table:**

```
Your Prompt Library
════════════════════════════════════════════════════════

NAME                CATEGORY          CLEAR    UPDATED
───────────────────────────────────────────────────────
email-campaign      marketing         8.5      2025-11-05
prd-template        product-mgmt      9.0      2025-11-04
blog-post           writing           7.8      2025-11-03

Total: 3 prompts | Avg quality: 8.4/10
```

**Suggest:**
- "Want to load one? Just ask: 'show me [name]'"
- "Need to improve quality? I can help optimize any prompt"

### 3. Load/Show Prompt

When user asks: "show me email-campaign" or "load prd-template"

**Read .claude/prompts/{name}.md**
**Display:**

```
Prompt: email-campaign
Category: marketing | Version: 1.0 | Quality: 8.5/10
Last updated: 2025-11-05
═══════════════════════════════════════════════════════

[Full prompt content here]

═══════════════════════════════════════════════════════

Actions:
- Use this prompt: Just reference it in your request
- Improve it: "optimize email-campaign"
- Test it: "test email-campaign with [example]"
- Create variant: "create email-campaign-v2 based on this"
```

### 4. Version Control (Automatic)

When user edits a saved prompt:

**Detect:** User modifies content of .claude/prompts/{name}.md
**Before saving changes:**

"I see you're updating {name} (currently v{X}).

Changes detected:
- [summary of what changed]

Actions:
1. Save as v{X+1} (recommended - keeps history)
2. Overwrite v{X} (lose old version)
3. Save as new prompt

What would you like?"

**If save as new version:**
- Append old version to `versions` array in frontmatter
- Increment version number
- Update `updated` date
- Recalculate `clear_score`

### 5. Quality Scoring (CLEAR Framework)

**Run automatically when:**
- Saving a new prompt
- User asks "is this good?" or "rate this prompt"
- User says "optimize" or "improve"

**CLEAR Scoring (1-10 for each):**

**C - Clarity:** Are instructions unambiguous?
- 1-3: Vague, unclear
- 4-7: Mostly clear
- 8-10: Crystal clear

**L - Length:** Appropriate detail?
- 1-3: Too terse or verbose
- 4-7: Decent length
- 8-10: Perfect detail level

**E - Examples:** Includes examples where needed?
- 1-3: Missing examples
- 4-7: Some examples
- 8-10: Perfect examples

**A - Audience:** Target audience clear?
- 1-3: No audience specified
- 4-7: Implicit audience
- 8-10: Explicit target audience

**R - Result:** Desired output well-defined?
- 1-3: Unclear output
- 4-7: General output
- 8-10: Specific, measurable output

**Overall CLEAR Score:** Average of 5 dimensions

**Display:**
```
Quality Analysis: email-campaign
═══════════════════════════════════════

CLEAR Score: 8.5/10 ⭐ Excellent

Breakdown:
├─ Clarity:   9/10 ✓ Crystal clear instructions
├─ Length:    8/10 ✓ Appropriate detail
├─ Examples:  8/10 ✓ Good examples provided
├─ Audience:  9/10 ✓ Target audience explicit
└─ Result:    8/10 ✓ Clear output format

Strengths:
✓ Very clear structure
✓ Good examples
✓ Well-defined audience

Suggestions for improvement:
→ Add specific output format (e.g., "300 words, 5 bullet points")
→ Include constraint (e.g., "avoid jargon")

Want me to optimize this prompt? Say "optimize email-campaign"
```

### 6. Test Prompts

When user says: "test email-campaign" or "validate this prompt"

**Generate 3 test cases:**
1. Best case (ideal input)
2. Edge case (challenging input)
3. Real-world case (typical scenario)

**For each test case:**
- Run the prompt with test input
- Evaluate output quality (RATE framework)
- Show results

**Display:**
```
Test Results: email-campaign
═══════════════════════════════════════

Test 1: Best Case (B2B SaaS product launch)
Input: [test input]
Output: [generated output]
RATE Score: 9.2/10 ✓ Excellent

Test 2: Edge Case (Complex product with multiple features)
Input: [test input]
Output: [generated output]
RATE Score: 7.5/10 ⚠ Good but could be better

Test 3: Real-world (Weekly newsletter)
Input: [test input]
Output: [generated output]
RATE Score: 8.8/10 ✓ Excellent

Overall: 8.5/10 - Production ready!
Passed: 3/3 tests
```

### 7. Optimize Prompts

When user says: "optimize email-campaign" or "improve this prompt"

**Analyze:**
1. Calculate CLEAR score
2. Identify anti-patterns (vague words, missing examples, etc.)
3. Generate improved version

**Show before/after:**
```
Optimization: email-campaign
═══════════════════════════════════════

Current (v1.0): CLEAR 8.5/10
Optimized (v1.1): CLEAR 9.2/10 (+0.7 improvement)

Changes:
1. ✓ Added specific output format
   Before: "Write a compelling email"
   After: "Write a 200-word email with 3 sections..."

2. ✓ Added constraints
   Before: (none)
   After: "Avoid jargon, write at 8th grade level"

3. ✓ Improved examples
   Before: Generic example
   After: Industry-specific example

Want to save as v1.1? Say "yes"
```

### 8. Search Prompts

When user asks: "find prompts about email" or "search marketing"

**Search criteria:**
- Name contains keyword
- Category matches
- Tags include keyword
- Description contains keyword
- Content includes keyword

**Display results:**
```
Search Results: "email"
═══════════════════════════════════════

Found 3 prompts:

1. email-campaign (marketing, 8.5/10)
   "Write email marketing campaigns"
   Updated: 2025-11-05

2. email-professional (writing, 8.0/10)
   "Draft professional business emails"
   Updated: 2025-11-04

3. email-sequence (marketing, 7.5/10)
   "Create multi-email nurture sequences"
   Updated: 2025-11-03

Want to view one? Say "show email-campaign"
```

### 9. Delete Prompts

When user says: "delete email-campaign" or "remove this prompt"

**Confirm first:**
```
⚠ Delete Confirmation

Prompt: email-campaign
Category: marketing
Version: 1.2
Last used: 2 days ago

Are you sure you want to delete this prompt?
- Say "yes" to delete
- Say "no" to cancel
```

**If yes:** Delete .claude/prompts/{name}.md

## Guidelines

**Always:**
- Be proactive (offer to save good prompts)
- Explain what you're doing
- Show quality scores
- Suggest improvements
- Make it easy (smart defaults)

**Never:**
- Interrupt focused work
- Force saving (always ask)
- Lose version history
- Make assumptions without confirming

## Data Format

**Each prompt file: `.claude/prompts/{name}.md`**

```yaml
---
name: prompt-name
category: product-management | marketing | writing | analysis
description: One-sentence description
tags: [tag1, tag2, tag3]
created: YYYY-MM-DD
updated: YYYY-MM-DD
version: X.Y
clear_score: X.X
versions:
  - version: 1.0
    date: YYYY-MM-DD
    clear_score: X.X
  - version: 1.1
    date: YYYY-MM-DD
    clear_score: X.X
---

[Prompt content here]
```

**No JSON files!** Everything in markdown with YAML frontmatter.

## Examples

**Example 1: User writes a prompt**
```
User: "Create a comprehensive PRD that includes: user stories,
       acceptance criteria, technical requirements, success metrics"

Claude: "That's a well-structured prompt! Want to save it?

Suggested:
- Name: prd-comprehensive
- Category: product-management
- Description: Generate comprehensive PRDs with all sections

Say 'yes' to save or customize"

User: "yes"

Claude: "✓ Saved to .claude/prompts/prd-comprehensive.md
         CLEAR Score: 8.2/10

         Next time, just say 'use prd-comprehensive' to load it!"
```

**Example 2: User wants to improve quality**
```
User: "optimize my email-campaign prompt"

Claude: [Analyzes prompt using CLEAR framework]
        [Shows current score: 7.5/10]
        [Suggests 3 specific improvements]
        [Shows optimized version: 8.8/10]

        "Save as v1.1? Say 'yes'"

User: "yes"

Claude: "✓ Updated email-campaign to v1.1
         Quality improved: 7.5 → 8.8 (+1.3)
         Old version saved in history"
```

**Example 3: User edits a saved prompt**
```
User: [Edits .claude/prompts/blog-post.md]

Claude: "I see you're updating blog-post (v1.0).

Changes detected:
- Added SEO keyword section
- Changed word count from 1000 to 1500

Save as v1.1 (keeps history) or overwrite v1.0?"

User: "v1.1"

Claude: "✓ Saved as blog-post v1.1
         Quality: 8.0/10 (unchanged)
         Version 1.0 preserved in history"
```
```

---

## Implementation Comparison

### Old Approach (Slash Commands + JSON)
**Week 1-2 Plan:**
- Day 1: Implement /prompt-save command
- Day 2: Implement /prompt-list command
- Day 3: Build JSON index management
- Day 4: Implement version control logic
- Day 5: Implement /prompt-compare
- Day 6-7: Add quality scoring
- Day 8-10: Polish

**Total files:** 10 command files + 2 JSON schemas + logic

### New Approach (Single Skill + Markdown)
**Week 1-2 Plan:**
- Day 1: Write SKILL.md (all logic in one file!)
- Day 2: Test Skill activation (does Claude invoke it?)
- Day 3: Refine Skill instructions based on testing
- Day 4: Create 10 seed prompt files (markdown + YAML)
- Day 5: Add CLEAR scoring logic to Skill
- Day 6: Add version control logic to Skill
- Day 7: Add test/optimize features
- Day 8-10: User testing + polish

**Total files:** 1 SKILL.md + seed prompts

**Difference:** 90% less complexity! ✅

---

## Why Skills Are Perfect for PromptForge

### 1. **Prompt Management is a Background Capability**
Users don't wake up thinking "I need to manage prompts today"
They wake up thinking "I need to write a PRD"

Skills let Claude help in the background:
- Detect when user writes reusable prompts
- Proactively offer to save
- Automatically track quality
- Suggest improvements in context

### 2. **No Training Required**
Users don't need to learn `/prompt-save`, `/prompt-list`, etc.
They just work naturally:
- "Save this"
- "Show my prompts"
- "Is this good?"

Claude understands and activates the Skill automatically.

### 3. **Contextual Intelligence**
Skill sees full conversation:
- If user just wrote a PRD prompt → offer to save in "product-management" category
- If user is in .claude/prompts/ → activate prompt management mode
- If user asks "how's my prompt?" → run CLEAR scoring automatically

### 4. **Seamless Versioning**
When user edits a saved prompt file, Skill detects it automatically:
- No need to remember to "save as v2"
- Skill prompts: "Save changes as v1.1?"
- Version history automatic

---

## Revised MVP Sprint Plan (Skills-Based)

### Week 1: Build the Skill

#### Day 1-3: Write SKILL.md
**Task:** Write comprehensive SKILL.md with all logic
**Includes:**
- When to activate
- Save prompts (proactive detection)
- List prompts (read .md files)
- Load prompts (display from .md)
- CLEAR scoring (quality analysis)
- Search (grep .md files)
- Delete (confirm + remove)

**Test:** Does Claude activate the Skill when appropriate?

#### Day 4: Create Seed Prompts
**Task:** Create 10 high-quality seed prompts
**Format:** Markdown with YAML frontmatter
**Categories:**
- Product Management (3): prd-template, user-story, roadmap
- Marketing (4): email-campaign, blog-post, social-media, landing-page
- Writing (2): executive-summary, meeting-notes
- Analysis (1): swot-analysis

**Test:** Can Claude list, load, and analyze seed prompts?

#### Day 5: Refine SKILL.md
**Task:** Based on testing, refine Skill instructions
**Focus:**
- Is activation too aggressive or not enough?
- Are suggestions helpful or annoying?
- Does CLEAR scoring work well?

**Test:** User testing with 3 people

### Week 2: Advanced Features + Polish

#### Day 6-7: Version Control
**Add to SKILL.md:**
- Detect when user edits existing prompt
- Offer to save as new version
- Preserve old versions in frontmatter array
- Show version history

**Test:** Edit a prompt, verify versioning works

#### Day 8: Test & Optimize Features
**Add to SKILL.md:**
- Generate test cases for prompts
- Run tests, show results
- Suggest optimizations based on CLEAR scores

**Test:** "Test email-campaign" → see results

#### Day 9: Documentation
**Create:**
- README.md (what is PromptForge, how to use)
- .claude/claude.md (explain to Claude how PromptForge works)
- Demo video (90 seconds)

#### Day 10: Launch Prep
**Final polish:**
- User test with 5 people
- Fix any issues
- Prepare Product Hunt launch materials

---

## Success Criteria (Revised)

### Technical
- ✅ Skill activates when user writes prompts
- ✅ Can save prompts as .md files with YAML frontmatter
- ✅ Can list all prompts
- ✅ Can load/show specific prompts
- ✅ CLEAR scoring works accurately
- ✅ Version control preserves history
- ✅ No JSON files (pure markdown)

### User Experience
- ✅ Users say "this feels magical" (proactive help)
- ✅ Users don't need to learn commands
- ✅ Prompts improve over time (quality scores increase)
- ✅ Never lose a good prompt (version history)

### Simplicity
- ✅ 1 SKILL.md file (vs 10+ command files)
- ✅ Pure markdown (vs JSON + MD)
- ✅ Git-friendly (beautiful diffs)
- ✅ Easy to understand (read SKILL.md, you get it)

---

## Example: End-to-End Flow

**User Journey (Skills-based):**

```
[User is working on product planning]

User: "Claude, help me write a PRD for a new user authentication feature.
       Include: user stories, acceptance criteria, technical requirements,
       and success metrics."

Claude: [Writes comprehensive PRD]

Claude: "I notice you've asked for a well-structured PRD format.
         Would you like me to save this as a reusable prompt?

         Suggested name: prd-authentication-template
         Category: product-management
         CLEAR Score: 8.5/10 ✓ Excellent

         Say 'yes' to save, or I can customize the metadata."

User: "Actually, name it prd-comprehensive"

Claude: "✓ Saved to .claude/prompts/prd-comprehensive.md
         Quality: 8.5/10 (production-ready)

         Next time, just say 'use my comprehensive PRD prompt'
         and I'll load it!"

[2 weeks later]

User: "Show me my prd prompt"

Claude: [Displays prd-comprehensive]
        "This is version 1.0 (created 2 weeks ago).
         Quality: 8.5/10

         Want to use it? Edit it? Or improve the quality?"

User: "How can I improve it?"

Claude: [Analyzes using CLEAR framework]
        "Current: 8.5/10

         Suggestions:
         1. Add specific output format → +0.3
         2. Include example for complex features → +0.4

         Optimized version would score 9.2/10

         Want to see the optimized version?"

User: "Yes, save it as v1.1"

Claude: "✓ Updated prd-comprehensive to v1.1
         Quality improved: 8.5 → 9.2 (+0.7)
         Old version preserved in history

         Changes:
         - Added output format section
         - Included example for complex features
         - Improved clarity in acceptance criteria"
```

**Total user effort:** Natural conversation, no commands to remember!

---

## Final Recommendation

### APPROVED: Skills-First Approach ✅

**Why this is WAY better:**

1. **90% less code** (1 SKILL.md vs 10+ command files)
2. **Simpler data** (pure markdown, no JSON)
3. **Better UX** (proactive, seamless, magical)
4. **Easier to maintain** (one file to update)
5. **More powerful** (Claude's full intelligence, contextual)

**What changed:**
- ❌ Slash commands → ✅ Agent Skill
- ❌ JSON index → ✅ YAML frontmatter
- ❌ User-invoked → ✅ Model-invoked
- ❌ 10 files → ✅ 1 file

**Ready to build Day 1?** 🚀
