# LLM Engine - Interview Whisperer

## Overview

The LLM Engine is a **Retrieval-Augmented Generation (RAG)** system that generates intelligent interview answers by combining:
- **ChromaDB** for semantic search across user documents
- **Ollama** for embeddings and text generation
- **Smart prompt engineering** with STAR method guidance

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      LLM Engine Pipeline                     │
└─────────────────────────────────────────────────────────────┘

   Interview Question
         │
         ▼
   ┌──────────────┐
   │  Embedding   │  (Ollama nomic-embed-text)
   └──────┬───────┘
         │
         ▼
   ┌──────────────┐
   │  ChromaDB    │  (Query top 3-5 relevant chunks)
   │   Query      │
   └──────┬───────┘
         │
         ▼
   ┌──────────────┐
   │   Format     │  (Remove duplicates, add sources)
   │   Context    │
   └──────┬───────┘
         │
         ▼
   ┌──────────────┐
   │    Build     │  (STAR method, conversational tone)
   │   Prompt     │
   └──────┬───────┘
         │
         ▼
   ┌──────────────┐
   │   Ollama     │  (llama3.1:8b generation)
   │  Generate    │
   └──────┬───────┘
         │
         ▼
   Generated Answer
   + Confidence Score
   + Source Documents
```

## Features

### ✅ Implemented

1. **RAG Pipeline**
   - Semantic search using ChromaDB
   - Context retrieval with similarity scoring
   - Intelligent context formatting

2. **Answer Generation**
   - Standard generation (`generate_answer`)
   - Streaming generation (`stream_answer`) for UI updates
   - STAR method guidance in prompts
   - Temperature-controlled creativity (default 0.7)

3. **Confidence Scoring**
   - Based on similarity scores from ChromaDB
   - Adjusts for answer length and fallback phrases
   - Returns 0.0-1.0 scale

4. **Performance Optimizations**
   - Embedding caching (same question = cached embedding)
   - Batch context retrieval
   - Configurable result counts

5. **Error Handling**
   - Graceful fallback when no context found
   - Clear error messages for Ollama issues
   - Timeout handling for long generations

## Usage

### Basic Usage

```python
from llm_engine import LLMEngine

# Initialize engine
engine = LLMEngine(db_path="../data/chroma_db")

# Ask a question
question = "Tell me about your experience with product management?"
result = engine.generate_answer(question)

print(f"Answer: {result['answer']}")
print(f"Confidence: {result['confidence']:.0%}")
print(f"Sources: {', '.join(result['sources'])}")
```

### Streaming for UI Updates

```python
# Define callback for each token
def on_token(token: str):
    print(token, end='', flush=True)
    # Or update UI with token

# Stream the answer
result = engine.stream_answer(question, on_token)
```

### Custom Configuration

```python
# Use different models
engine = LLMEngine(
    db_path="../data/chroma_db",
    model="llama3.1:8b",           # Generation model
    embed_model="nomic-embed-text"  # Embedding model
)

# Generate with custom parameters
result = engine.generate_answer(
    question=question,
    temperature=0.5,  # More deterministic
    max_tokens=150    # Shorter answers
)
```

### Retrieve Context Only

```python
# Get relevant context without generating answer
context = engine.retrieve_context(question, n_results=5)

for chunk in context:
    print(f"Source: {chunk['source']}")
    print(f"Score: {chunk['score']:.2f}")
    print(f"Text: {chunk['text']}\n")
