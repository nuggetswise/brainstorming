"""
LLM Engine for Interview Whisperer

Implements Retrieval-Augmented Generation (RAG) to answer interview questions
using the user's documents stored in ChromaDB and Ollama for generation.
"""

import logging
from typing import List, Dict, Optional, Callable, Tuple, Any
from pathlib import Path
import time
from functools import lru_cache
import hashlib

# Vector database
import chromadb
from chromadb.config import Settings

# LLM integration
try:
    import ollama
    OLLAMA_AVAILABLE = True
except ImportError:
    OLLAMA_AVAILABLE = False
    raise ImportError("ollama package not installed. Install with: pip install ollama")

# Local imports
try:
    from .config import (
        OLLAMA_LLM_MODEL,
        OLLAMA_EMBED_MODEL,
        OLLAMA_HOST,
        CHROMA_COLLECTION_NAME,
        logger
    )
except ImportError:
    # Fallback for direct execution
    from config import (
        OLLAMA_LLM_MODEL,
        OLLAMA_EMBED_MODEL,
        OLLAMA_HOST,
        CHROMA_COLLECTION_NAME,
        logger
    )


# =============================================================================
# PROMPT TEMPLATES
# =============================================================================

PROMPT_TEMPLATE = """You are helping during a job interview. Based on the context from the candidate's documents, provide a concise, natural answer.

Context from candidate's resume and notes:
{context}

Interview Question: "{question}"

Instructions:
- Use STAR method (Situation, Task, Action, Result) if applicable
- Keep answer to 2-3 sentences (60-90 seconds when spoken)
- Be specific and reference actual experience from the context
- Sound natural and conversational (not robotic)
- If the context doesn't contain relevant information, say "I don't have specific experience with that, but here's a related example..."

Answer:"""

FALLBACK_PROMPT = """You are helping during a job interview. The candidate doesn't have specific documented experience for this question.

Interview Question: "{question}"

Provide a brief, professional response acknowledging the gap while demonstrating willingness to learn. Keep it to 1-2 sentences.

Answer:"""


# =============================================================================
# LLM ENGINE CLASS
# =============================================================================

