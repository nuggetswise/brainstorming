# PromptForge Sprint 0: Kickoff Checklist & Guide

**Sprint Duration:** 14 days
**Team:** Prompt Engineer + AI Engineer
**Goal:** Build plugin infrastructure, subagents, and migrate 3 prompts
**Start Date:** [TBD]
**End Date:** [TBD]

---

## 📋 Pre-Sprint 0 Checklist (Complete Before Day 1)

### Product Lead Tasks

- [ ] **Review and approve** Product Plan v2.0
- [ ] **Confirm team availability** (both engineers for 14 days)
- [ ] **Schedule kickoff meeting** (Day 1, 30-60 min)
- [ ] **Create GitHub repository** or confirm existing repo
- [ ] **Set up project tracking** (GitHub Projects, Jira, etc.)
- [ ] **Approve budget** (~$100 for Claude API usage)
- [ ] **Define success criteria** for Sprint 0 demo

### AI Engineer Tasks

- [ ] **Review Product Plan v2.0** (architecture, subagents, edge cases)
- [ ] **Read Claude Code plugin docs**: https://code.claude.com/docs/en/plugin-marketplaces
- [ ] **Set up development environment**
  - Claude Code installed and working
  - Git configured
  - Text editor ready
  - Node.js/npm installed (for validation scripts)
- [ ] **Review plugin.json specification**
- [ ] **Understand subagent architecture** (agents/ directory, delegation)
- [ ] **Review all 10 edge cases** (5 per subagent)
- [ ] **Clone any reference repositories** (if available)
- [ ] **Confirm Day 1-2 availability** (project setup critical)

### Prompt Engineer Tasks

- [ ] **Review Product Plan v2.0** (content library, CLEAR framework)
- [ ] **Study CLEAR framework deeply**
  - Clarity (25%)
  - Length (20%)
  - Examples (20%)
  - Audience (15%)
  - Result (20%)
- [ ] **Review 3 existing prompts** to migrate:
  - interview-analysis.md
  - feature-prioritization.md
  - feedback-synthesis.md
- [ ] **Review prompt template structure**
- [ ] **Prepare workspace** for prompt writing
- [ ] **Familiarize with YAML frontmatter** format
- [ ] **Understand enhancement dimensions**:
  - Industry, Company Stage, Detail Level, Output Format, Team Context
- [ ] **Confirm Day 3-4 availability** (prompt migration critical)

### Team Collaboration Setup

- [ ] **Create shared communication channel** (Slack, Discord, email thread)
- [ ] **Set up daily standup time** (15 min, same time each day)
- [ ] **Define code review process** (who reviews what)
- [ ] **Agree on documentation standards** (markdown, formatting)
- [ ] **Set up shared file storage** (if needed beyond Git)
- [ ] **Exchange contact info** for urgent issues

---

## 🚀 Day 1: Sprint Kickoff

### Kickoff Meeting Agenda (60 min)

**Attendees:** Product Lead, Prompt Engineer, AI Engineer

#### 1. Welcome & Context (10 min)
- Why we're building PromptForge
- Vision: 70 world-class PM prompts with AI enhancement
- Market opportunity: vs $49 Gumroad library

#### 2. Sprint 0 Goals Review (10 min)
- **Primary Goal:** Plugin infrastructure + 2 subagents + 3 prompts migrated
- **Success Criteria:**
  - Can install plugin locally
  - Skill auto-activates correctly
  - Enhancement improves CLEAR scores by +0.3
  - All 10 edge cases handled gracefully
  - 3 prompts migrated and scored

#### 3. Architecture Walkthrough (15 min)
- **AI Engineer presents:**
  - Plugin structure (`.claude-plugin/plugin.json`)
  - Skills directory
  - Agents directory (enhancer, researcher)
  - Commands directory
  - Prompts directory structure
- **Q&A on technical approach**

#### 4. Content & Quality Review (10 min)
- **Prompt Engineer presents:**
  - CLEAR framework scoring
  - Prompt template structure
  - Enhancement methodology
  - Quality bar (8.5+ minimum)
- **Q&A on content approach**

#### 5. Timeline & Milestones (5 min)
- Week 1 (Days 1-7): Setup + Skill
- Week 2 (Days 8-14): Subagents + Commands
- Daily standup: [TIME TBD]
- Mid-sprint check-in: Day 7
- Demo & retro: Day 14