```

## API Reference

### `LLMEngine.__init__`

```python
def __init__(
    self,
    db_path: str,
    model: str = "llama3.1:8b",
    embed_model: str = "nomic-embed-text",
    collection_name: str = "interview_context"
)
```

**Parameters:**
- `db_path`: Path to ChromaDB database
- `model`: Ollama model for text generation
- `embed_model`: Ollama model for embeddings
- `collection_name`: ChromaDB collection name

**Raises:**
- `RuntimeError`: If Ollama not running or ChromaDB inaccessible

### `retrieve_context`

```python
def retrieve_context(
    self,
    question: str,
    n_results: int = 3
) -> List[Dict[str, Any]]
```

**Returns:**
```python
[
    {
        'text': str,       # Document chunk text
        'source': str,     # Source filename
        'score': float,    # Similarity score (0-1)
        'metadata': dict   # Additional metadata
    },
    ...
]
```

### `generate_answer`

```python
def generate_answer(
    self,
    question: str,
    context: Optional[List[Dict]] = None,
    temperature: float = 0.7,
    max_tokens: int = 250
) -> Dict[str, Any]
```

**Returns:**
```python
{
    'answer': str,           # Generated answer
    'confidence': float,     # 0.0-1.0
    'sources': List[str],    # Source filenames
    'context_used': bool,    # Whether context was found
    'generation_time': float # Seconds taken
}
```

### `stream_answer`

```python
def stream_answer(
    self,
    question: str,
    callback: Callable[[str], None],
    context: Optional[List[Dict]] = None,
    temperature: float = 0.7,
    max_tokens: int = 250
) -> Dict[str, Any]
```

**Parameters:**
- `callback`: Function called with each token: `callback(token: str)`

**Returns:** Same as `generate_answer`

### `get_confidence_score`

```python
def get_confidence_score(
    self,
    question: str,
    answer: str,
    context: Optional[List[Dict]] = None
) -> float
```

**Scoring Logic:**
- High similarity (≥0.7) → ~85% confidence
- Medium similarity (0.5-0.7) → ~65% confidence
- Low similarity (0.3-0.5) → ~45% confidence
- Very low (<0.3) → ~25% confidence
- Adjusted for answer length and fallback phrases

### `get_stats`

```python
def get_stats(self) -> Dict[str, Any]
```

**Returns:**
```python
{
    'model': str,
    'embed_model': str,
    'collection_name': str,
    'document_count': int,
    'cache_size': int,
    'db_path': str
}
```

## Prompt Engineering

### Main Prompt Template

```
You are helping during a job interview. Based on the context from
the candidate's documents, provide a concise, natural answer.

Context from candidate's resume and notes:
{context}

Interview Question: "{question}"

Instructions:
- Use STAR method (Situation, Task, Action, Result) if applicable
- Keep answer to 2-3 sentences (60-90 seconds when spoken)
- Be specific and reference actual experience from the context
- Sound natural and conversational (not robotic)
- If the context doesn't contain relevant information, say
  "I don't have specific experience with that, but here's a
  related example..."

Answer:
```

### Fallback Prompt (No Context)

```
You are helping during a job interview. The candidate doesn't
have specific documented experience for this question.

Interview Question: "{question}"

Provide a brief, professional response acknowledging the gap
while demonstrating willingness to learn. Keep it to 1-2 sentences.

Answer:
```

## Configuration

All settings are centralized in `config.py`:

```python
# Ollama settings
OLLAMA_LLM_MODEL = "llama3.1:8b"
OLLAMA_EMBED_MODEL = "nomic-embed-text"
OLLAMA_HOST = "http://localhost:11434"

# ChromaDB settings
CHROMA_COLLECTION_NAME = "interview_context"
CHROMA_DB_DIR = DATA_DIR / "chroma_db"
```

## Performance

### Optimization Strategies

1. **Embedding Caching**
   - Same question → Cached embedding
   - Cache cleared with `engine.clear_cache()`

2. **Context Retrieval**
   - Default: Top 3 chunks (configurable)
   - Deduplication of similar chunks
   - Fast similarity search via ChromaDB

3. **Generation**
   - Max tokens: 250 (configurable)
   - Stop tokens: `['\n\n', 'Question:', 'Interview Question:']`
   - Temperature: 0.7 (balanced creativity)

### Typical Performance

- Context retrieval: ~100-200ms
- Answer generation: ~2-5s (depends on answer length)
- Streaming: ~50-100 tokens/second

## Error Handling

### Common Errors and Solutions

#### Ollama Not Running

```
RuntimeError: Ollama is not running or not accessible.
Please start Ollama with: ollama serve
```

**Solution:** Start Ollama in a terminal:
```bash
ollama serve
```

#### No Documents in Database

```
Warning: ChromaDB collection is empty. Please run document processor first.
```

**Solution:** Process documents first:
```bash
python app/document_processor.py
```

#### Model Not Found

```
Warning: Model llama3.1:8b not found. Pulling model...
```

**Solution:** Wait for auto-pull, or manually:
```bash
ollama pull llama3.1:8b
ollama pull nomic-embed-text
```

#### Generation Timeout

The engine handles timeouts gracefully with fallback messages.

## Testing

### Run Unit Tests

```bash
python app/test_llm_engine.py
```

### Run Full Integration Test

```bash
python -m app.llm_engine
```

This will:
1. Initialize the engine
2. Test standard generation on 5 questions
3. Test streaming generation
4. Test context retrieval
5. Display statistics

### Example Output

```
❓ Question: Tell me about your experience with product management?
──────────────────────────────────────────────────────────
💡 Answer: I have extensive experience in product management,
having led the development of multiple B2B SaaS products. At my
previous role, I managed the entire product lifecycle from
discovery to launch, working closely with engineering and
design teams to deliver features that increased user engagement
by 45%.

