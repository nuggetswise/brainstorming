# LLM Engine Integration Example

## Complete Workflow: Document Processing → Answer Generation

This example demonstrates the full pipeline from processing documents to generating interview answers.

## Step 1: Setup and Document Processing

```python
#!/usr/bin/env python3
"""
Complete Interview Whisperer workflow example
"""

from pathlib import Path
from document_processor import DocumentProcessor
from llm_engine import LLMEngine

# Configuration
DOCUMENTS_DIR = "../documents"
DB_PATH = "../data/chroma_db"

# Step 1: Process documents (one-time setup)
print("=" * 60)
print("STEP 1: Processing Documents")
print("=" * 60)

processor = DocumentProcessor(
    documents_dir=DOCUMENTS_DIR,
    db_path=DB_PATH
)

# Process all documents in the folder
print("\nProcessing documents...")
results = processor.process_all_documents()

print(f"\n✓ Processed {len(results)} documents")
for result in results:
    if result['success']:
        print(f"  - {result['file']}: {result['chunks_created']} chunks")
    else:
        print(f"  - {result['file']}: FAILED - {result['error']}")
```

## Step 2: Initialize LLM Engine

```python
# Step 2: Initialize LLM Engine
print("\n" + "=" * 60)
print("STEP 2: Initializing LLM Engine")
print("=" * 60)

engine = LLMEngine(db_path=DB_PATH)

# Show stats
stats = engine.get_stats()
print(f"\nEngine Stats:")
print(f"  - Model: {stats['model']}")
print(f"  - Embedding Model: {stats['embed_model']}")
print(f"  - Documents in DB: {stats['document_count']}")
print(f"  - Cache size: {stats['cache_size']}")
```

## Step 3: Generate Interview Answers

```python
# Step 3: Answer interview questions
print("\n" + "=" * 60)
print("STEP 3: Generating Interview Answers")
print("=" * 60)

interview_questions = [
    "Tell me about yourself and your background?",
    "What's your experience with product management?",
    "Describe a challenging project you worked on?",
    "How do you prioritize competing features?",
    "What's your biggest professional achievement?"
]

for i, question in enumerate(interview_questions, 1):
    print(f"\n--- Question {i} ---")
    print(f"❓ {question}")
    print("-" * 60)

    # Generate answer
    result = engine.generate_answer(question)

    # Display answer
    print(f"\n💡 ANSWER:")
    print(f"   {result['answer']}")

    # Display metadata
    print(f"\n📊 METADATA:")
    print(f"   Confidence: {result['confidence']:.0%}")
    print(f"   Sources: {', '.join(result['sources']) if result['sources'] else 'None'}")
    print(f"   Context Found: {'Yes' if result['context_used'] else 'No'}")
    print(f"   Time: {result['generation_time']:.2f}s")

    # Show confidence interpretation
    if result['confidence'] >= 0.8:
        confidence_label = "🟢 HIGH"
    elif result['confidence'] >= 0.5:
        confidence_label = "🟡 MEDIUM"
    else:
        confidence_label = "🔴 LOW"

    print(f"   Confidence Level: {confidence_label}")
```

## Step 4: Interactive Mode

```python
# Step 4: Interactive question answering
print("\n" + "=" * 60)
print("STEP 4: Interactive Mode")
print("=" * 60)

print("\nType your interview questions (or 'quit' to exit):")

while True:
    question = input("\n❓ Question: ").strip()

    if question.lower() in ['quit', 'exit', 'q']:
        print("Goodbye!")
        break

    if not question:
        continue

    # Stream the answer for real-time feel
    print("\n💡 Answer: ", end='', flush=True)

    def stream_callback(token: str):
        print(token, end='', flush=True)

    result = engine.stream_answer(question, stream_callback)

    # Show metadata after answer completes
    print(f"\n\n   (Confidence: {result['confidence']:.0%}, "
          f"Sources: {len(result['sources'])}, "
          f"Time: {result['generation_time']:.2f}s)")
```

## Step 5: Context Inspection (Debug Mode)