#### 6. Roles & Responsibilities (5 min)
- **AI Engineer:** Infrastructure, subagents, commands
- **Prompt Engineer:** Content, quality, documentation
- **Collaboration points:** Enhancement templates, testing, review

#### 7. First Tasks Assignment (5 min)
- Review Day 1-2 tasks (below)
- Clarify any blockers
- Set first checkpoint: End of Day 2

### Day 1 Afternoon: Begin Work

**AI Engineer - Day 1 Tasks (4-6 hours):**

1. **Create Repository Structure** (1-2 hours)
   ```bash
   mkdir promptforge-plugin
   cd promptforge-plugin
   git init

   # Create directory structure
   mkdir -p .claude-plugin
   mkdir -p skills/promptforge
   mkdir -p agents
   mkdir -p commands
   mkdir -p prompts/product-management/{01-strategy,02-research,03-execution,04-analysis,05-communication,06-special-workflows}
   mkdir -p docs

   # Create initial files
   touch .claude-plugin/plugin.json
   touch skills/promptforge/SKILL.md
   touch README.md
   touch .gitignore
   ```

2. **Create plugin.json** (1 hour)
   ```json
   {
     "name": "promptforge",
     "version": "0.1.0",
     "description": "World-class Product Manager prompt library with AI-powered enhancement",
     "author": "PromptForge Team",
     "license": "MIT",
     "homepage": "https://github.com/[YOUR-ORG]/promptforge-plugin",
     "repository": "https://github.com/[YOUR-ORG]/promptforge-plugin",
     "keywords": ["prompts", "product-management", "pm", "enhancement"],
     "components": {
       "skills": ["promptforge"],
       "agents": ["prompt-enhancer", "prompt-researcher"],
       "commands": ["prompt-browse", "prompt-enhance", "prompt-score"]
     },
     "requirements": {
       "claude-code": ">=1.0.0"
     }
   }
   ```

3. **Create README.md skeleton** (30 min)
   - Project title and description
   - Installation instructions (placeholder)
   - Quick start (placeholder)
   - License: MIT

4. **Create .gitignore** (15 min)
   ```
   # OS files
   .DS_Store
   Thumbs.db

   # IDE
   .vscode/
   .idea/
   *.swp
   *.swo

   # Temp files
   *.tmp
   *.log

   # Don't ignore these
   !.claude-plugin/
   ```

5. **Initial commit & push** (15 min)
   ```bash
   git add .
   git commit -m "Initial project structure for PromptForge plugin"
   git remote add origin [REPO_URL]
   git push -u origin main
   ```

**Prompt Engineer - Day 1 Tasks (4-6 hours):**

1. **Design Prompt Template** (2 hours)
   - Create `docs/PROMPT_TEMPLATE.md` with:
     - YAML frontmatter structure
     - Required sections
     - Formatting guidelines
     - Example prompt following template

2. **Write QUALITY_STANDARDS.md** (1 hour)
   - CLEAR framework explained
   - Scoring rubric for each dimension
   - Examples of scores (3/10, 7/10, 10/10)
   - Quality thresholds
   - Common mistakes to avoid

3. **Create Metadata Schema** (1 hour)
   - Define all frontmatter fields:
     ```yaml
     name: string
     category: strategy|research|execution|analysis|communication|special
     subcategory: string
     description: string
     clear_score: number
     industry: all|b2b-saas|ecommerce|enterprise|consumer|healthcare|fintech|marketplace
     company_stage: all|startup|growth|enterprise
     time_estimate: string (e.g., "30-45 min")
     difficulty: beginner|intermediate|advanced
     frameworks: [array of strings]
     tags: [array of strings]
     related_prompts: [array of strings]
     version: string
     last_updated: YYYY-MM-DD
     ```

4. **Document in Git** (30 min)
   ```bash
   git pull
   git add docs/PROMPT_TEMPLATE.md docs/QUALITY_STANDARDS.md
   git commit -m "Add prompt template and quality standards"
   git push
   ```

### Day 1 End-of-Day Sync (15 min)

**Checklist:**
- [ ] Repository created and both engineers have access
- [ ] Basic structure in place
- [ ] plugin.json created
- [ ] Prompt template designed
- [ ] Quality standards documented
- [ ] No blockers for Day 2