📊 Metadata:
   - Confidence: 87%
   - Sources: resume.pdf, project_notes.md
   - Context Used: True
   - Generation Time: 3.42s
```

## Integration with Other Components

### Document Processor

The LLM Engine depends on documents being processed first:

```python
# 1. Process documents (one-time setup)
from document_processor import DocumentProcessor

processor = DocumentProcessor(
    documents_dir="../documents",
    db_path="../data/chroma_db"
)
processor.process_all_documents()

# 2. Use LLM Engine
from llm_engine import LLMEngine

engine = LLMEngine(db_path="../data/chroma_db")
result = engine.generate_answer("Tell me about yourself?")
```

### Launcher Integration

The launcher will use streaming for real-time UI updates:

```python
from llm_engine import LLMEngine

engine = LLMEngine("../data/chroma_db")

def update_ui(token: str):
    # Update text overlay in real-time
    overlay.append_text(token)

result = engine.stream_answer(detected_question, update_ui)
```

## Advanced Usage

### Custom Prompts

You can modify the prompt templates at the module level:

```python
from llm_engine import LLMEngine, PROMPT_TEMPLATE

# Customize prompt
CUSTOM_PROMPT = """Answer this interview question concisely:

Context: {context}
Question: {question}

Answer:"""

# Use custom prompt by modifying module constant
import llm_engine
llm_engine.PROMPT_TEMPLATE = CUSTOM_PROMPT

engine = LLMEngine("../data/chroma_db")
```

### Batch Processing

```python
questions = [
    "Tell me about yourself?",
    "What's your biggest strength?",
    "Why do you want this role?"
]

results = []
for question in questions:
    result = engine.generate_answer(question)
    results.append(result)

# Analyze confidence scores
avg_confidence = sum(r['confidence'] for r in results) / len(results)
print(f"Average confidence: {avg_confidence:.0%}")
```

### Context Pre-fetching

```python
# Retrieve context once, use multiple times
question = "Tell me about your leadership experience?"
context = engine.retrieve_context(question, n_results=5)

# Generate with different parameters
conservative = engine.generate_answer(
    question, context=context, temperature=0.3
)
creative = engine.generate_answer(
    question, context=context, temperature=0.9
)
```

## Troubleshooting

### Low Confidence Scores

**Possible causes:**
- Documents don't contain relevant information
- Question is too vague or broad
- ChromaDB collection needs rebuilding

**Solutions:**
- Add more documents to `documents/` directory
- Reprocess documents: `python app/document_processor.py`
- Rephrase question to be more specific

### Slow Generation

**Possible causes:**
- Large context chunks
- Slow Ollama model
- CPU-only inference

**Solutions:**
- Reduce `n_results` in `retrieve_context`
- Use smaller Ollama model (e.g., `llama3.1:7b`)
- Lower `max_tokens` parameter
- Consider GPU acceleration for Ollama

### Generic Answers

**Possible causes:**
- No relevant context found
- Fallback prompt being used

**Solutions:**
- Check `context_used` in results
- Inspect retrieved context: `retrieve_context(question)`
- Add more diverse documents

## Future Enhancements

- [ ] Multi-language support
- [ ] Answer caching (cache question → answer pairs)
- [ ] Conversation history (multi-turn interviews)
- [ ] Custom STAR method templates
- [ ] Answer quality scoring
- [ ] A/B testing different prompts
- [ ] Integration with speech synthesis
- [ ] Real-time answer refinement

## Contributing

When modifying the LLM Engine:

1. Run unit tests: `python app/test_llm_engine.py`
2. Test with real documents
3. Verify confidence scores are reasonable
4. Update this documentation
5. Add docstrings to new methods

## License

Part of Interview Whisperer project.

---

**Last Updated:** November 13, 2025
**Version:** 1.0.0
**Status:** Production-ready
