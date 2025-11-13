# Document Processor - Quick Start Guide

## 30-Second Setup

```bash
# 1. Install dependencies
pip install PyPDF2 python-docx chromadb ollama

# 2. Install Ollama (if not already installed)
curl -fsSL https://ollama.ai/install.sh | sh

# 3. Pull embedding model
ollama pull nomic-embed-text

# 4. Add documents
# Drop PDF, DOCX, TXT, or MD files into: /home/user/interview-whisperer/documents/

# 5. Process documents
cd /home/user/interview-whisperer/app
python test_processor.py
```

## Basic Usage

### Python Script

```python
from document_processor import DocumentProcessor

# Initialize
processor = DocumentProcessor(
    documents_dir="../documents",
    db_path="../data/chroma_db"
)

# Process all documents
results = processor.process_all_documents()
print(f"✅ Processed {results['total_chunks']} chunks")

# Search for similar content
results = processor.query_similar("product management frameworks")
for result in results:
    print(result['document'][:100])
```

### Command Line

```bash
# Test the processor
python test_processor.py

# Clear database and reprocess
python test_processor.py --clear
```

## File Support

| Format | Extension | Library | Status |
|--------|-----------|---------|--------|
| PDF | .pdf | PyPDF2 | ✅ Supported |
| Word | .docx | python-docx | ✅ Supported |
| Text | .txt | built-in | ✅ Supported |
| Markdown | .md | built-in | ✅ Supported |

## Common Commands

```python
# Get stats
stats = processor.get_stats()
# Returns: {'total_chunks': X, 'files_processed': Y, 'last_updated': timestamp}

# Scan documents
docs = processor.scan_documents()
# Returns: List of file metadata

# Extract text
text = processor.extract_text("path/to/file.pdf")
# Returns: Extracted text string

# Chunk text
chunks = processor.chunk_text(text, chunk_size=500, overlap=50)
# Returns: List of text chunks

# Query
results = processor.query_similar("interview questions", n_results=5)
# Returns: List of similar chunks with metadata

# Clear database
processor.clear_database()
# Returns: True if successful
```

## Configuration

### Chunking Parameters

```python
chunks = processor.chunk_text(
    text,
    chunk_size=500,  # Words per chunk (default: 500)
    overlap=50       # Overlap words (default: 50)
)
```

**Recommendations:**
- Small docs (< 1000 words): `chunk_size=200, overlap=30`
- Medium docs (1000-5000 words): `chunk_size=500, overlap=50`
- Large docs (> 5000 words): `chunk_size=1000, overlap=100`

### Query Parameters

```python
results = processor.query_similar(
    query_text="your question here",
    n_results=5  # Number of results (default: 5)
)
```

**Recommendations:**
- Quick lookup: `n_results=3`
- Comprehensive search: `n_results=10`
- Balance: `n_results=5` (default)

## Troubleshooting

### No documents found
```bash
ls /home/user/interview-whisperer/documents/
# Make sure files have extensions: .pdf, .docx, .txt, .md
```

### Ollama not available
```bash
# Check if Ollama is running
ollama list

# Start Ollama service
ollama serve &

# Pull model
ollama pull nomic-embed-text
```

### Import errors
```bash
pip install PyPDF2 python-docx chromadb ollama
```

### Permission errors
```bash
# Check directory permissions
ls -la /home/user/interview-whisperer/data/
chmod -R 755 /home/user/interview-whisperer/data/
```

## Directory Structure

```
interview-whisperer/
├── app/
│   ├── document_processor.py      ← Main processor class
│   ├── test_processor.py          ← Test script
│   ├── README_PROCESSOR.md        ← Full documentation
│   └── QUICK_START.md             ← This file
├── documents/                      ← Drop your files here
│   ├── resume.pdf
│   ├── job_description.docx
│   └── interview_notes.md
├── data/
│   ├── chroma_db/                 ← Vector database
│   └── logs/                      ← Processing logs
└── requirements.txt
```

## Next Steps

1. **Add Documents**: Drop files into `documents/` folder
2. **Process**: Run `python test_processor.py`
3. **Query**: Use `processor.query_similar()` to search
4. **Integrate**: Import into your Interview Whisperer app

## Full Documentation

See [README_PROCESSOR.md](README_PROCESSOR.md) for:
- Complete API reference
- Architecture details
- Performance benchmarks
- Integration examples
- Advanced usage