**Discussion:**
- What went well?
- Any surprises or challenges?
- Ready for Day 2 tasks?

---

## 📅 Day 2: Core Setup Continues

### Daily Standup (15 min)

**Each person shares:**
1. What I completed yesterday
2. What I'm doing today
3. Any blockers

### AI Engineer - Day 2 Tasks (6-8 hours)

1. **Create PromptForge Skill (v1 - Basic)** (4-5 hours)

   **File:** `skills/promptforge/SKILL.md`

   ```markdown
   ---
   name: promptforge
   description: World-class Product Manager prompt library with AI-powered enhancement
   ---

   # PromptForge Skill

   ## When to Activate

   Activate this skill when:
   - User asks for help with PM tasks ("I need to write a PRD")
   - User mentions prompts ("show me prompts for...")
   - User is in promptforge-plugin directory
   - User requests specific PM workflow ("feature prioritization")

   ## What This Skill Does

   PromptForge provides:
   - 70+ world-class PM prompts (CLEAR score 8.5+)
   - AI-powered enhancement for your context
   - Semantic search across library
   - Quality scoring using CLEAR framework

   ## Browse Mode

   When user wants to explore the library:

   1. Show category tree with prompt counts
   2. Display top 3 prompts per category with CLEAR scores
   3. Highlight time estimates and difficulty
   4. Ask which category or specific prompt they want

   Example response:
   ```
   📚 PromptForge Library (70 Prompts)

   📊 Strategy (10 prompts)
      • Product Vision Statement (9.0) - 30-45 min
      • Roadmap Planning (9.0) - 45-60 min
      • OKR Setting & Tracking (8.8) - 30 min

   🔍 Research & Discovery (15 prompts)
      • User Interview Guide (9.0) - 20-30 min
      • Interview Analysis (9.2) - 45-60 min
      • Competitive Analysis (8.9) - 45-60 min

   [... etc ...]

   Which category interests you? Or search by keyword.
   ```

   ## Load Mode

   When user requests specific prompt:

   1. Read prompt file from `prompts/` directory
   2. Parse YAML frontmatter for metadata
   3. Display formatted prompt with:
      - Name and CLEAR score
      - Time estimate and difficulty
      - Full prompt content
      - Frameworks referenced
   4. Offer enhancement options

   Example response:
   ```
   📋 Feature Prioritization (CLEAR: 9.2/10)

   ⏱️  Time: 30-45 min  |  📊 Difficulty: Intermediate
   🎯 Frameworks: RICE, ICE, Priority Matrix

   [Full prompt content displayed]

   Options:
   1. ✅ Use this prompt as-is
   2. 🎨 Customize for your context (industry, stage, etc.)
   3. 📖 See example output
   4. 🔗 View related prompts
   ```

   ## Enhancement Mode

   When user wants customization:

   1. Confirm which prompt to enhance
   2. Delegate to `prompt-enhancer` subagent:
      ```
      I'll customize this prompt for you.

      Invoking prompt enhancer...
      [Subagent takes over in separate context]
      ```
   3. Wait for subagent to return enhanced prompt
   4. Display result from subagent

   ## Search Mode

   When user searches:

   1. Check if it's a simple keyword or complex query
   2. For simple: Search prompts locally by:
      - Name matching
      - Tag matching
      - Description matching
   3. For complex: Delegate to `prompt-researcher` subagent
   4. Show top 5 results with excerpts

   ## Important Guidelines

   - Always show CLEAR scores to build trust
   - Emphasize time savings ("This prompt will save you 2 hours")
   - Be proactive: "Since you're working on X, you might also need Y"
   - Highlight enhancement: "This is excellent as-is, but I can customize it for your B2B SaaS context"

   ## Don't

   - Don't create prompts from scratch (use library only)
   - Don't claim prompts are perfect (invite feedback)
   - Don't overwhelm with all 70 at once (progressive disclosure)
   ```

2. **Test Skill Activation** (1 hour)
   - Install plugin locally
   - Test activation triggers
   - Verify browse mode works
   - Document any issues

