# Repository Cleanup & Main Branch Plan

**Date:** November 6, 2025
**Status:** 🔴 CRITICAL - Repository needs immediate cleanup
**Priority:** HIGH

---

## 🚨 Problems Identified

### 1. **No Real "main" Branch**
- Default branch: `claude/sonnet-email-prompt-system-011CUq7DY1jXUBRVSpTpLV3Q`
- This is a Claude-generated feature branch, not a proper main branch
- ❌ No `main` or `master` branch exists

### 2. **Current Default Branch is Outdated**
- Contains old file structure (all 26 unarchived files)
- Old README (multi-project focus)
- No Sprint 0 documentation
- No archive directory
- Outdated examples/promptforge-demo

### 3. **Our Clean Work is Isolated**
- Branch: `claude/review-product-plan-011CUr1GxHrvVy5WmuZEyQov`
- Has: Clean structure, archive, Sprint 0 docs
- ❌ Not visible on GitHub as default branch
- ❌ Not merged anywhere

### 4. **8 Feature Branches Exist** (7 stale)
```
✅ claude/review-product-plan-011CUr1GxHrvVy5WmuZEyQov (current - good)
❌ claude/opensource-mission-projects-011CUqDnNLSPqo2sBB7Gidvz (stale)
❌ claude/opensource-mission-projects-011CUqDpMy9wR6UVP2TnHJQC (stale)
❌ claude/organize-mail-archive-011CUqo5SosdRnMWZfaBWFYx (stale)
❌ claude/promptforge-audit-pm-prompts-011CUqrKY3Pi3SDHvvXQUWVD (stale)
❌ claude/promptforge-competitive-analysis-011CUqMDVfiuWW5ZhDXWPHBc (stale)
❌ claude/sonnet-email-prompt-system-011CUq77ws28Pvj7FE4QRNs2 (stale)
❌ claude/sonnet-email-prompt-system-011CUq7DY1jXUBRVSpTpLV3Q (default - outdated)
```

### 5. **examples/promptforge-demo is Outdated**
- References old MISSION_DRIVEN_PROJECTS.md (now archived)
- Demo concept superseded by real PromptForge plugin plan
- Confusing to keep old demo when building real product

---

## ✅ Solution: Clean Main Branch Strategy

### Goal
Create a clean `main` branch with:
- Sprint 0-ready structure
- Archive directory visible
- No stale files
- No confusing demo
- Ready for team to start implementation

---

## 📋 Step-by-Step Plan

### Phase 1: Create Clean Main Branch (15 min)

**Step 1: Create main branch from our clean work**
```bash
# We're on: claude/review-product-plan-011CUr1GxHrvVy5WmuZEyQov
# This has all our clean work

# Create main branch from current state
git checkout -b main

# Remove examples/promptforge-demo (outdated demo)
git rm -r examples/

# Commit
git commit -m "Remove outdated examples/promptforge-demo

This demo referenced old multi-project structure.
PromptForge is now a real plugin (see Sprint 0 docs), not a demo.

Current structure is Sprint 0-ready:
- 7 core documentation files
- archive/ with legacy files
- Clean, focused on single product"

# Push main branch
git push -u origin main
```

**Step 2: Set main as default branch**
```bash
# This must be done on GitHub UI:
# Settings → Branches → Default branch → Change to "main"
```

**Result:**
- ✅ Clean main branch exists
- ✅ Contains Sprint 0 work
- ✅ Archive visible
- ✅ No outdated demo
- ✅ Set as default

---

### Phase 2: Delete Stale Feature Branches (5 min)

**Step 3: Delete stale remote branches**
```bash
# Delete 7 stale branches (keep review-product-plan for reference)
git push origin --delete claude/opensource-mission-projects-011CUqDnNLSPqo2sBB7Gidvz
git push origin --delete claude/opensource-mission-projects-011CUqDpMy9wR6UVP2TnHJQC
git push origin --delete claude/organize-mail-archive-011CUqo5SosdRnMWZfaBWFYx
git push origin --delete claude/promptforge-audit-pm-prompts-011CUqrKY3Pi3SDHvvXQUWVD
git push origin --delete claude/promptforge-competitive-analysis-011CUqMDVfiuWW5ZhDXWPHBc
git push origin --delete claude/sonnet-email-prompt-system-011CUq77ws28Pvj7FE4QRNs2
git push origin --delete claude/sonnet-email-prompt-system-011CUq7DY1jXUBRVSpTpLV3Q
```

**Optional: Keep review-product-plan as reference**
```bash
# Can keep this for Sprint 0 reference, or delete after main is stable
# git push origin --delete claude/review-product-plan-011CUr1GxHrvVy5WmuZEyQov
```

**Result:**
- ✅ 7 stale branches deleted
- ✅ Only main (and optionally review-product-plan) remain
- ✅ Clean branch list

---

### Phase 3: Verification (5 min)

**Step 4: Verify main branch**
```bash
# Switch to main
git checkout main

# Verify structure
ls -la
# Should see:
# - 7 core .md files
# - archive/ directory
# - No examples/ directory
# - .claude/ directory

# Verify archive
ls -la archive/
# Should see:
# - ARCHIVE_README.md
# - promptforge-legacy/
# - other-projects/

# Verify root files
ls *.md
# Should see:
# - README.md
# - PROMPTFORGE_PRODUCT_PLAN_V2.md
# - PROMPTFORGE_SPRINT0_KICKOFF.md
# - PROMPTFORGE_SPRINT0_TASKS.md
# - PROMPTFORGE_TEAM_ONBOARDING.md
# - PROMPTFORGE_QUICK_REFERENCE.md
# - PROMPTFORGE_REPO_TEMPLATE.md
```

