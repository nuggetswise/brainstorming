# PromptForge - Quick Start Implementation Guide

**Get Started Building in 30 Minutes**

---

## Step 1: Project Setup (5 minutes)

```bash
# Create project structure
mkdir promptforge
cd promptforge

# Create directory structure
mkdir -p .claude/{commands,data,prompts}
mkdir -p src/{core,nodes,utils}
mkdir -p tests

# Create Python environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install anthropic click rich
```

## Step 2: Create Core Claude Client (10 minutes)

Create `src/core/claude_client.py`:

```python
import os
import anthropic
import hashlib
import json
from pathlib import Path

class ClaudeClient:
    """Simple Claude API wrapper with caching"""

    def __init__(self, cache_dir=".claude/data/cache"):
        self.client = anthropic.Anthropic(
            api_key=os.environ.get("ANTHROPIC_API_KEY")
        )
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def call(self, prompt: str, use_cache: bool = True):
        """Call Claude with optional caching"""

        # Check cache
        if use_cache:
            cache_key = hashlib.sha256(prompt.encode()).hexdigest()
            cache_file = self.cache_dir / f"{cache_key}.json"

            if cache_file.exists():
                with open(cache_file) as f:
                    return json.load(f)['response']

        # Make API call
        response = self.client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}]
        )

        result = response.content[0].text

        # Save to cache
        if use_cache:
            with open(cache_file, 'w') as f:
                json.dump({'response': result}, f)

        return result
```

## Step 3: Build First Command - /prompt-save (15 minutes)

Create `.claude/commands/prompt-save.md`:

```markdown
---
description: Save a prompt to your library for reuse
---

You are helping the user save a prompt to their library.

## Steps:

1. Ask for the prompt name (use kebab-case)
2. Ask them to provide the prompt content
3. Ask for metadata:
   - Category (code, writing, analysis, etc.)
   - Description (one sentence)
   - Tags (comma-separated)

4. Save the prompt to `.claude/prompts/{name}.md` with this format:

\`\`\`markdown
---
name: {name}
category: {category}
description: {description}
tags: {tags}
created: {date}
version: 1.0
---

{prompt_content}
\`\`\`

5. Update the index at `.claude/data/prompt-index.json`:

\`\`\`json
{
  "prompts": [
    {
      "id": "{name}",
      "name": "{name}",
      "category": "{category}",
      "description": "{description}",
      "tags": [{tags}],
      "created": "{date}",
      "version": "1.0",
      "file": ".claude/prompts/{name}.md"
    }
  ]
}
\`\`\`

6. Confirm with:
   "✓ Saved to .claude/prompts/{name}.md"
   "Run `/prompt-list` to see all your saved prompts"
```

## Step 4: Test It! (5 minutes)

```bash
# Set your API key
export ANTHROPIC_API_KEY=your_key_here

# In Claude Code:
cd promptforge
claude /prompt-save

# Follow the prompts to save your first prompt!
```

---

## Next Steps: Add More Commands

### /prompt-list Command

Create `.claude/commands/prompt-list.md`:

```markdown
---
description: List all saved prompts in your library
---

You are showing the user their prompt library.

## Steps:

1. Read `.claude/data/prompt-index.json`
2. If it doesn't exist or is empty, say:
   "No prompts saved yet. Run `/prompt-save` to add your first prompt!"

3. Display prompts in a formatted table:

\`\`\`
Your Prompt Library
═══════════════════════════════════════════════════════════

NAME                  CATEGORY     DESCRIPTION
────────────────────────────────────────────────────────────
code-review           code         Comprehensive code review
meeting-summary       writing      Summarize meeting notes
bug-analysis          code         Analyze and fix bugs

Total: 3 prompts
\`\`\`

4. Suggest next actions:
   - `/prompt-load [name]` - Load a prompt
   - `/prompt-save` - Save a new prompt
   - `/prompt-search [query]` - Search prompts
```

### /prompt-search Command

Create `.claude/commands/prompt-search.md`:

```markdown
---
description: Search prompts by semantic meaning
---

You are helping the user search their prompt library.

## Steps:

1. Ask for their search query if not provided
2. Read all prompts from `.claude/data/prompt-index.json`
3. For each prompt, analyze semantic similarity to the query
4. Rank prompts by relevance (0-100% match)
5. Display top 5 results:

\`\`\`
Found 5 matching prompts:

1. python-debugger (98% match)
   "Step-by-step Python debugging with root cause analysis"

2. code-analysis (87% match)
   "Analyze code for bugs, performance issues..."

3. error-explainer (82% match)
   "Explain error messages and suggest fixes"

Load a prompt: /prompt-load [name]
\`\`\`

## Ranking Logic:

Consider:
- Keywords overlap
- Semantic similarity of description
- Category relevance
- Tags match

Explain why each prompt matched in parentheses.
```

### /prompt-score Command