3. **Create Category READMEs** (1-2 hours)

   **Example:** `prompts/product-management/02-research/README.md`
   ```markdown
   # Research & Discovery Prompts

   ## Overview

   This category contains 15 prompts for user research, market analysis,
   and discovery activities.

   ## When to Use These Prompts

   - Planning or conducting user interviews
   - Analyzing research data
   - Understanding market dynamics
   - Creating user personas
   - Mapping customer journeys

   ## Available Prompts

   ### User Research
   1. **User Interview Guide** (9.0) - Create structured interview scripts
   2. **Interview Analysis** (9.2) - Synthesize interview insights thematically
   3. **Survey Design** (8.8) - Create effective surveys

   ### Market Analysis
   4. **Competitive Analysis** (8.9) - Analyze competitors systematically
   5. **Market Research Report** (8.6) - Synthesize market data

   [... etc ...]

   ## Getting Started

   Most PMs start with:
   1. User Interview Guide → conduct research
   2. Interview Analysis → synthesize findings
   3. Persona Development → document user types

   ## Related Categories

   - Strategy: Use research to inform product vision
   - Execution: Translate insights to user stories
   ```

4. **End of Day:** Commit and push all work

### Prompt Engineer - Day 2 Tasks (6-8 hours)

1. **Locate & Review Existing 3 Prompts** (1 hour)
   - Find interview-analysis.md (or create placeholder)
   - Find feature-prioritization.md (or create placeholder)
   - Find feedback-synthesis.md (or create placeholder)
   - Review current format and content

2. **Create Enhancement Template Library** (3-4 hours)

   **File:** `docs/ENHANCEMENT_TEMPLATES.md`

   Document transformation patterns for each dimension:

   **Industry Transformations:**
   - B2B SaaS → Add ARR, MRR, churn metrics
   - E-commerce → Add GMV, conversion rate, cart abandonment
   - Healthcare → Add compliance (HIPAA), patient outcomes
   - FinTech → Add security, regulatory compliance

   **Stage Transformations:**
   - Startup → Reduce stakeholders, increase speed
   - Growth → Add process, scale considerations
   - Enterprise → Add governance, compliance, committees

   **Detail Level:**
   - Quick → 50% fewer steps, 1 example minimum
   - Standard → As designed
   - Comprehensive → 2x examples, edge cases, checklists

   [Document 20-30 transformation patterns with examples]

3. **Write ENHANCEMENT_GUIDE.md Draft** (2 hours)
   - What is enhancement?
   - How does it work?
   - What dimensions can be customized?
   - Example: Original vs Enhanced (side-by-side)
   - When to enhance vs use original
   - Best practices

4. **End of Day:** Commit and push documentation

### Day 2 End-of-Day Sync (15 min)

**Checklist:**
- [ ] PromptForge Skill created (basic version)
- [ ] Category READMEs created
- [ ] Enhancement templates documented
- [ ] ENHANCEMENT_GUIDE.md drafted
- [ ] Ready to migrate prompts on Day 3

---

## 📅 Days 3-7: Week 1 Completion

### Day 3-4: Migrate Existing Prompts

**Prompt Engineer (Lead):**
- [ ] Migrate interview-analysis.md to new template
- [ ] Migrate feature-prioritization.md to new template
- [ ] Migrate feedback-synthesis.md to new template
- [ ] Score all 3 using CLEAR framework
- [ ] Document scoring rationale
- [ ] Create before/after comparison

**AI Engineer (Support):**
- [ ] Build CLEAR scoring automation script
- [ ] Validate migrated prompts load correctly in Skill
- [ ] Test metadata parsing
- [ ] Provide feedback on quality

### Day 5-7: Test & Iterate Skill

**AI Engineer (Lead):**
- [ ] Test browse mode with 3 prompts
- [ ] Test load mode for each prompt
- [ ] Implement basic search (keyword matching)
- [ ] Fix bugs found in testing
- [ ] Document Skill behavior

**Prompt Engineer (Support):**
- [ ] Test user workflows
- [ ] Identify UX issues
- [ ] Suggest improvements
- [ ] Write usage examples for README

**Day 7: Mid-Sprint Review (1 hour)**
- Demo: Browse and load 3 prompts
- Review: CLEAR scores and quality
- Discuss: Any adjustments needed for Week 2
- Confirm: Ready for subagent development

---

## 📅 Days 8-14: Week 2 - Subagents

### Day 8-10: Prompt Enhancer Subagent

