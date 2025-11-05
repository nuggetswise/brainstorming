# PM Research Suite for Claude Code

**Replace Dovetail ($1,000+/month) and UserTesting ($300+/month) with Claude Code commands**

## Overview

The PM Research Suite is a collection of slash commands and AI agents for product managers to perform qualitative research analysis, feedback synthesis, and feature prioritization—all within Claude Code.

### What's Included

- **8 Slash Commands** for common PM research workflows
- **3 Specialized Agents** for deep analysis
- **Example datasets** to test commands
- **Documentation** and best practices

### Cost Savings

- **Dovetail**: Save $1,000-12,000/year
- **UserTesting**: Save $3,600+/year
- **ProductBoard prioritization**: Save $7,000+/year
- **Total**: $11,600-22,600/year

### Requirements

- Claude Pro subscription (for Claude Code access)
- Basic understanding of product management
- Research data (interviews, surveys, feedback)

---

## Installation

### Option 1: Copy to Project (Recommended)

```bash
# Clone or download this repository
git clone https://github.com/yourusername/claude-code-pm-research-suite

# Copy to your project
cp -r claude-code-pm-research-suite/.claude ~/your-project/

# Start Claude Code in your project
cd ~/your-project
claude
```

### Option 2: Install Globally

```bash
# Copy commands to global Claude Code directory
cp -r claude-code-pm-research-suite/.claude/commands/* ~/.claude/commands/

# Copy agents
cp -r claude-code-pm-research-suite/.claude/agents/* ~/.claude/agents/

# Now available in any project!
```

### Option 3: Plugin (Future)

```bash
# Once packaged as plugin
> /plugin install pm-research-suite
```

---

## Commands Overview

### 1. `/pm/interview-analysis`
Analyze user interview transcripts to extract themes and insights.

**Input**: Transcript file or pasted text
**Output**: Thematic analysis with quotes, insights, recommendations
**Time**: 2-5 minutes
**Replaces**: Dovetail analysis features

**Example**:
```bash
> /pm/interview-analysis interviews/user-005.txt
```

### 2. `/pm/feedback-synthesis`
Synthesize insights from multiple feedback sources.

**Input**: Multiple files (interviews, surveys, tickets)
**Output**: Cross-source pattern analysis, priorities
**Time**: 3-7 minutes
**Replaces**: Dovetail synthesis, manual spreadsheet work

**Example**:
```bash
> /pm/feedback-synthesis feedback/january-2025/*
```

### 3. `/pm/persona-builder`
Generate data-driven user personas from research.

**Input**: Research files or synthesis report
**Output**: Detailed persona document with goals, pain points, behaviors
**Time**: 3-5 minutes
**Replaces**: Manual persona creation

**Example**:
```bash
> /pm/persona-builder --from feedback-synthesis.md
```

### 4. `/pm/insight-extraction`
Extract key insights from research documents.

**Input**: Any research document
**Output**: Bulleted insights with evidence
**Time**: 1-2 minutes
**Replaces**: Manual highlighting and note-taking

**Example**:
```bash
> /pm/insight-extraction research-report.md
```

### 5. `/pm/journey-map`
Create customer journey maps from qualitative data.

**Input**: Research about user workflows
**Output**: Journey map with stages, actions, pain points, opportunities
**Time**: 3-5 minutes
**Replaces**: Manual journey mapping workshops

**Example**:
```bash
> /pm/journey-map "onboarding flow" --from interviews/*.txt
```

### 6. `/pm/usability-report`
Generate usability test reports.

**Input**: Usability test notes or recordings
**Output**: Issues by severity, recommendations
**Time**: 3-5 minutes
**Replaces**: Manual report writing

**Example**:
```bash
> /pm/usability-report tests/checkout-flow-v2.txt
```

### 7. `/pm/competitive-analysis`
Analyze competitor features and positioning.

**Input**: Competitor names or research notes
**Output**: Feature comparison, gaps, opportunities
**Time**: 2-4 minutes
**Replaces**: Manual competitive spreadsheets

**Example**:
```bash
> /pm/competitive-analysis "Notion, Coda, ClickUp" --focus "collaboration features"
```