```python
# Step 5: Inspect retrieved context (for debugging)
print("\n" + "=" * 60)
print("STEP 5: Context Inspection (Debug)")
print("=" * 60)

debug_question = "What technical skills do you have?"
print(f"\n❓ Question: {debug_question}")
print("-" * 60)

# Retrieve context
context = engine.retrieve_context(debug_question, n_results=5)

print(f"\n📚 Retrieved {len(context)} context chunks:\n")

for i, chunk in enumerate(context, 1):
    print(f"{i}. SOURCE: {chunk['source']}")
    print(f"   SCORE: {chunk['score']:.2f}")
    print(f"   TEXT: {chunk['text'][:200]}...")
    print()

# Generate answer using this context
print("\n💡 Generated Answer:")
result = engine.generate_answer(debug_question, context=context)
print(f"   {result['answer']}")
```

## Real-World Usage: GUI Integration

```python
# Example: Integration with UI overlay

class InterviewOverlay:
    """Mock UI overlay for demonstration."""

    def __init__(self):
        self.engine = LLMEngine("../data/chroma_db")
        self.current_answer = ""

    def on_question_detected(self, question: str):
        """Called when microphone detects a question."""
        print(f"\n🎤 Detected: {question}")

        # Clear previous answer
        self.current_answer = ""

        # Stream answer to overlay
        def update_overlay(token: str):
            self.current_answer += token
            self.display_text(self.current_answer)

        # Generate and display
        result = self.engine.stream_answer(question, update_overlay)

        # Show confidence indicator
        self.show_confidence_indicator(result['confidence'])

    def display_text(self, text: str):
        """Update UI with text."""
        # In real app, this would update GUI widget
        print(f"\r💭 {text}", end='', flush=True)

    def show_confidence_indicator(self, confidence: float):
        """Show confidence level in UI."""
        if confidence >= 0.8:
            color = "🟢 HIGH"
        elif confidence >= 0.5:
            color = "🟡 MEDIUM"
        else:
            color = "🔴 LOW"

        print(f"\n   Confidence: {color} ({confidence:.0%})")

# Usage
overlay = InterviewOverlay()

# Simulate questions being detected
test_questions = [
    "Tell me about your background?",
    "What's your biggest strength?",
    "Why do you want to work here?"
]

for question in test_questions:
    overlay.on_question_detected(question)
    print("\n" + "-" * 60)
```

## Performance Monitoring

```python
# Monitor performance and quality

class PerformanceMonitor:
    """Track LLM Engine performance metrics."""

    def __init__(self, engine: LLMEngine):
        self.engine = engine
        self.history = []

    def ask_question(self, question: str):
        """Ask question and log metrics."""
        result = self.engine.generate_answer(question)

        # Log metrics
        self.history.append({
            'question': question,
            'confidence': result['confidence'],
            'generation_time': result['generation_time'],
            'sources_count': len(result['sources']),
            'context_used': result['context_used']
        })

        return result

    def get_statistics(self):
        """Get aggregate statistics."""
        if not self.history:
            return None

        return {
            'total_questions': len(self.history),
            'avg_confidence': sum(h['confidence'] for h in self.history) / len(self.history),
            'avg_time': sum(h['generation_time'] for h in self.history) / len(self.history),
            'context_hit_rate': sum(1 for h in self.history if h['context_used']) / len(self.history)
        }

    def print_report(self):
        """Print performance report."""
        stats = self.get_statistics()

        print("\n" + "=" * 60)
        print("PERFORMANCE REPORT")
        print("=" * 60)

        print(f"\nTotal Questions: {stats['total_questions']}")
        print(f"Average Confidence: {stats['avg_confidence']:.0%}")
        print(f"Average Generation Time: {stats['avg_time']:.2f}s")
        print(f"Context Hit Rate: {stats['context_hit_rate']:.0%}")

# Usage
monitor = PerformanceMonitor(engine)

questions = [
    "Tell me about yourself?",
    "What's your experience with Python?",
    "Describe a challenging project?"
]

for q in questions:
    result = monitor.ask_question(q)
    print(f"✓ {q[:50]}... (Confidence: {result['confidence']:.0%})")

monitor.print_report()
```

## Error Handling Example