**AI Engineer (Lead):**
- [ ] Create `agents/prompt-enhancer.md` structure
- [ ] Implement context gathering workflow
- [ ] Implement enhancement transformations
- [ ] Add CLEAR scoring comparison
- [ ] Implement 5 edge cases:
  - [ ] Enhancement makes score worse
  - [ ] Impossible combination requested
  - [ ] User abandons mid-enhancement
  - [ ] Original already industry-specific
  - [ ] Enhancement timeout
- [ ] Test with all 3 existing prompts
- [ ] Measure score improvements

**Prompt Engineer (Support):**
- [ ] Provide enhancement templates
- [ ] Test enhanced versions for quality
- [ ] Validate improvements are meaningful
- [ ] Document enhancement patterns observed

### Day 11-12: Prompt Researcher Subagent

**AI Engineer (Lead):**
- [ ] Create `agents/prompt-researcher.md` structure
- [ ] Implement search logic (semantic + keyword)
- [ ] Implement comparison mode
- [ ] Implement workflow recommendations
- [ ] Implement 5 edge cases:
  - [ ] No results found
  - [ ] Too many results (ambiguous query)
  - [ ] User doesn't know what they need
  - [ ] Unrelated comparison requested
  - [ ] Handoff to enhancer when appropriate
- [ ] Test search relevance

**Prompt Engineer (Support):**
- [ ] Create search test cases
- [ ] Test comparison quality
- [ ] Validate workflow recommendations
- [ ] Document search patterns

### Day 13-14: Commands & Final Integration

**AI Engineer (Lead):**
- [ ] Create `commands/prompt-browse.md`
- [ ] Create `commands/prompt-enhance.md`
- [ ] Create `commands/prompt-score.md`
- [ ] Test full integration:
  - Skill → Subagent delegation
  - Commands → Subagent invocation
  - Edge cases → Graceful handling
- [ ] Fix integration bugs
- [ ] Performance testing

**Prompt Engineer (Support):**
- [ ] Write command documentation
- [ ] Create usage examples
- [ ] End-to-end testing
- [ ] Document user workflows

**Day 14: Sprint 0 Demo & Retrospective (2 hours)**

#### Demo (1 hour)

Show working features:
1. Plugin installation
2. Skill auto-activation
3. Browse 3 prompts
4. Load and display a prompt
5. Enhancement workflow (context gathering → enhanced prompt → score comparison)
6. Search and discovery
7. Custom commands
8. Edge case handling (pick 2-3 to demonstrate)

#### Retrospective (1 hour)

**What went well:**
- [Team fills in]

**What could be improved:**
- [Team fills in]

**Action items for Sprint 1:**
- [Team fills in]

**Sprint 0 Success Criteria Review:**
- [ ] Can install plugin locally ✅/❌
- [ ] Skill auto-activates correctly ✅/❌
- [ ] Enhancement improves CLEAR scores by +0.3 ✅/❌
- [ ] Search finds relevant prompts ✅/❌
- [ ] All 10 edge cases handled gracefully ✅/❌
- [ ] 3 prompts migrated and scored ✅/❌
- [ ] Zero critical bugs ✅/❌

---

## 🎯 Sprint 0 Deliverables Checklist

### Infrastructure
- [ ] Plugin repository created
- [ ] Directory structure complete
- [ ] plugin.json configured
- [ ] README.md with installation instructions
- [ ] .gitignore configured
- [ ] All files in Git

### Skills
- [ ] PromptForge Skill created
- [ ] Auto-activation working
- [ ] Browse mode functional
- [ ] Load mode functional
- [ ] Search mode (basic) functional

### Subagents
- [ ] Prompt Enhancer created
- [ ] All 5 enhancer edge cases handled
- [ ] Enhancement improves scores (+0.3 average)
- [ ] Prompt Researcher created
- [ ] All 5 researcher edge cases handled
- [ ] Search returns relevant results

### Commands
- [ ] /prompt-browse command works
- [ ] /prompt-enhance command works
- [ ] /prompt-score command works
- [ ] All commands integrated with subagents

### Content
- [ ] 3 prompts migrated to new format
- [ ] All 3 scored with CLEAR framework
- [ ] Category READMEs created
- [ ] Prompt template documented