class LLMEngine:
    """
    LLM Engine for generating interview answers using RAG.

    Features:
    - Retrieves relevant context from ChromaDB
    - Generates answers using Ollama
    - Supports streaming for real-time UI updates
    - Caches embeddings for performance
    - Provides confidence scoring
    """

    def __init__(
        self,
        db_path: str,
        model: str = OLLAMA_LLM_MODEL,
        embed_model: str = OLLAMA_EMBED_MODEL,
        collection_name: str = CHROMA_COLLECTION_NAME
    ):
        """
        Initialize the LLM Engine.

        Args:
            db_path: Path to ChromaDB database
            model: Ollama model for text generation
            embed_model: Ollama model for embeddings
            collection_name: ChromaDB collection name

        Raises:
            RuntimeError: If Ollama is not running or ChromaDB cannot be accessed
        """
        self.logger = logging.getLogger('InterviewWhisperer.LLMEngine')
        self.model = model
        self.embed_model = embed_model
        self.db_path = Path(db_path)
        self.collection_name = collection_name

        # Embedding cache (question hash -> embedding)
        self._embedding_cache: Dict[str, List[float]] = {}

        # Initialize ChromaDB
        self._init_chromadb()

        # Verify Ollama is running
        self._verify_ollama()

        self.logger.info(f"LLMEngine initialized with model={model}, embed_model={embed_model}")

    def _init_chromadb(self) -> None:
        """Initialize ChromaDB connection and collection."""
        try:
            self.logger.info(f"Connecting to ChromaDB at {self.db_path}")
            self.client = chromadb.PersistentClient(
                path=str(self.db_path),
                settings=Settings(anonymized_telemetry=False)
            )

            # Get or create collection
            self.collection = self.client.get_or_create_collection(
                name=self.collection_name,
                metadata={"description": "Interview context from user documents"}
            )

            # Check if collection has documents
            count = self.collection.count()
            self.logger.info(f"Connected to collection '{self.collection_name}' with {count} documents")

            if count == 0:
                self.logger.warning("ChromaDB collection is empty. Please run document processor first.")

        except Exception as e:
            self.logger.error(f"Failed to initialize ChromaDB: {e}")
            raise RuntimeError(f"ChromaDB initialization failed: {e}")

    def _verify_ollama(self) -> None:
        """Verify Ollama is running and models are available."""
        try:
            # Test connection
            models = ollama.list()
            available_models = [m['name'] for m in models.get('models', [])]

            self.logger.info(f"Ollama is running. Available models: {available_models}")

            # Check if required models are available
            if not any(self.model in m for m in available_models):
                self.logger.warning(f"Model {self.model} not found. Pulling model...")
                ollama.pull(self.model)

            if not any(self.embed_model in m for m in available_models):
                self.logger.warning(f"Embedding model {self.embed_model} not found. Pulling model...")
                ollama.pull(self.embed_model)

        except Exception as e:
            self.logger.error(f"Ollama verification failed: {e}")
            raise RuntimeError(
                f"Ollama is not running or not accessible. "
                f"Please start Ollama with: ollama serve\n"
                f"Error: {e}"
            )

    def _get_question_hash(self, question: str) -> str:
        """Generate a hash for caching question embeddings."""
        return hashlib.md5(question.lower().strip().encode()).hexdigest()

    def _get_embedding(self, text: str) -> List[float]:
        """
        Generate embedding for text using Ollama.

        Args:
            text: Text to embed

        Returns:
            List of floats representing the embedding

        Raises:
            RuntimeError: If embedding generation fails
        """
        # Check cache
        text_hash = self._get_question_hash(text)
        if text_hash in self._embedding_cache:
            self.logger.debug(f"Using cached embedding for: {text[:50]}...")
            return self._embedding_cache[text_hash]

        try:
            self.logger.debug(f"Generating embedding for: {text[:50]}...")
            response = ollama.embeddings(
                model=self.embed_model,
                prompt=text
            )
            embedding = response['embedding']

            # Cache it
            self._embedding_cache[text_hash] = embedding

            return embedding

        except Exception as e:
            self.logger.error(f"Embedding generation failed: {e}")
            raise RuntimeError(f"Failed to generate embedding: {e}")

    def retrieve_context(
        self,
        question: str,
        n_results: int = 3
    ) -> List[Dict[str, Any]]:
        """
        Retrieve relevant context chunks from ChromaDB.

        Args:
            question: The interview question
            n_results: Number of top results to retrieve

        Returns:
            List of dictionaries with keys:
                - text: The document chunk text
                - source: Source file name
                - score: Similarity score (0-1, higher is better)
                - metadata: Additional metadata
        """
        if self.collection.count() == 0:
            self.logger.warning("No documents in database to retrieve from")
            return []

        try:
            # Generate embedding for question
            question_embedding = self._get_embedding(question)

            # Query ChromaDB
            self.logger.debug(f"Querying ChromaDB for: {question}")
            results = self.collection.query(
                query_embeddings=[question_embedding],
                n_results=min(n_results, self.collection.count())
            )

            # Format results
            context_chunks = []
            if results['documents'] and results['documents'][0]:
                for i, doc in enumerate(results['documents'][0]):
                    # Distance to similarity score (ChromaDB returns L2 distance)
                    # Lower distance = higher similarity
                    # Convert to 0-1 scale where 1 is most similar
                    distance = results['distances'][0][i] if results['distances'] else 1.0
                    similarity = max(0, 1 - (distance / 2))  # Normalize

                    metadata = results['metadatas'][0][i] if results['metadatas'] else {}

                    context_chunks.append({
                        'text': doc,
                        'source': metadata.get('source', 'Unknown'),
                        'score': similarity,
                        'metadata': metadata
                    })

            self.logger.info(
                f"Retrieved {len(context_chunks)} chunks with scores: "
                f"{[round(c['score'], 2) for c in context_chunks]}"
            )

            return context_chunks

        except Exception as e:
            self.logger.error(f"Context retrieval failed: {e}")
            return []

    def _format_context(self, chunks: List[Dict[str, Any]]) -> str:
        """
        Format context chunks into a readable string.

        Args:
            chunks: List of context chunks

        Returns:
            Formatted context string
        """
        if not chunks:
            return "No relevant context found in documents."

        # Remove duplicate text (sometimes same chunk retrieved)
        seen_texts = set()
        unique_chunks = []
        for chunk in chunks:
            if chunk['text'] not in seen_texts:
                unique_chunks.append(chunk)
                seen_texts.add(chunk['text'])

        # Format as numbered list with sources
        formatted = []
        for i, chunk in enumerate(unique_chunks, 1):
            source = chunk['source']
            text = chunk['text'].strip()
            formatted.append(f"{i}. [{source}] {text}")

        return "\n\n".join(formatted)

    def generate_answer(
        self,
        question: str,
        context: Optional[List[Dict[str, Any]]] = None,
        temperature: float = 0.7,
        max_tokens: int = 250
    ) -> Dict[str, Any]:
        """
        Generate an interview answer using RAG.

        Args:
            question: The interview question
            context: Optional pre-retrieved context (if None, will retrieve)
            temperature: Generation temperature (0.0-1.0)
            max_tokens: Maximum tokens in response

        Returns:
            Dictionary with keys:
                - answer: Generated answer text
                - confidence: Confidence score (0.0-1.0)
                - sources: List of source documents used
                - context_used: Whether context was available
                - generation_time: Time taken to generate
        """
        start_time = time.time()

        # Retrieve context if not provided
        if context is None:
            context = self.retrieve_context(question, n_results=3)

        # Determine if we have useful context
        has_context = bool(context and context[0]['score'] > 0.3)

        # Build prompt
        if has_context:
            formatted_context = self._format_context(context)
            prompt = PROMPT_TEMPLATE.format(
                context=formatted_context,
                question=question
            )
        else:
            prompt = FALLBACK_PROMPT.format(question=question)
            self.logger.warning("No relevant context found, using fallback prompt")

        # Generate answer
        try:
            self.logger.info(f"Generating answer for: {question}")
            response = ollama.generate(
                model=self.model,
                prompt=prompt,
                options={
                    'temperature': temperature,
                    'num_predict': max_tokens,
                    'stop': ['\n\n', 'Question:', 'Interview Question:']
                }
            )

            answer = response['response'].strip()
            generation_time = time.time() - start_time

            # Calculate confidence score
            confidence = self.get_confidence_score(question, answer, context)

            # Extract sources
            sources = list(set([c['source'] for c in context])) if context else []

            result = {
                'answer': answer,
                'confidence': confidence,
                'sources': sources,
                'context_used': has_context,
                'generation_time': generation_time,
                'question': question
            }

            self.logger.info(
                f"Generated answer in {generation_time:.2f}s "
                f"(confidence: {confidence:.0%}, sources: {len(sources)})"
            )

            return result

        except Exception as e:
            self.logger.error(f"Answer generation failed: {e}")

            # Return fallback response
            return {
                'answer': (
                    "I apologize, but I'm having trouble generating a response right now. "
                    "Could you please rephrase the question?"
                ),
                'confidence': 0.0,
                'sources': [],
                'context_used': False,
                'generation_time': time.time() - start_time,
                'error': str(e)
            }

    def stream_answer(
        self,
        question: str,
        callback: Callable[[str], None],
        context: Optional[List[Dict[str, Any]]] = None,
        temperature: float = 0.7,
        max_tokens: int = 250
    ) -> Dict[str, Any]:
        """
        Generate answer with streaming (for real-time UI updates).

        Args:
            question: The interview question
            callback: Function to call with each token (callback(token))
            context: Optional pre-retrieved context
            temperature: Generation temperature
            max_tokens: Maximum tokens in response

        Returns:
            Dictionary with metadata (same as generate_answer)
        """
        start_time = time.time()

        # Retrieve context if not provided
        if context is None:
            context = self.retrieve_context(question, n_results=3)

        # Determine if we have useful context
        has_context = bool(context and context[0]['score'] > 0.3)

        # Build prompt
        if has_context:
            formatted_context = self._format_context(context)
            prompt = PROMPT_TEMPLATE.format(
                context=formatted_context,
                question=question
            )
        else:
            prompt = FALLBACK_PROMPT.format(question=question)

        # Generate with streaming
        try:
            self.logger.info(f"Streaming answer for: {question}")

            full_answer = ""
            stream = ollama.generate(
                model=self.model,
                prompt=prompt,
                stream=True,
                options={
                    'temperature': temperature,
                    'num_predict': max_tokens,
                    'stop': ['\n\n', 'Question:', 'Interview Question:']
                }
            )

            for chunk in stream:
                token = chunk['response']
                full_answer += token
                callback(token)

            generation_time = time.time() - start_time

            # Calculate confidence
            confidence = self.get_confidence_score(question, full_answer, context)

            # Extract sources
            sources = list(set([c['source'] for c in context])) if context else []

            result = {
                'answer': full_answer.strip(),
                'confidence': confidence,
                'sources': sources,
                'context_used': has_context,
                'generation_time': generation_time,
                'question': question
            }

            self.logger.info(
                f"Streamed answer in {generation_time:.2f}s "
                f"(confidence: {confidence:.0%})"
            )

            return result

        except Exception as e:
            self.logger.error(f"Streaming generation failed: {e}")

            error_msg = (
                "I apologize, but I'm having trouble generating a response right now."
            )
            callback(error_msg)

            return {
                'answer': error_msg,
                'confidence': 0.0,
                'sources': [],
                'context_used': False,
                'generation_time': time.time() - start_time,
                'error': str(e)
            }

    def get_confidence_score(
        self,
        question: str,
        answer: str,
        context: Optional[List[Dict[str, Any]]] = None
    ) -> float:
        """
        Estimate confidence in the generated answer.

        Args:
            question: The interview question
            answer: The generated answer
            context: Retrieved context chunks

        Returns:
            Confidence score between 0.0 and 1.0
        """
        if not context or len(context) == 0:
            return 0.2  # Low confidence without context

        # Get top similarity score
        top_score = context[0]['score']

        # Confidence thresholds based on similarity
        if top_score >= 0.7:
            # High similarity - high confidence
            base_confidence = 0.85
        elif top_score >= 0.5:
            # Medium similarity - medium confidence
            base_confidence = 0.65
        elif top_score >= 0.3:
            # Low similarity - low confidence
            base_confidence = 0.45
        else:
            # Very low similarity - very low confidence
            base_confidence = 0.25

        # Adjust based on answer length (very short answers may indicate issues)
        answer_length = len(answer.split())
        if answer_length < 10:
            base_confidence *= 0.7  # Penalty for very short answers
        elif answer_length > 100:
            base_confidence *= 0.9  # Slight penalty for very long answers

        # Check if answer contains fallback phrases
        fallback_phrases = [
            "don't have specific experience",
            "not sure about",
            "can't recall",
            "trouble generating"
        ]
        if any(phrase in answer.lower() for phrase in fallback_phrases):
            base_confidence *= 0.5

        # Ensure confidence stays in valid range
        return max(0.0, min(1.0, base_confidence))

    def clear_cache(self) -> None:
        """Clear the embedding cache."""
        self._embedding_cache.clear()
        self.logger.info("Embedding cache cleared")

    def get_stats(self) -> Dict[str, Any]:
        """
        Get engine statistics.

        Returns:
            Dictionary with stats about the engine state
        """
        return {
            'model': self.model,
            'embed_model': self.embed_model,
            'collection_name': self.collection_name,
            'document_count': self.collection.count(),
            'cache_size': len(self._embedding_cache),
            'db_path': str(self.db_path)
        }


