# Claude Mail - Suggested Project Structure

## Recommended Tech Stack

```
Backend:
- Python 3.11+
- Claude Sonnet 4.5 API (Anthropic SDK)
- SQLite/PostgreSQL (memory persistence)
- FastAPI (if building API)

Frontend (Phase 2+):
- React/Next.js
- TailwindCSS
- Shadcn/UI components

CLI (MVP):
- Click or Typer (Python CLI framework)
- Rich (beautiful terminal output)
```

## Project Directory Structure

```
claude-mail/
├── README.md
├── .env.example
├── pyproject.toml
├── requirements.txt
│
├── src/
│   ├── __init__.py
│   ├── main.py                    # CLI entry point
│   │
│   ├── nodes/
│   │   ├── __init__.py
│   │   ├── audience_mapper.py     # Psychographic analysis
│   │   ├── offer_decoder.py       # Service/offer analysis
│   │   ├── prompt_maestro.py      # Core email generation
│   │   ├── tone_calibrator.py     # Tone adjustment
│   │   ├── campaign_sequencer.py  # Email sequencing logic
│   │   └── memory_node.py         # Memory management
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── claude_client.py       # Sonnet 4.5 API wrapper
│   │   ├── config.py              # Configuration management
│   │   ├── prompts.py             # Prompt templates
│   │   └── types.py               # Type definitions
│   │
│   ├── memory/
│   │   ├── __init__.py
│   │   ├── store.py               # Memory storage interface
│   │   ├── sqlite_store.py        # SQLite implementation
│   │   ├── vector_store.py        # Vector embeddings (future)
│   │   └── schemas.py             # Database schemas
│   │
│   ├── data/
│   │   ├── __init__.py
│   │   ├── input_parser.py        # Parse user inputs
│   │   ├── web_research.py        # Public data gathering
│   │   └── validators.py          # Input validation
│   │
│   ├── output/
│   │   ├── __init__.py
│   │   ├── formatters.py          # Output formatting
│   │   ├── exporters.py           # CSV/JSON export
│   │   └── templates.py           # Email templates
│   │
│   └── utils/
│       ├── __init__.py
│       ├── logger.py              # Logging utilities
│       ├── helpers.py             # Helper functions
│       └── analytics.py           # Usage tracking
│
├── tests/
│   ├── __init__.py
│   ├── test_nodes/
│   ├── test_memory/
│   ├── test_core/
│   └── fixtures/
│
├── docs/
│   ├── PRODUCT_RESEARCH.md        # ✅ Already created
│   ├── QUICK_SUMMARY.md           # ✅ Already created
│   ├── API.md                     # API documentation
│   ├── PROMPTS.md                 # Prompt engineering docs
│   └── USER_GUIDE.md              # User documentation
│
├── examples/
│   ├── sample_icp.json
│   ├── sample_offer.json
│   ├── sample_campaign.json
│   └── outputs/
│
├── scripts/
│   ├── setup_db.py                # Initialize database
│   ├── seed_data.py               # Seed sample data
│   └── migrate.py                 # Database migrations
│
└── assets/
    ├── prompts/                   # Prompt templates
    ├── examples/                  # Example campaigns
    └── resources/                 # Case studies, insights
```

## Key Files to Create First (MVP)

### 1. Configuration
```bash
.env.example
pyproject.toml
requirements.txt
```

### 2. Core Infrastructure
```bash
src/core/claude_client.py         # Anthropic API wrapper
src/core/prompts.py                # Prompt templates
src/core/config.py                 # Config loader
```

### 3. Memory System
```bash
src/memory/store.py                # Abstract interface
src/memory/sqlite_store.py         # SQLite implementation
src/memory/schemas.py              # DB schemas
```

### 4. Node Implementations
```bash
src/nodes/audience_mapper.py       # Priority 1
src/nodes/offer_decoder.py         # Priority 1
src/nodes/prompt_maestro.py        # Priority 1
src/nodes/memory_node.py           # Priority 1
src/nodes/tone_calibrator.py       # Priority 2
src/nodes/campaign_sequencer.py    # Priority 2
```

### 5. CLI Interface
```bash
src/main.py                        # CLI entry point
src/output/formatters.py           # Terminal output
```