Create `.claude/commands/prompt-score.md`:

```markdown
---
description: Score a prompt's quality on multiple dimensions
---

You are evaluating a prompt's quality.

## Steps:

1. Ask which prompt to score (or paste a prompt)
2. Evaluate on these dimensions (0-10 each):
   - Clarity: Are instructions clear?
   - Specificity: Are requirements specific?
   - Completeness: Does it cover all aspects?
   - Structure: Is it well-organized?
   - Examples: Are there helpful examples?
   - Constraints: Are boundaries defined?

3. Calculate overall score (average)
4. Assign letter grade:
   - A: 9.0-10.0
   - B: 8.0-8.9
   - C: 7.0-7.9
   - D: 6.0-6.9
   - F: <6.0

5. Display results:

\`\`\`
Prompt Quality Report: {name}
═══════════════════════════════════════════

Overall Score: 8.2/10 (B+)

Dimension Breakdown:
├─ Clarity:      9/10 ✓ Excellent
├─ Specificity:  8/10 ✓ Good
├─ Completeness: 7/10 ✓ Good
├─ Structure:    9/10 ✓ Excellent
├─ Examples:     6/10 ⚠ Fair
└─ Constraints:  8/10 ✓ Good

Strengths:
✓ Very clear instructions
✓ Well-structured with numbered steps

Areas for Improvement:
• Add concrete examples
• Define severity levels more clearly

Recommendation: Good quality prompt, ready for use.
\`\`\`

## Scoring Guidelines:

**Clarity (0-10):**
- 10: Crystal clear, no ambiguity
- 7-9: Clear but could be more specific
- 4-6: Some confusion possible
- 0-3: Vague or confusing

**Specificity (0-10):**
- 10: Very specific requirements
- 7-9: Good detail
- 4-6: Some specifics missing
- 0-3: Too generic

**Completeness (0-10):**
- 10: Covers all necessary aspects
- 7-9: Mostly complete
- 4-6: Some aspects missing
- 0-3: Incomplete

**Structure (0-10):**
- 10: Excellently organized
- 7-9: Well-structured
- 4-6: Decent structure
- 0-3: Poorly organized

**Examples (0-10):**
- 10: Great examples provided
- 7-9: Good examples
- 4-6: Basic examples
- 0-3: No examples (if needed)
- N/A: Examples not needed

**Constraints (0-10):**
- 10: Clear boundaries defined
- 7-9: Good constraints
- 4-6: Some constraints
- 0-3: No constraints
```

---

## Advanced: Add Prompt Optimization

Create `.claude/commands/prompt-optimize.md`:

```markdown
---
description: Get AI-powered suggestions to improve your prompt
---

You are analyzing a prompt and suggesting improvements.

## Steps:

1. Ask which prompt to optimize (or paste content)
2. Analyze the prompt for:
   - Length (optimal: 200-800 chars)
   - Number of instructions (optimal: 5-10)
   - Has examples? (good practice)
   - Has output format? (good practice)
   - Has constraints? (good practice)
   - Clarity issues
   - Specificity issues

3. Provide specific, actionable suggestions

4. Display results:

\`\`\`
Analyzing prompt: code-review
════════════════════════════════════════════

Current Quality: 7.8/10 (Good)

Issues Found:
⚠ Too long (1,450 chars) - optimal is 200-800
⚠ 12 instructions - consider consolidating
✓ Has good examples
✓ Output format defined

Suggested Improvements:

1. Consolidate instructions 7-9 into one
   Current: "Check for X. Check for Y. Check for Z."
   Better: "Check for X, Y, and Z."
   Impact: -15% length, +0.2 clarity

2. Move example to appendix
   Current: Example in middle of instructions
   Better: Example at end
   Impact: +0.5 structure score

3. Reduce instruction count
   Current: 12 separate instructions
   Better: Group related items
   Impact: +0.3 clarity

Expected Improvement:
├─ Quality: 7.8 → 8.3 (+0.5)
├─ Token usage: 1,450 → 1,150 (-20%)
└─ Clarity: 7.5 → 8.0 (+0.5)

Would you like to:
[1] See the improved version
[2] Apply suggestions automatically
[3] Save both versions for comparison
\`\`\`

## Optimization Principles:

1. **Optimal length:** 200-800 characters
   - Too short: Lacks detail
   - Too long: Loses focus

2. **Instruction count:** 5-10 items
   - Too few: Not specific enough
   - Too many: Overwhelming

3. **Structure:**
   - Start with context/goal
   - List instructions (numbered)
   - Provide examples
   - Define output format
   - Set constraints

4. **Examples:**
   - Always helpful
   - Show expected quality
   - Demonstrate format

5. **Output format:**
   - Specify structure
   - Use templates
   - Define clearly

6. **Constraints:**
   - What to include
   - What to avoid
   - Limits/boundaries
```

---

## Example: Using PromptForge

