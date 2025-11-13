# Document Processor

Robust document processing system for Interview Whisperer that extracts text from documents, creates intelligent chunks, generates embeddings, and stores them in ChromaDB for semantic search.

## Features

- **Multi-format Support**: PDF, DOCX, TXT, MD
- **Smart Chunking**: Respects sentence boundaries with configurable overlap
- **Semantic Embeddings**: Uses Ollama's nomic-embed-text model
- **Vector Storage**: ChromaDB for efficient similarity search
- **Error Handling**: Gracefully handles corrupted files and missing dependencies
- **Progress Tracking**: Real-time progress callbacks
- **Logging**: Comprehensive logging to data/logs/

## Quick Start

### 1. Install Dependencies

```bash
pip install PyPDF2 python-docx chromadb ollama
```

### 2. Install Ollama

```bash
# Install Ollama (see https://ollama.ai)
# Linux:
curl -fsSL https://ollama.ai/install.sh | sh

# macOS:
brew install ollama

# Windows:
# Download from https://ollama.ai
```

### 3. Pull Embedding Model

```bash
ollama pull nomic-embed-text
```

### 4. Add Documents

Place your documents in `/home/user/interview-whisperer/documents/`:

```
documents/
├── resume.pdf
├── job_description.docx
├── company_research.txt
└── interview_notes.md
```

### 5. Process Documents

```python
from document_processor import DocumentProcessor

# Initialize
processor = DocumentProcessor(
    documents_dir="../documents",
    db_path="../data/chroma_db"
)

# Process all documents
def progress(current, total, msg):
    print(f"[{current}/{total}] {msg}")

results = processor.process_all_documents(progress_callback=progress)
print(f"Processed {results['processed_files']} files, {results['total_chunks']} chunks")
```

Or use the test script:

```bash
cd /home/user/interview-whisperer/app
python test_processor.py
```

## Usage

### Basic Processing

```python
from document_processor import DocumentProcessor

processor = DocumentProcessor("../documents", "../data/chroma_db")

# Scan for documents
documents = processor.scan_documents()
print(f"Found {len(documents)} documents")

# Process all
stats = processor.process_all_documents()
print(stats)
```

### Query Similar Content

```python
# Search for relevant chunks
results = processor.query_similar(
    query_text="What are the key PM frameworks?",
    n_results=5
)

for result in results:
    print(f"File: {result['metadata']['file_name']}")
    print(f"Content: {result['document'][:200]}...")
    print(f"Distance: {result['distance']}\n")
```

### Custom Chunking

```python
# Extract and chunk manually
text = processor.extract_text("path/to/file.pdf")
chunks = processor.chunk_text(
    text,
    chunk_size=500,  # words per chunk
    overlap=50       # overlap between chunks
)
```

### Database Management

```python
# Get statistics
stats = processor.get_stats()
print(f"Total chunks: {stats['total_chunks']}")
print(f"Files processed: {stats['files_processed']}")
print(f"Last updated: {stats['last_updated']}")

# Clear database (re-processing)
processor.clear_database()
```

## Architecture

### Processing Pipeline

```
1. Scan Documents
   ↓
2. Extract Text (PDF/DOCX/TXT/MD)
   ↓
3. Smart Chunking (sentence-aware)
   ↓
4. Generate Embeddings (Ollama)
   ↓
5. Store in ChromaDB (with metadata)
```

### Smart Chunking

The chunker respects sentence boundaries and creates overlapping chunks for better context:

```python
# Example: chunk_size=500, overlap=50
Chunk 1: [words 1-500]
Chunk 2: [words 451-950]  # 50-word overlap from chunk 1
Chunk 3: [words 901-1400] # 50-word overlap from chunk 2
```

Benefits:
- Preserves sentence integrity
- Maintains context across chunk boundaries
- Better embedding quality
- Improved search accuracy

### Metadata Structure

Each chunk stores:

```python
{
    'file_name': 'resume.pdf',
    'file_type': '.pdf',
    'chunk_id': 0,              # Chunk number within file
    'total_chunks': 12,         # Total chunks for this file
    'processed_at': '2025-11-13T00:00:00'
}
```

## API Reference

### DocumentProcessor Class

#### `__init__(documents_dir, db_path)`
Initialize the processor.

**Parameters:**
- `documents_dir` (str): Path to documents folder
- `db_path` (str): Path to ChromaDB storage

#### `scan_documents() -> List[Dict]`
Scan for supported documents.

**Returns:**
- List of document metadata dictionaries

#### `extract_text(file_path) -> Optional[str]`
Extract text from a file.

**Parameters:**
- `file_path` (str): Path to file

**Returns:**
- Extracted text or None if failed

#### `chunk_text(text, chunk_size=500, overlap=50) -> List[str]`
Split text into intelligent chunks.

**Parameters:**
- `text` (str): Text to chunk
- `chunk_size` (int): Target words per chunk
- `overlap` (int): Words to overlap between chunks

**Returns:**
- List of text chunks