**Step 5: Verify on GitHub**
- Go to GitHub repository
- Default branch should be `main`
- archive/ folder should be visible
- No examples/ folder
- Clean file list (7 files + archive)

**Result:**
- ✅ Main branch is clean
- ✅ Archive visible on GitHub
- ✅ Sprint 0-ready structure

---

## 📊 Before & After Comparison

### Before (Current State)

**Default Branch:** `claude/sonnet-email-prompt-system-011CUq7DY1jXUBRVSpTpLV3Q`
```
Root directory:
- 26 files (cluttered, unarchived)
- examples/promptforge-demo/ (outdated)
- Old README (multi-project)
- claude-mail-archive/ (old project)

Feature branches: 8 total
Archive: Not visible (doesn't exist in default branch)
Sprint 0 docs: Not in default branch
Status: ❌ Confusing, not ready
```

### After (Proposed Clean State)

**Default Branch:** `main`
```
Root directory:
- 7 core files (Sprint 0-ready)
- archive/ (19 legacy files preserved)
- Clean README (PromptForge focus)
- .claude/ (project config)

Feature branches: 1 (or 0 after cleanup)
Archive: ✅ Visible and documented
Sprint 0 docs: ✅ All present
Status: ✅ Ready for implementation
```

---

## 🎯 Expected Outcomes

### For Team
- ✅ Clone repository → see clean structure
- ✅ See archive folder immediately
- ✅ No confusion about old files
- ✅ Ready to start Sprint 0

### For GitHub Visitors
- ✅ Professional repository structure
- ✅ Clear README explains current focus
- ✅ Archive shows research history
- ✅ No outdated demos

### For You
- ✅ Clean main branch to show engineers
- ✅ No stale branches to manage
- ✅ Archive preserves all history
- ✅ Ready for Sprint 0 kickoff

---

## ⚠️ Important Notes

### What Gets Deleted
1. **examples/promptforge-demo** - Outdated demo, superseded by real plugin
2. **7 stale feature branches** - Old work, no longer needed

### What Gets Preserved
1. **All Git history** - Everything stays in Git history
2. **Archive folder** - All 19 legacy files preserved and documented
3. **Review-product-plan branch** (optional) - Can keep for reference

### What's Safe
- ✅ No data loss (everything in Git history)
- ✅ Can restore any file from archive or Git history
- ✅ Can recreate any branch if needed

---

## 🚀 Execution Commands (Copy-Paste Ready)

```bash
# Phase 1: Create clean main branch
git checkout claude/review-product-plan-011CUr1GxHrvVy5WmuZEyQov
git checkout -b main
git rm -r examples/
git commit -m "Remove outdated examples/promptforge-demo and create clean main

- Removed examples/promptforge-demo (outdated demo)
- Created main branch from clean Sprint 0 work
- Repository now Sprint 0-ready with:
  - 7 core documentation files
  - archive/ directory with 19 legacy files
  - Clean README focused on PromptForge
  - All Sprint 0 implementation guides

Ready for team to begin Sprint 0."
git push -u origin main

# Phase 2: Delete stale branches
git push origin --delete claude/opensource-mission-projects-011CUqDnNLSPqo2sBB7Gidvz
git push origin --delete claude/opensource-mission-projects-011CUqDpMy9wR6UVP2TnHJQC
git push origin --delete claude/organize-mail-archive-011CUqo5SosdRnMWZfaBWFYx
git push origin --delete claude/promptforge-audit-pm-prompts-011CUqrKY3Pi3SDHvvXQUWVD
git push origin --delete claude/promptforge-competitive-analysis-011CUqMDVfiuWW5ZhDXWPHBc
git push origin --delete claude/sonnet-email-prompt-system-011CUq77ws28Pvj7FE4QRNs2
git push origin --delete claude/sonnet-email-prompt-system-011CUq7DY1jXUBRVSpTpLV3Q

# Optional: Delete review-product-plan branch after confirming main is good
# git push origin --delete claude/review-product-plan-011CUr1GxHrvVy5WmuZEyQov

# Phase 3: Verify
git checkout main
ls -la
ls -la archive/
ls *.md

echo "✅ Done! Repository is clean."
```

---

## 📋 Post-Cleanup Checklist

After executing the plan:

- [ ] Main branch exists
- [ ] Main branch is default on GitHub (Settings → Branches)
- [ ] Main branch contains 7 core files
- [ ] archive/ directory is visible
- [ ] archive/ contains promptforge-legacy/ and other-projects/
- [ ] examples/ directory is removed
- [ ] README.md is Sprint 0-focused
- [ ] 7 stale branches deleted
- [ ] Repository looks professional on GitHub

---

## 🎉 Final Result

**Repository will be:**
- ✅ Clean main branch with Sprint 0 docs
- ✅ Archive visible and documented
- ✅ No outdated demos or stale branches
- ✅ Professional structure
- ✅ Ready for team to clone and start Sprint 0

**Time to complete:** ~25 minutes

**Risk level:** LOW (all data preserved in Git history)

---

## 🤔 Decision Required

**Do you want me to execute this plan?**

1. **Yes, execute now** - I'll run all commands and clean up
2. **Let me review first** - You want to think about it
3. **Modify the plan** - You want to change something

Just say "execute" and I'll make it happen! 🚀

---

**Document Status:** READY FOR EXECUTION
**Created:** November 6, 2025
**Owner:** Product Team