# =============================================================================
# TESTING & DEMONSTRATION
# =============================================================================

def main():
    """Test the LLM Engine with sample questions."""
    print("=" * 60)
    print("LLM Engine Test Suite")
    print("=" * 60)

    # Initialize engine
    print("\n1️⃣  Initializing LLM Engine...")
    try:
        engine = LLMEngine("../data/chroma_db")
        print("   ✓ Engine initialized successfully")

        # Print stats
        stats = engine.get_stats()
        print(f"\n   📊 Engine Stats:")
        print(f"      - Model: {stats['model']}")
        print(f"      - Embedding Model: {stats['embed_model']}")
        print(f"      - Documents in DB: {stats['document_count']}")
        print(f"      - Cache size: {stats['cache_size']}")

    except Exception as e:
        print(f"   ✗ Failed to initialize: {e}")
        return

    # Test questions
    test_questions = [
        "Tell me about your experience with product management?",
        "How do you prioritize features?",
        "Describe a time you handled a difficult stakeholder?",
        "What's your experience with agile development?",
        "How do you measure product success?"
    ]

    print("\n" + "=" * 60)
    print("2️⃣  Testing Standard Answer Generation")
    print("=" * 60)

    for i, question in enumerate(test_questions, 1):
        print(f"\n❓ Question {i}: {question}")
        print("-" * 60)

        try:
            result = engine.generate_answer(question)

            print(f"💡 Answer: {result['answer']}\n")
            print(f"📊 Metadata:")
            print(f"   - Confidence: {result['confidence']:.0%}")
            print(f"   - Sources: {', '.join(result['sources']) if result['sources'] else 'None'}")
            print(f"   - Context Used: {result['context_used']}")
            print(f"   - Generation Time: {result['generation_time']:.2f}s")

        except Exception as e:
            print(f"   ✗ Error: {e}")

    # Test streaming
    print("\n" + "=" * 60)
    print("3️⃣  Testing Streaming Generation")
    print("=" * 60)

    test_stream_question = "What's your biggest achievement?"
    print(f"\n❓ Question: {test_stream_question}")
    print("-" * 60)
    print("💡 Streaming Answer: ", end='', flush=True)

    def print_token(token: str):
        print(token, end='', flush=True)

    try:
        result = engine.stream_answer(test_stream_question, print_token)
        print("\n")
        print(f"\n📊 Metadata:")
        print(f"   - Confidence: {result['confidence']:.0%}")
        print(f"   - Generation Time: {result['generation_time']:.2f}s")

    except Exception as e:
        print(f"\n   ✗ Error: {e}")

    # Test context retrieval
    print("\n" + "=" * 60)
    print("4️⃣  Testing Context Retrieval")
    print("=" * 60)

    test_retrieval_question = "What technical skills do you have?"
    print(f"\n❓ Question: {test_retrieval_question}")
    print("-" * 60)

    try:
        context = engine.retrieve_context(test_retrieval_question, n_results=3)
        print(f"📚 Retrieved {len(context)} context chunks:\n")

        for i, chunk in enumerate(context, 1):
            print(f"{i}. Source: {chunk['source']}")
            print(f"   Score: {chunk['score']:.2f}")
            print(f"   Text: {chunk['text'][:100]}...")
            print()

    except Exception as e:
        print(f"   ✗ Error: {e}")

    print("\n" + "=" * 60)
    print("✅ Test Suite Complete")
    print("=" * 60)


if __name__ == "__main__":
    main()