### 8. `/pm/feature-prioritization`
Prioritize features using RICE or ICE scoring.

**Input**: List of features or feedback file
**Output**: Scored priorities with roadmap recommendations
**Time**: 3-7 minutes
**Replaces**: Productboard/Aha! prioritization

**Example**:
```bash
> /pm/feature-prioritization "Dark mode, SSO, API limits, Bulk actions"
```

---

## Agents Overview

### 1. Research Analyst Agent
**Specialization**: Deep qualitative analysis using academic methodologies

**Use when**: You need rigorous thematic analysis following best practices

**Invoke**:
```bash
> Use the research-analyst agent to analyze interviews/*.txt
```

### 2. Insight Synthesizer Agent
**Specialization**: Pattern recognition across diverse data sources

**Use when**: You have multiple data types and need cross-cutting insights

**Invoke**:
```bash
> Use the insight-synthesizer agent to find patterns in feedback/
```

### 3. Persona Generator Agent
**Specialization**: Creating realistic, data-driven user personas

**Use when**: You need detailed personas for design/development teams

**Invoke**:
```bash
> Use the persona-generator agent to create persona from synthesis.md
```

---

## Quick Start Guide

### Your First Analysis (5 minutes)

1. **Get some data**: Have an interview transcript or feedback ready

2. **Analyze interview**:
   ```bash
   > /pm/interview-analysis path/to/transcript.txt
   ```

3. **Review output**: Claude will provide themes, quotes, insights

4. **Extract priorities**:
   ```bash
   > /pm/feature-prioritization --from interview-analysis.md
   ```

5. **Done!** You just replaced a $100 Dovetail workflow

### Multi-Source Synthesis (10 minutes)

1. **Gather feedback** in a folder: `feedback/`

2. **Synthesize**:
   ```bash
   > /pm/feedback-synthesis feedback/*
   ```

3. **Build persona**:
   ```bash
   > /pm/persona-builder --from feedback-synthesis.md
   ```

4. **Prioritize features**:
   ```bash
   > /pm/feature-prioritization --from feedback-synthesis.md
   ```

5. **Create journey map**:
   ```bash
   > /pm/journey-map "user onboarding" --from feedback-synthesis.md
   ```

---

## Best Practices

### Data Preparation

✅ **Do**:
- Use plain text files (.txt, .md)
- Label speakers in transcripts (Interviewer: / Participant:)
- Include date and context metadata
- Keep raw transcripts unedited

❌ **Don't**:
- Use PDFs or Word docs (convert first)
- Mix multiple interviews in one file
- Edit transcripts to fit narratives
- Remove "negative" feedback

### Analysis Workflow

1. **Start specific** → **Go broad**:
   - Analyze individual interviews first
   - Then synthesize across all sources
   - Finally, create artifacts (personas, journey maps)

2. **Iterate**:
   - Run commands multiple times with different focuses
   - Refine based on output
   - Ask for deeper analysis if needed

3. **Document**:
   - Save command outputs as markdown files
   - Commit to git for version control
   - Share with team via GitHub/Notion

### Pro Tips

- **Use file patterns**: `feedback/interviews-*.txt` for batch processing
- **Add focus areas**: Commands accept custom focus instructions
- **Chain commands**: Output of one command feeds into another
- **Save favorites**: Copy frequently-used commands to project root
- **Customize prompts**: Edit `.claude/commands/*.md` to fit your needs

---

## Example Workflows

### Workflow 1: User Interview Analysis

```bash
# 1. Analyze individual interviews
> /pm/interview-analysis interviews/user-001.txt
> /pm/interview-analysis interviews/user-002.txt
> /pm/interview-analysis interviews/user-003.txt

# 2. Synthesize across all interviews
> /pm/feedback-synthesis interviews/*.txt

# 3. Create persona from synthesis
> /pm/persona-builder --from feedback-synthesis.md

# 4. Identify features to build
> /pm/feature-prioritization --from feedback-synthesis.md

# 5. Map journey
> /pm/journey-map "checkout flow" --from interviews/*.txt
```

**Time**: 15-20 minutes
**Replaces**: 4-8 hours of manual work + $100 Dovetail cost

### Workflow 2: Competitive Analysis