```python
# Robust error handling for production

def safe_answer_generation(engine: LLMEngine, question: str):
    """Generate answer with comprehensive error handling."""

    try:
        # Attempt to generate answer
        result = engine.generate_answer(question)

        # Check if answer quality is acceptable
        if result['confidence'] < 0.3:
            print("⚠️  Warning: Low confidence answer")
            print("   Consider rephrasing question or adding more documents")

        if not result['context_used']:
            print("⚠️  Warning: No relevant context found")
            print("   Answer is based on general knowledge only")

        if result['generation_time'] > 10.0:
            print("⚠️  Warning: Slow generation (>10s)")
            print("   Consider optimizing or using smaller model")

        return result

    except RuntimeError as e:
        if "Ollama" in str(e):
            print("❌ Error: Ollama is not running")
            print("   Please start Ollama: ollama serve")
        elif "ChromaDB" in str(e):
            print("❌ Error: Database not found")
            print("   Please run document processor first")
        else:
            print(f"❌ Error: {e}")

        return None

    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

# Usage
result = safe_answer_generation(engine, "Tell me about yourself?")

if result:
    print(f"✓ Answer: {result['answer']}")
else:
    print("✗ Failed to generate answer")
```

## Complete Application Example

```python
#!/usr/bin/env python3
"""
Complete Interview Whisperer application with LLM Engine.
"""

import sys
from pathlib import Path
from document_processor import DocumentProcessor
from llm_engine import LLMEngine

def setup_system():
    """Initial setup: process documents and initialize engine."""
    print("Setting up Interview Whisperer...")

    # Process documents
    processor = DocumentProcessor(
        documents_dir="../documents",
        db_path="../data/chroma_db"
    )

    doc_results = processor.process_all_documents()
    print(f"✓ Processed {len(doc_results)} documents")

    # Initialize engine
    engine = LLMEngine(db_path="../data/chroma_db")
    print(f"✓ LLM Engine ready")

    return engine

def run_interview_practice(engine: LLMEngine):
    """Run interactive interview practice."""
    print("\n" + "=" * 60)
    print("Interview Practice Mode")
    print("=" * 60)
    print("\nI'll ask you common interview questions.")
    print("Type your response, and I'll provide a suggested answer.\n")

    common_questions = [
        "Tell me about yourself?",
        "What's your biggest strength?",
        "What's your biggest weakness?",
        "Why do you want to work here?",
        "Describe a challenging project you worked on?"
    ]

    for i, question in enumerate(common_questions, 1):
        print(f"\n--- Question {i}/{len(common_questions)} ---")
        print(f"Interviewer: {question}")

        # Get user's answer
        user_answer = input("\nYour answer: ")

        # Show suggested answer
        print("\n💡 Suggested answer based on your documents:")
        print("-" * 60)

        def stream_callback(token: str):
            print(token, end='', flush=True)

        result = engine.stream_answer(question, stream_callback)

        print("\n" + "-" * 60)
        print(f"Confidence: {result['confidence']:.0%}")

        # Ask if user wants to continue
        continue_practice = input("\nContinue? (y/n): ").lower()
        if continue_practice != 'y':
            break

    print("\n✓ Practice session complete!")

def main():
    """Main application entry point."""
    try:
        # Setup
        engine = setup_system()

        # Run practice
        run_interview_practice(engine)

    except KeyboardInterrupt:
        print("\n\nGoodbye!")
        sys.exit(0)

    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

## Next Steps

1. **Add Documents**: Place PDF, DOCX, TXT, or MD files in `documents/`
2. **Process Documents**: Run `document_processor.py`
3. **Test Engine**: Run `llm_engine.py` to test
4. **Integrate**: Use in launcher or GUI application

## Performance Tips

1. **Cache Embeddings**: Same questions reuse cached embeddings
2. **Batch Questions**: Process multiple questions without reinitializing
3. **Adjust n_results**: Start with 3, increase if needed
4. **Temperature Tuning**: Lower (0.3-0.5) for consistent, higher (0.7-0.9) for creative
5. **Monitor Confidence**: Track over time to identify document gaps

---

**Status:** Production-ready integration examples
**Last Updated:** November 13, 2025