### 6. Testing
```bash
tests/test_memory/test_store.py
tests/test_nodes/test_audience_mapper.py
tests/fixtures/sample_data.py
```

## Database Schema (SQLite for MVP)

```sql
-- Campaigns table
CREATE TABLE campaigns (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    icp_data JSON NOT NULL,
    offer_data JSON NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Leads table
CREATE TABLE leads (
    id TEXT PRIMARY KEY,
    campaign_id TEXT NOT NULL,
    name TEXT,
    company TEXT,
    profile_data JSON,
    psychographic_analysis JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (campaign_id) REFERENCES campaigns(id)
);

-- Emails table
CREATE TABLE emails (
    id TEXT PRIMARY KEY,
    lead_id TEXT NOT NULL,
    campaign_id TEXT NOT NULL,
    sequence_number INTEGER NOT NULL,
    subject TEXT NOT NULL,
    body TEXT NOT NULL,
    assets_shared JSON,
    tone_profile JSON,
    status TEXT DEFAULT 'draft',
    sent_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (lead_id) REFERENCES leads(id),
    FOREIGN KEY (campaign_id) REFERENCES campaigns(id)
);

-- Memory entries (for novelty tracking)
CREATE TABLE memory_entries (
    id TEXT PRIMARY KEY,
    lead_id TEXT NOT NULL,
    entry_type TEXT NOT NULL, -- 'asset_shared', 'insight_mentioned', 'topic_covered'
    content TEXT NOT NULL,
    email_id TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (lead_id) REFERENCES leads(id),
    FOREIGN KEY (email_id) REFERENCES emails(id)
);

-- Asset library
CREATE TABLE assets (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    asset_type TEXT NOT NULL, -- 'case_study', 'insight', 'tool', 'calculator'
    content TEXT,
    url TEXT,
    tags JSON,
    usage_count INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Performance tracking (Phase 3)
CREATE TABLE performance_metrics (
    id TEXT PRIMARY KEY,
    email_id TEXT NOT NULL,
    opened BOOLEAN DEFAULT FALSE,
    replied BOOLEAN DEFAULT FALSE,
    clicked BOOLEAN DEFAULT FALSE,
    converted BOOLEAN DEFAULT FALSE,
    reply_sentiment TEXT,
    tracked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (email_id) REFERENCES emails(id)
);
```

## CLI Commands (MVP)

```bash
# Initialize project
claude-mail init

# Create new campaign
claude-mail campaign create --name "Q1 Outreach"

# Add ICP definition
claude-mail icp add --campaign "Q1 Outreach" --file icp.json

# Add offer/service
claude-mail offer add --campaign "Q1 Outreach" --file offer.json

# Add leads
claude-mail leads add --campaign "Q1 Outreach" --file leads.csv

# Generate campaign
claude-mail generate --campaign "Q1 Outreach" --output ./output

# View memory for lead
claude-mail memory show --lead-id abc123

# Export campaign
claude-mail export --campaign "Q1 Outreach" --format csv

# Stats
claude-mail stats --campaign "Q1 Outreach"
```

## Environment Variables

```bash
# .env.example
ANTHROPIC_API_KEY=your_api_key_here
DATABASE_URL=sqlite:///claude_mail.db
LOG_LEVEL=INFO
MAX_EMAILS_PER_CAMPAIGN=7
DEFAULT_TONE=professional
ENABLE_ANALYTICS=false
```

## Development Workflow

```bash
# Setup
git clone <repo>
cd claude-mail
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"

# Initialize database
python scripts/setup_db.py

# Run tests
pytest

# Run CLI
claude-mail --help

# Development mode
python -m src.main --debug
```

## Next Steps

1. **Set up project skeleton** (directories, pyproject.toml)
2. **Implement core Claude client** (src/core/claude_client.py)
3. **Build memory system** (src/memory/)
4. **Create first node** (src/nodes/audience_mapper.py)
5. **Wire up CLI** (src/main.py)
6. **Test end-to-end** with sample data
7. **Iterate on prompts** for quality

---

Ready to start building? Let me know if you want me to:
1. Generate the initial project structure
2. Create the core files
3. Write the first node implementation
4. Set up the database schema
