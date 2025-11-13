"""
Integration Example: Using DocumentProcessor in Interview Whisperer

This example shows how to integrate the DocumentProcessor into the main
Interview Whisperer application for context-aware interview assistance.
"""

from typing import List, Dict, Optional
from document_processor import DocumentProcessor
import logging


class InterviewContextManager:
    """
    Manages interview context using processed documents.

    This class provides a simple interface for:
    1. Processing user documents
    2. Retrieving relevant context for questions
    3. Providing document-aware interview assistance
    """

    def __init__(self, documents_dir: str, db_path: str):
        """
        Initialize the context manager.

        Args:
            documents_dir: Path to documents folder
            db_path: Path to ChromaDB storage
        """
        self.processor = DocumentProcessor(documents_dir, db_path)
        self.logger = logging.getLogger(__name__)

    def process_documents(self, progress_callback=None) -> Dict:
        """
        Process all documents in the documents folder.

        Args:
            progress_callback: Optional callback for progress updates

        Returns:
            Processing statistics
        """
        self.logger.info("Processing documents...")
        stats = self.processor.process_all_documents(progress_callback)

        if stats['processed_files'] > 0:
            self.logger.info(
                f"✅ Processed {stats['processed_files']} files "
                f"({stats['total_chunks']} chunks)"
            )
        else:
            self.logger.warning("No documents processed")

        return stats

    def get_relevant_context(
        self,
        question: str,
        max_chunks: int = 3,
        max_chars: int = 1000
    ) -> str:
        """
        Get relevant context for an interview question.

        Args:
            question: The interview question or topic
            max_chunks: Maximum number of chunks to retrieve
            max_chars: Maximum total characters to return

        Returns:
            Formatted context string
        """
        results = self.processor.query_similar(question, n_results=max_chunks)

        if not results:
            return ""

        context_parts = []
        total_chars = 0

        for result in results:
            chunk = result['document']
            file_name = result['metadata']['file_name']

            # Add source attribution
            context_parts.append(f"From {file_name}:\n{chunk}\n")
            total_chars += len(chunk)

            if total_chars >= max_chars:
                break

        return "\n".join(context_parts)

    def prepare_interview_answer(
        self,
        question: str,
        include_context: bool = True
    ) -> Dict[str, str]:
        """
        Prepare components for answering an interview question.

        Args:
            question: The interview question
            include_context: Whether to include document context

        Returns:
            Dictionary with question, context, and guidance
        """
        result = {
            'question': question,
            'context': '',
            'guidance': self._get_answer_guidance(question)
        }

        if include_context:
            result['context'] = self.get_relevant_context(question)

        return result

    def _get_answer_guidance(self, question: str) -> str:
        """
        Get structured guidance for answering the question.

        Args:
            question: The interview question

        Returns:
            Guidance string
        """
        # This would use an LLM in production
        # For now, provide generic guidance
        return """
        Answer Structure:
        1. Direct answer (30 seconds)
        2. Specific example (1 minute)
        3. Impact/results (30 seconds)
        4. Key takeaway (15 seconds)

        Tips:
        - Use STAR format (Situation, Task, Action, Result)
        - Quantify impact when possible
        - Connect to job requirements
        - Keep total answer under 2 minutes
        """

    def get_stats(self) -> Dict:
        """Get current database statistics."""
        return self.processor.get_stats()

    def clear_and_reprocess(self, progress_callback=None) -> Dict:
        """Clear database and reprocess all documents."""
        self.processor.clear_database()
        return self.process_documents(progress_callback)


# ============================================================================
# Example Usage in GUI Application
# ============================================================================

class MockInterviewGUI:
    """
    Mock GUI to demonstrate integration.

    In the real application, this would be a tkinter GUI.
    """

    def __init__(self):
        self.context_manager = InterviewContextManager(
            documents_dir="../documents",
            db_path="../data/chroma_db"
        )
        self.current_question = None

    def on_startup(self):
        """Called when application starts."""
        print("Interview Whisperer Starting...")

        # Check if documents need processing
        stats = self.context_manager.get_stats()

        if stats['files_processed'] == 0:
            print("\n📄 No documents processed yet.")
            print("Would you like to process documents now? (y/n)")

            # In real GUI, this would be a dialog
            response = input()

            if response.lower() == 'y':
                self.process_documents_with_progress()
        else:
            print(f"\n✅ {stats['files_processed']} documents ready")
            print(f"   {stats['total_chunks']} chunks available")

    def process_documents_with_progress(self):
        """Process documents with progress updates."""
        print("\n🚀 Processing documents...")

        def progress_callback(current, total, message):
            # In real GUI, update progress bar
            print(f"  [{current}/{total}] {message}")

        results = self.context_manager.process_documents(progress_callback)

        print(f"\n✅ Processing complete!")
        print(f"   Files: {results['processed_files']}/{results['total_files']}")
        print(f"   Chunks: {results['total_chunks']}")

        if results['errors']:
            print(f"\n⚠️  {len(results['errors'])} errors")

    def on_question_detected(self, question: str):
        """Called when a question is detected via speech."""
        self.current_question = question
        print(f"\n❓ Question detected: {question}\n")

        # Get context and guidance
        answer_prep = self.context_manager.prepare_interview_answer(
            question,
            include_context=True
        )

        # Display to user
        if answer_prep['context']:
            print("📚 Relevant Context:")
            print(answer_prep['context'][:500])
            print("...\n")

        print("💡 Guidance:")
        print(answer_prep['guidance'])

    def on_practice_mode(self):
        """Practice mode with document-aware questions."""
        print("\n🎯 Practice Mode\n")

        # Example practice questions
        practice_questions = [
            "Tell me about a time you had to prioritize features",
            "How do you handle stakeholder disagreements?",
            "Explain your approach to user research"
        ]

        for i, question in enumerate(practice_questions, 1):
            print(f"\nQuestion {i}: {question}")

            # Get relevant context
            context = self.context_manager.get_relevant_context(
                question,
                max_chunks=2,
                max_chars=500
            )

            if context:
                print("\n📖 Your documents mention:")
                print(context[:300])
                print("...\n")

            print("⏱️  You have 2 minutes. Ready? (press Enter)")
            input()
            print("🎤 Recording... (speak your answer)\n")

            # In real app, record and analyze answer


# ============================================================================
# Main Example
# ============================================================================

def main():
    """Run the mock GUI example."""
    print("=" * 70)
    print("Interview Whisperer - Integration Example")
    print("=" * 70)

    # Create mock GUI
    app = MockInterviewGUI()

    # Simulate startup
    app.on_startup()

    # Simulate question detection
    print("\n" + "=" * 70)
    app.on_question_detected(
        "Tell me about your experience with product prioritization"
    )

    # Simulate practice mode
    print("\n" + "=" * 70)
    print("\nWould you like to try practice mode? (y/n)")
    response = input()

    if response.lower() == 'y':
        app.on_practice_mode()

    print("\n" + "=" * 70)
    print("Example complete!")
    print("=" * 70)


if __name__ == "__main__":
    main()