```bash
# 1. Analyze competitors
> /pm/competitive-analysis "Slack, Teams, Discord" --focus "pricing and features"

# 2. Identify gaps
> /pm/insight-extraction competitive-analysis.md "focus on gaps in market"

# 3. Prioritize opportunities
> /pm/feature-prioritization --from competitive-analysis.md
```

**Time**: 10 minutes
**Replaces**: Hours of research + spreadsheet creation

### Workflow 3: Feature Prioritization from Feedback

```bash
# 1. Gather all feedback
> /pm/feedback-synthesis feedback/*.txt support-tickets.csv reviews.txt

# 2. Extract feature requests
> /pm/insight-extraction feedback-synthesis.md "focus on feature requests"

# 3. Prioritize with RICE
> /pm/feature-prioritization --from feedback-synthesis.md

# 4. Create roadmap visualization
> /pm/journey-map "feature implementation roadmap" --from prioritization.md
```

**Time**: 15 minutes
**Replaces**: ProductBoard workflow ($70K/year)

---

## Customization

### Edit Commands

Commands are markdown files in `.claude/commands/pm/`. Edit them to:
- Change output format
- Add custom sections
- Include company-specific frameworks
- Adjust analysis depth

**Example**: Add your prioritization formula
```markdown
# Edit: .claude/commands/pm/feature-prioritization.md

## Custom Scoring
Use [CompanyName]'s proprietary formula:
Score = (UserVotes × 2) + (RevenueImpact × 3) + (StrategicFit × 1)
```

### Create New Commands

```bash
# Create new command file
touch .claude/commands/pm/my-custom-command.md

# Edit with your prompt
# Save and use:
> /pm/my-custom-command
```

### Combine with MCP Servers

Enhance commands with external data:

```json
// claude_desktop_config.json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@notionhq/client"],
      "env": {
        "NOTION_TOKEN": "your-token"
      }
    }
  }
}
```

Now commands can read/write to Notion automatically!

---

## Troubleshooting

### Command not found

**Issue**: `/pm/interview-analysis` not showing up

**Fix**:
```bash
# Check .claude directory exists
ls -la .claude/commands/pm/

# Restart Claude Code
# Type / to see all commands
```

### Poor analysis quality

**Issue**: Output is too generic

**Fix**:
- Provide more context in input
- Use richer data (full transcripts, not summaries)
- Try specialized agents for deep analysis
- Add focus instructions: `/pm/command "focus on X"`

### Large file handling

**Issue**: Transcript too large

**Fix**:
```bash
# Split into chunks
split -l 500 large-transcript.txt chunk-

# Analyze separately
> /pm/interview-analysis chunk-*

# Then synthesize
> /pm/feedback-synthesis analysis-*.md
```

---

## Roadmap

### v1.0 (Current)
- [x] 8 core PM commands
- [x] 3 specialized agents
- [x] Documentation and examples

### v1.1 (Next Month)
- [ ] Journey map visualization (Mermaid diagrams)
- [ ] Persona templates with images
- [ ] Integration with Linear/GitHub for feature tracking
- [ ] Export to Notion/Confluence

### v1.2 (Q2 2025)
- [ ] Video/audio transcription with Whisper MCP
- [ ] Sentiment analysis across feedback
- [ ] Competitive intelligence automation
- [ ] Template library for different industries

### v2.0 (Q3 2025)
- [ ] Web dashboard for visualization
- [ ] Team collaboration features
- [ ] Research repository management
- [ ] Advanced ML insights

---

## Community & Support

### Get Help
- **GitHub Issues**: Report bugs or request features
- **Discussions**: Ask questions, share workflows
- **Discord**: Join the community (link)

### Contribute
- Share custom commands
- Improve documentation
- Submit agents
- Report bugs

### Stay Updated
- Watch GitHub repo for releases
- Follow on Twitter: @yourhandle
- Subscribe to newsletter

---

## License

MIT License - Free to use and modify

---

## Credits

Created by [Your Name]
Inspired by expensive PM tools that gatekeep basic workflows
Built with Claude Code and Claude Sonnet 4.5

**Save $11K-22K/year. Research better. Ship faster. 🚀**
