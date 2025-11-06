# PromptForge Architecture V2.0
**Updated:** November 6, 2025
**Status:** Sprint 0 Ready
**Target:** Claude Code Plugin for PM Professionals

---

## 🎯 Core Strategic Pivot

### What Changed:
**Before:** Website/SaaS for prompt library
**After:** Claude Code plugin for AI-powered PM work

### Why This is Better:
- ✅ Blue ocean market (almost no competition in plugin space)
- ✅ Seamless workflow integration (no copy/paste friction)
- ✅ Context-aware enhancement (knows user's project)
- ✅ Organic discovery (Claude Code marketplace)
- ✅ Network effects (users can extend locally)

---

## 👥 Target Users

**Primary:**
- Product Managers using Claude Code (Claude Pro subscribers)
- Default model: Sonnet 4.5
- Working on product strategy, research, execution

**Secondary (Future):**
- Developers building PM tools
- Teams wanting standardized PM prompts

**NOT Targeting:**
- Website visitors looking for copy/paste prompts
- Hobbyists using free ChatGPT
- Users wanting cloud-hosted search

---

## 🏗️ Plugin Architecture

### Installation Location:
```
~/.claude-code/plugins/promptforge/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── skills/promptforge/
│   └── SKILL.md                 # Auto-activation logic
├── agents/
│   ├── prompt-enhancer.md       # Customization agent (Sonnet)
│   └── prompt-researcher.md     # Browse/search agent (Sonnet)
├── commands/
│   ├── prompt-browse.md         # /prompt-browse
│   ├── prompt-enhance.md        # /prompt-enhance
│   └── prompt-score.md          # /prompt-score
└── prompts/product-management/
    ├── 01-strategy/             # 8-12 prompts
    ├── 02-research/             # 8-12 prompts
    ├── 03-execution/            # 12-15 prompts
    ├── 04-analysis/             # 8-12 prompts
    ├── 05-communication/        # 8-12 prompts
    └── 06-special-workflows/    # 8-12 prompts
    # Total: 70 prompts (PRIME 8.5+)
```

### Installation Method:
```bash
# Via Claude Code marketplace (preferred)
# User installs from marketplace UI

# OR manual install (for development)
$ cd ~/.claude-code/plugins/
$ git clone [promptforge-repo] promptforge
```

---

## 🎬 User Interaction Flows

### Flow 1: Auto-Activation (80% of use cases)

**User working in Claude Code:**
```
PM: "I need to prioritize features for our Q2 roadmap"
  ↓
[PromptForge Skill auto-activates]
  ↓
Claude: "I can help! I have a Feature Prioritization prompt (PRIME 9.2).
         Would you like to:
         1. Show me the prompt as-is
         2. Customize it for your context
         3. Browse related prompts"
  ↓
PM: "Customize for B2B SaaS startup"
  ↓
[Prompt Enhancer reads local file, applies customization]
  ↓
Claude: [Shows enhanced prompt with PRIME 9.4]
        "Changes made:
         ✓ Added ARR impact to RICE framework
         ✓ SaaS examples (Slack, Notion, Linear)
         ✓ Reduced stakeholder complexity

         Want to iterate further?"
```

**Key Benefits:**
- ✅ No commands to remember (auto-activates)
- ✅ Contextual (understands "B2B SaaS startup")
- ✅ Iterative (can refine in conversation)
- ✅ Quality guaranteed (PRIME validated)

### Flow 2: Explicit Commands (Power users)

**User knows what they want:**
```
PM: /prompt-browse execution
  ↓
[Command lists 12 execution-category prompts]
  ↓
PM: "Show me feature-prioritization"
  ↓
[Displays full prompt with metadata]
  ↓
PM: "Enhance for healthcare"
  ↓
[Enhancer customizes, returns PRIME-validated version]
```

### Flow 3: Direct File Access (Advanced)

**User treats it like local files:**
```
PM: "Read the customer interview prompt"
  ↓
Claude: [Finds and reads ~/.claude-code/plugins/promptforge/prompts/.../customer-interview.md]
  ↓
PM: "Make it shorter for 15-min interviews"
  ↓
[Enhancer condenses while maintaining quality]
```

---

## 🤖 Model Strategy (SIMPLIFIED)

### Decision: Default to Sonnet 4.5

**Why:**
- ✅ Claude Pro subscribers get Sonnet by default
- ✅ Sonnet handles 95% of enhancements excellently
- ✅ No model-switching overhead
- ✅ Simpler architecture (one less thing to configure)

**Implementation:**
```markdown
# In all agent files - NO model specified

---
name: prompt-enhancer
# model: <not specified - uses session model (Sonnet 4.5)>
tools: Read, Write, Edit
---
```

**Documentation Note:**
```markdown
## Requirements

PromptForge is optimized for Claude Code with Sonnet 4.5
(default for Claude Pro subscribers).

- ✅ Sonnet 4.5: Full functionality, excellent results
- ⚠️ Haiku: Limited enhancement quality (browsing OK)
- ✅ Opus: Works great but slower (unnecessary for most tasks)
```

**No Fallback Complexity Needed:**
- Users have Sonnet by default
- If they switch to Haiku, quality degrades gracefully
- We don't need to detect/warn (keep it simple)

---

## 📊 Quality Framework: PRIME

### Why PRIME (not CLEAR):

**Problem Found:**
- Dr. Leo S. Lo published "CLEAR Framework" in 2023
- His CLEAR = How to WRITE prompts to AI
- Our CLEAR = How to SCORE prompt quality
- Same acronym = Confusion ❌

**Solution: PRIME Framework**

```
P - Precision (25%)
    Clear, specific, unambiguous instructions

R - Richness (20%)
    Appropriate detail level for task complexity

I - Instruction (20%)
    Explicit output format and success criteria

M - Metadata (15%)
    Target audience, prerequisites, context explicit

E - Examples (20%)
    Concrete demonstrations of desired output

---
PRIME Score = (P × 0.25) + (R × 0.20) + (I × 0.20) + (M × 0.15) + (E × 0.20)

Minimum for inclusion: 8.5 PRIME
Target average: 9.0+ PRIME
```

### Using Both Frameworks:

**Lo's CLEAR (Writing Guidance):**
Use when CREATING prompts for the library:
- Concise instructions (remove fluff)
- Logical structure (clear flow)
- Explicit requirements (no vagueness)
- Adaptive iteration (test with PMs)
- Reflective evaluation (does it work?)

**Our PRIME (Quality Scoring):**
Use when EVALUATING prompts for inclusion:
- Must score 8.5+ PRIME
- Peer review required
- Enhancement validated
- Documented in frontmatter

**Attribution:**
```markdown
Credit: Lo, L. S. (2023). "The CLEAR path: A framework for
enhancing information literacy through prompt engineering."
Journal of Academic Librarianship, 49(4), 102720.
```

---

## 🎯 Sprint 0 Focus (14 Days)

### Week 1: Infrastructure

**AI Engineer:**
- [ ] Repository structure (folders, .claude-plugin/)
- [ ] plugin.json manifest
- [ ] Basic skill with auto-activation triggers
- [ ] Category READMEs with structure
- [ ] Testing framework setup

**Prompt Engineer:**
- [ ] PRIME framework documentation
- [ ] Prompt template with frontmatter
- [ ] Lo's CLEAR writing guidelines
- [ ] Select 3 P0 prompts to migrate:
  - Feature Prioritization (execution)
  - Customer Interview (research)
  - Feedback Synthesis (analysis)

### Week 2: Enhancement System

**AI Engineer:**
- [ ] Prompt Enhancer agent (5 edge cases)
- [ ] Prompt Researcher agent (5 edge cases)
- [ ] 3 slash commands (/browse, /enhance, /score)
- [ ] Integration testing with 3 prompts

**Prompt Engineer:**
- [ ] Score all 3 prompts with PRIME (target 9.0+)
- [ ] Test enhancement on all 3
- [ ] Validate +0.3 PRIME improvement average
- [ ] Document enhancement patterns

### Success Criteria:

- [ ] Plugin installs without errors
- [ ] Skill auto-activates on PM requests
- [ ] Enhancement improves PRIME by +0.3 avg
- [ ] All 10 edge cases handled
- [ ] 3 prompts at PRIME 9.0+
- [ ] Demo-ready by Day 14

---

## 💡 Key Technical Decisions

### 1. Local-First Architecture
**Decision:** All prompts stored locally on user's machine
**Rationale:** Privacy, speed, no API dependencies
**Impact:** Users can customize freely, fork, extend

### 2. Skills Auto-Activation
**Decision:** Proactive skill triggers on PM-related requests
**Rationale:** Seamless UX, no commands to remember
**Impact:** 80% of users won't need to learn slash commands

### 3. Markdown Everything
**Decision:** Prompts, agents, commands all in .md files
**Rationale:** Git-friendly, human-readable, easy to edit
**Impact:** Users can read/edit without special tools

### 4. No Community Sharing (V1)
**Decision:** Users can extend locally, but no push-back to library
**Rationale:** Keep V1 simple, add later if needed
**Impact:** Faster to ship, less complexity

### 5. Claude Code Only (V1)
**Decision:** Don't support Cursor/Windsurf/Aider yet
**Rationale:** Focus on one platform, iterate
**Impact:** Smaller TAM but faster validation

---

## 📈 Competitive Positioning

### vs. Gumroad Prompt Libraries

| Aspect | Gumroad Libraries | PromptForge |
|--------|------------------|-------------|
| Format | PDF/Notion doc | Claude Code plugin |
| Quality | 6-7 PRIME avg | 8.5+ PRIME guaranteed |
| Price | $29-49 one-time | Free (or $9/mo marketplace) |
| Experience | Copy/paste | AI-enhanced, contextual |
| Updates | Manual download | Auto-update (future) |
| Customization | Manual editing | AI-powered enhancement |
| Target | Hobbyists | Professional PMs |

### Market Opportunity:

**Gumroad Market:**
- 1000s of customers
- Low quality expectations
- Price-sensitive

**Claude Code Plugin Market:**
- Smaller TAM (Claude Pro users)
- High quality expectations ✅ (our strength!)
- Value-focused (will pay for quality)
- Blue ocean (almost no competition)

**Strategic Advantage:**
We're the ONLY high-quality PM prompt library in plugin format.

---

## 🚀 Post-Sprint 0 Roadmap (Sprints 1-3)

### Sprint 1: Category Completion (2 weeks)
- Migrate 20 more prompts (total 23)
- Complete Strategy + Research categories
- User testing with 5 beta PMs

### Sprint 2: Scale to 70 Prompts (2 weeks)
- Execution category (12-15 prompts)
- Analysis category (8-12 prompts)
- Communication category (8-12 prompts)

### Sprint 3: Polish & Launch (2 weeks)
- Special Workflows category
- Documentation completion
- Claude Code marketplace submission
- Launch to beta community

---

## ✅ What We're NOT Building (V1 Scope)

### Explicitly Out of Scope:

❌ **Web interface** - Plugin only
❌ **Community sharing** - Local customization only
❌ **Multi-agent support** - Cursor/Windsurf later
❌ **Telemetry/analytics** - Privacy-first, no tracking
❌ **Paid features** - Free in V1, monetization later
❌ **Prompt builder** - Enhancement only, not creation
❌ **Team collaboration** - Single-user focus
❌ **Cloud sync** - Local files only

### Why Scope Discipline Matters:

Each feature above adds 1-2 weeks to Sprint 0.
Ship fast, validate, iterate based on user feedback.

---

## 📋 Updated Documentation Requirements

### Must Update Before Sprint 0:

1. **CLAUDE.md**
   - Replace CLEAR → PRIME framework
   - Update architecture to plugin-first
   - Simplify model strategy (Sonnet default)
   - Remove web UI references

2. **PROMPTFORGE_PRODUCT_PLAN_V2.md**
   - Update market positioning (plugin vs SaaS)
   - Revise competitive analysis
   - Update distribution strategy
   - Adjust monetization approach

3. **PROMPTFORGE_SPRINT0_TASKS.md**
   - Align tasks with plugin architecture
   - Update Week 1 & Week 2 priorities
   - Add plugin-specific testing criteria
   - Update success metrics

4. **PROMPTFORGE_REPO_TEMPLATE.md**
   - Change folder structure to plugin format
   - Add .claude-plugin/ directory
   - Update installation instructions
   - Add local customization guide

5. **QUALITY_STANDARDS.md (New)**
   - PRIME framework detailed rubric
   - Lo's CLEAR writing guidelines
   - Enhancement validation process
   - Scoring examples

---

## 🎯 Next Steps (Start Sprint 0)

### Immediate (Today):

1. **Create feature branch:**
   ```bash
   git checkout -b claude/sprint0-plugin-architecture-{sessionId}
   ```

2. **Update core documentation:**
   - [ ] CLAUDE.md (CLEAR → PRIME, plugin architecture)
   - [ ] PROMPTFORGE_PRODUCT_PLAN_V2.md (market positioning)
   - [ ] PROMPTFORGE_SPRINT0_TASKS.md (align with plugin focus)

3. **Create new documents:**
   - [ ] QUALITY_STANDARDS.md (PRIME rubric + Lo's CLEAR)
   - [ ] PROMPTFORGE_ARCHITECTURE_V2.md (this document)

4. **Archive old thinking:**
   - [ ] Move web UI brainstorming to archive/
   - [ ] Keep for reference but mark as superseded

### Tomorrow (Day 1 Sprint 0):

1. **Repository setup:**
   - Create plugin folder structure
   - Draft plugin.json manifest
   - Create basic skill file

2. **First prompt migration:**
   - Choose Feature Prioritization
   - Apply PRIME framework
   - Score and document

### Week 1 Goal:

**Working plugin that:**
- Installs in Claude Code
- Has 1 functional prompt (Feature Prioritization)
- Skill auto-activates on related requests
- Can display prompt in conversation

---

## 📞 Key Questions Answered

**Q: How do users update prompts?**
A: V1 - Manual git pull. V2 - Auto-update from marketplace.

**Q: Can users add their own prompts?**
A: Yes! They can add .md files to local plugin folder.

**Q: What if user only has Haiku?**
A: Works but quality degrades. No special handling in V1.

**Q: Distribution method?**
A: Claude Code marketplace (official). Manual install for beta.

**Q: Other coding agents (Cursor, etc.)?**
A: Not in V1. Focus on Claude Code, expand later.

---

**Ready to start Sprint 0!** 🚀