```bash
# Save your first prompt
$ claude /prompt-save

> What do you want to name this prompt?
code-review

> Paste or describe the prompt:
Review code for security, performance, and best practices.
Provide specific feedback with examples.

> What category?
code

> Description (one sentence):
Comprehensive code review with actionable feedback

> Tags (comma-separated):
code, review, security, performance

✓ Saved to .claude/prompts/code-review.md

# List your prompts
$ claude /prompt-list

Your Prompt Library
═══════════════════════════════════════════
NAME           CATEGORY    DESCRIPTION
───────────────────────────────────────────
code-review    code        Comprehensive review

Total: 1 prompt

# Score the prompt
$ claude /prompt-score code-review

Prompt Quality Report: code-review
═══════════════════════════════════════════
Overall Score: 6.5/10 (D)

Issues:
⚠ Too short (lacks detail)
⚠ No examples
⚠ No output format

# Optimize it
$ claude /prompt-optimize code-review

Suggested Improvements:
1. Add specific instructions
2. Include example review
3. Define output format

Would you like to see the improved version? [y/n]
y

Improved Version:
─────────────────────────────────────────
Review the following code for:
1. Security vulnerabilities (SQL injection, XSS, etc.)
2. Performance issues (O(n²) algorithms, memory leaks)
3. Best practices (naming, structure, documentation)

For each issue found:
- SEVERITY: Critical/Major/Minor
- ISSUE: Description
- SUGGESTION: How to fix with code example

Example output:
CRITICAL | SQL Injection | Use parameterized queries:
  cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
─────────────────────────────────────────

Save as new version? [y/n]
y

✓ Saved as code-review v2

# Compare versions
$ claude /prompt-diff code-review v1 v2

Diff: v1 → v2
─────────────────────────────────────────
+ Added: Specific criteria (security, performance, practices)
+ Added: Output format specification
+ Added: Example output
~ Changed: Tone (more structured)

Quality improvement: 6.5 → 8.7 (+2.2)

# Search for prompts
$ claude /prompt-search "help debug python code"

Found 1 matching prompt:
1. code-review (75% match)
   Includes debugging capabilities

No exact match. Create new prompt? [y/n]
```

---

## File Structure After Setup

```
promptforge/
├─ .claude/
│  ├─ commands/
│  │  ├─ prompt-save.md
│  │  ├─ prompt-list.md
│  │  ├─ prompt-search.md
│  │  ├─ prompt-score.md
│  │  └─ prompt-optimize.md
│  ├─ data/
│  │  ├─ prompt-index.json
│  │  ├─ version-history.json
│  │  └─ cache/
│  └─ prompts/
│     ├─ code-review.md
│     └─ ...
├─ src/
│  └─ core/
│     └─ claude_client.py
└─ README.md
```

---

## What You've Built

✅ **Version control for prompts** (like git)
✅ **Semantic search** (find by meaning)
✅ **Quality scoring** (0-10 evaluation)
✅ **AI-powered optimization** (auto-improvements)
✅ **Local-first storage** (no servers needed)

**Time to build:** ~30 minutes
**Lines of code:** <200 (mostly markdown!)
**Value:** Infinite (manages all your prompts forever)

---

## Next Steps

### Week 1: Core Commands
- ✅ /prompt-save
- ✅ /prompt-list
- ✅ /prompt-search
- ⬜ /prompt-load
- ⬜ /prompt-delete
- ⬜ /prompt-diff

### Week 2: Intelligence
- ✅ /prompt-score
- ✅ /prompt-optimize
- ⬜ /prompt-test (run test cases)
- ⬜ /prompt-benchmark (A/B testing)

### Week 3: Advanced
- ⬜ /prompt-share (community)
- ⬜ /prompt-discover (browse)
- ⬜ /prompt-stats (analytics)

---

## Tips for Success

1. **Use it yourself daily**
   - Save every prompt you use
   - Score and optimize them
   - Build real usage data

2. **Start simple**
   - Don't over-engineer
   - Ship fast, iterate
   - Add features as needed

3. **Focus on UX**
   - CLI should be delightful
   - Clear, helpful output
   - Smart defaults

4. **Share early**
   - Tweet progress
   - Get feedback
   - Build community

---

## Common Issues & Solutions

**Issue: "No prompts found"**
- Create `.claude/data/prompt-index.json` manually:
  ```json
  {"prompts": []}
  ```

**Issue: "Claude API error"**
- Check `ANTHROPIC_API_KEY` is set
- Verify API key is valid
- Check rate limits

**Issue: "Slow search"**
- Add caching (already included!)
- Use embeddings for >500 prompts
- Implement pagination

---

## Resources

- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)
- [Anthropic API Reference](https://docs.anthropic.com)
- [Example Prompts](https://github.com/anthropics/anthropic-cookbook)

---

**Ready to build? Start with /prompt-save and go! 🚀**