#### `create_embeddings(chunks) -> Optional[List[List[float]]]`
Generate embeddings using Ollama.

**Parameters:**
- `chunks` (List[str]): Text chunks

**Returns:**
- List of embedding vectors or None if failed

#### `store_chunks(chunks, embeddings, metadata) -> bool`
Store chunks in ChromaDB.

**Parameters:**
- `chunks` (List[str]): Text chunks
- `embeddings` (List[List[float]]): Embedding vectors
- `metadata` (Dict): File metadata

**Returns:**
- True if successful

#### `process_all_documents(progress_callback=None) -> Dict`
Process all documents in the documents directory.

**Parameters:**
- `progress_callback` (Callable): Optional callback(current, total, message)

**Returns:**
- Statistics dictionary

#### `query_similar(query_text, n_results=5) -> List[Dict]`
Query for similar documents.

**Parameters:**
- `query_text` (str): Query text
- `n_results` (int): Number of results

**Returns:**
- List of similar documents with metadata

#### `get_stats() -> Dict`
Get database statistics.

**Returns:**
- Statistics dictionary

#### `clear_database() -> bool`
Clear all documents from database.

**Returns:**
- True if successful

## Error Handling

The processor handles errors gracefully:

### Corrupted Files
```python
# Skips corrupted files, logs error, continues processing
results = processor.process_all_documents()
if results['errors']:
    for error in results['errors']:
        print(f"Error: {error}")
```

### Missing Ollama
```python
# Clear error message if Ollama not running
embeddings = processor.create_embeddings(chunks)
if not embeddings:
    print("Make sure Ollama is running!")
    print("Run: ollama pull nomic-embed-text")
```

### Encoding Issues
```python
# Tries multiple encodings for text files
# Falls back gracefully if all fail
text = processor.extract_text("problematic.txt")
```

## Logging

Logs are stored in `/home/user/interview-whisperer/data/logs/`:

```
data/logs/
└── document_processor_20251113.log
```

Log format:
```
2025-11-13 00:00:00,000 - document_processor - INFO - Processed file.pdf (5 chunks)
2025-11-13 00:00:01,000 - document_processor - ERROR - Failed to extract text from corrupt.pdf
```

## Performance

### Benchmarks

| Operation | Time | Notes |
|-----------|------|-------|
| PDF extraction (10 pages) | ~1s | Depends on complexity |
| DOCX extraction (5000 words) | ~0.3s | Fast |
| Chunking (10,000 words) | ~0.1s | Very fast |
| Embedding (1 chunk) | ~0.5s | Depends on Ollama |
| ChromaDB storage (100 chunks) | ~0.2s | Fast |

### Optimization Tips

1. **Batch Processing**: Process multiple files at once
2. **Chunk Size**: Larger chunks = fewer embeddings = faster
3. **Ollama GPU**: Use GPU-accelerated Ollama for faster embeddings
4. **Parallel Processing**: Can be extended for parallel embedding generation

## Troubleshooting

### "No module named 'PyPDF2'"
```bash
pip install PyPDF2 python-docx chromadb ollama
```

### "Ollama embedding generation failed"
```bash
# Check Ollama is running
ollama list

# Pull the model
ollama pull nomic-embed-text

# Test manually
ollama run nomic-embed-text "test"
```

### "Failed to extract text from PDF"
- PDF might be scanned images (needs OCR)
- PDF might be corrupted
- Try opening in PDF viewer to verify

### "ChromaDB initialization failed"
- Check directory permissions
- Ensure path exists
- Check disk space

## Testing

Run the comprehensive test:

```bash
cd /home/user/interview-whisperer/app
python test_processor.py
```

Test individual components:

```bash
# Test without Ollama (extraction + chunking only)
python document_processor.py

# Clear database
python test_processor.py --clear
```

## Integration Example

### Interview Whisperer Integration

```python
from document_processor import DocumentProcessor

class InterviewAssistant:
    def __init__(self):
        self.processor = DocumentProcessor(
            documents_dir="./documents",
            db_path="./data/chroma_db"
        )

    def get_context(self, question: str) -> str:
        """Get relevant context for interview question."""
        results = self.processor.query_similar(question, n_results=3)

        context = "Relevant information:\n"
        for result in results:
            context += f"\n{result['document']}\n"

        return context

    def answer_question(self, question: str) -> str:
        """Answer question using retrieved context."""
        context = self.get_context(question)

        # Pass to LLM with context
        prompt = f"""
        Context: {context}

        Question: {question}

        Answer:
        """

        # return llm.generate(prompt)
        return context  # For demo
```

## Future Enhancements

- [ ] OCR support for scanned PDFs
- [ ] Parallel embedding generation
- [ ] Incremental updates (only process new/changed files)
- [ ] File deduplication
- [ ] Multi-language support
- [ ] Custom embedding models
- [ ] Web scraping integration
- [ ] Image extraction from PDFs

## License

Part of Interview Whisperer project.

## Support

For issues or questions:
1. Check troubleshooting section
2. Review logs in data/logs/
3. Test with sample documents
4. Verify Ollama is running