### Documentation
- [ ] QUALITY_STANDARDS.md complete
- [ ] ENHANCEMENT_GUIDE.md complete
- [ ] ENHANCEMENT_TEMPLATES.md complete
- [ ] PROMPT_TEMPLATE.md complete
- [ ] README.md updated with examples

### Testing
- [ ] Local plugin installation tested
- [ ] All features tested end-to-end
- [ ] Edge cases validated
- [ ] Performance acceptable (<3 sec per operation)
- [ ] Bug list created (if any)

---

## 🚨 Common Issues & Solutions

### Issue 1: Plugin Won't Install Locally

**Symptoms:** Error when running `/plugin install`

**Troubleshooting:**
1. Check plugin.json syntax (valid JSON?)
2. Verify all required fields present
3. Check file paths are correct
4. Review Claude Code plugin docs
5. Check Claude Code version compatibility

**Solution:** Fix plugin.json, test with minimal config first

---

### Issue 2: Skill Doesn't Auto-Activate

**Symptoms:** Skill never triggers automatically

**Troubleshooting:**
1. Check activation criteria in SKILL.md
2. Test with explicit trigger phrases
3. Verify skill is registered in plugin.json
4. Check directory structure matches spec
5. Review skill name matches everywhere

**Solution:** Refine activation criteria, test incrementally

---

### Issue 3: Subagent Delegation Fails

**Symptoms:** Subagent never invoked or errors out

**Troubleshooting:**
1. Check agent file exists and is valid markdown
2. Verify agent registered in plugin.json
3. Test agent invocation syntax
4. Check tool permissions in agent config
5. Review error messages carefully

**Solution:** Simplify agent first, add complexity gradually

---

### Issue 4: Enhancement Doesn't Improve Score

**Symptoms:** Enhanced version scores same or worse

**Troubleshooting:**
1. Review transformation logic
2. Check if original was already optimized
3. Validate CLEAR scoring calculation
4. Test with different dimensions
5. Compare specific CLEAR dimensions (which dropped?)

**Solution:** Refine transformations, handle "already optimal" case

---

### Issue 5: Performance Too Slow

**Symptoms:** Operations take >5 seconds

**Troubleshooting:**
1. Profile where time is spent
2. Check for unnecessary file reads
3. Optimize search algorithms
4. Cache repeated operations
5. Consider chunking large operations

**Solution:** Add caching, optimize file I/O, show progress indicators

---

## 📞 Getting Help

### Internal Team
- **Blocker in first 2 hours:** Escalate immediately to Product Lead
- **Daily blockers:** Raise in standup, pair program if needed
- **Technical questions:** Both engineers collaborate

### External Resources
- **Claude Code Docs:** https://code.claude.com/docs/
- **Plugin Marketplace:** https://code.claude.com/docs/en/plugin-marketplaces
- **Community:** (if available, link here)
- **Support:** (if available, link here)

### Escalation Path
1. Try to solve independently (30 min)
2. Ask teammate for help (30 min)
3. Research documentation (30 min)
4. Escalate to Product Lead
5. Consider scope adjustment if critical blocker

---

## ✅ Ready to Start?

### Final Pre-Flight Checklist

**Product Lead:**
- [ ] Approved Product Plan v2.0
- [ ] Scheduled Day 1 kickoff meeting
- [ ] Created repository (or confirmed URL)
- [ ] Granted team access
- [ ] Set up project tracking
- [ ] Available for Day 1 kickoff

**AI Engineer:**
- [ ] Reviewed full Product Plan v2.0
- [ ] Read Claude Code plugin documentation
- [ ] Development environment ready
- [ ] Understands subagent architecture
- [ ] Reviewed all edge cases
- [ ] Available for 14 days
- [ ] Ready for Day 1 tasks

**Prompt Engineer:**
- [ ] Reviewed full Product Plan v2.0
- [ ] Studied CLEAR framework
- [ ] Reviewed existing 3 prompts
- [ ] Understands enhancement dimensions
- [ ] Workspace prepared
- [ ] Available for 14 days
- [ ] Ready for Day 1 tasks

**All Checkboxes Complete?**

✅ **GO FOR SPRINT 0 KICKOFF!**

---

**Last Updated:** November 6, 2025
**Next Review:** Day 7 (Mid-Sprint Check-in)
**Document Owner:** Product Lead
