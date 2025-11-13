#!/usr/bin/env python3
"""
Test script for DocumentProcessor

This script demonstrates how to use the DocumentProcessor to:
1. Process documents from the documents/ folder
2. Store them in ChromaDB with embeddings
3. Query for similar content

Prerequisites:
- Ollama must be installed and running
- Run: ollama pull nomic-embed-text
"""

import sys
from pathlib import Path
from document_processor import DocumentProcessor


def test_processing():
    """Test document processing pipeline."""
    print("=" * 70)
    print("Document Processor - Full Test")
    print("=" * 70)

    # Initialize
    processor = DocumentProcessor(
        documents_dir="../documents",
        db_path="../data/chroma_db"
    )

    # Show current stats
    print("\n📊 Current Database Stats:")
    stats = processor.get_stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")

    # Scan for documents
    print("\n🔍 Scanning for documents...")
    documents = processor.scan_documents()

    if not documents:
        print("  ⚠️  No documents found!")
        print("  💡 Add PDF, DOCX, TXT, or MD files to ../documents/")
        return

    print(f"  Found {len(documents)} document(s):")
    for doc in documents:
        size_kb = doc['size'] / 1024
        print(f"    • {doc['name']} ({doc['extension']}, {size_kb:.1f} KB)")

    # Test extraction (without processing)
    print("\n📄 Testing text extraction:")
    for doc in documents[:2]:  # Test first 2 documents
        print(f"\n  Processing: {doc['name']}")

        # Extract
        text = processor.extract_text(doc['path'])
        if text:
            print(f"    ✓ Extracted: {len(text)} characters")

            # Chunk
            chunks = processor.chunk_text(text, chunk_size=200, overlap=30)
            print(f"    ✓ Created: {len(chunks)} chunks")

            if chunks:
                print(f"    ✓ Preview: {chunks[0][:100]}...")
        else:
            print(f"    ✗ Failed to extract text")

    # Ask if user wants to process
    print("\n" + "=" * 70)
    response = input("\n🚀 Process all documents and create embeddings? (requires Ollama) [y/N]: ")

    if response.lower() != 'y':
        print("\n⏭️  Skipping full processing")
        print("\nTo process documents:")
        print("  1. Install Ollama: https://ollama.ai")
        print("  2. Pull model: ollama pull nomic-embed-text")
        print("  3. Run this script again")
        return

    # Process all documents
    print("\n🚀 Processing all documents...")
    print("-" * 70)

    def progress_callback(current, total, message):
        print(f"  [{current}/{total}] {message}")

    results = processor.process_all_documents(progress_callback=progress_callback)

    # Show results
    print("-" * 70)
    print("\n✅ Processing Complete!")
    print(f"  Total files: {results['total_files']}")
    print(f"  Processed: {results['processed_files']}")
    print(f"  Failed: {results['failed_files']}")
    print(f"  Total chunks: {results['total_chunks']}")

    if results['errors']:
        print(f"\n⚠️  Errors:")
        for error in results['errors']:
            print(f"    - {error}")

    # Show updated stats
    print("\n📊 Updated Database Stats:")
    stats = processor.get_stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")

    # Test query
    if results['total_chunks'] > 0:
        print("\n🔎 Testing similarity search...")
        test_queries = [
            "What are product management frameworks?",
            "How to prepare for interviews?",
            "Tell me about prioritization"
        ]

        for query in test_queries[:1]:  # Test first query
            print(f"\n  Query: '{query}'")
            search_results = processor.query_similar(query, n_results=3)

            if search_results:
                print(f"  Found {len(search_results)} similar chunks:\n")
                for i, result in enumerate(search_results, 1):
                    print(f"  Result {i}:")
                    print(f"    File: {result['metadata']['file_name']}")
                    print(f"    Chunk: {result['metadata']['chunk_id'] + 1}/{result['metadata']['total_chunks']}")
                    if result['distance'] is not None:
                        print(f"    Distance: {result['distance']:.4f}")
                    print(f"    Preview: {result['document'][:120]}...")
                    print()
            else:
                print("  No results found")

    print("=" * 70)
    print("Test complete!")
    print("=" * 70)


def test_clear_db():
    """Test clearing the database."""
    print("=" * 70)
    print("Clear Database Test")
    print("=" * 70)

    processor = DocumentProcessor(
        documents_dir="../documents",
        db_path="../data/chroma_db"
    )

    stats = processor.get_stats()
    print(f"\nCurrent chunks in DB: {stats['total_chunks']}")

    if stats['total_chunks'] == 0:
        print("Database is already empty!")
        return

    response = input("\n⚠️  Really clear the database? [y/N]: ")

    if response.lower() == 'y':
        if processor.clear_database():
            print("✅ Database cleared successfully")
            stats = processor.get_stats()
            print(f"New count: {stats['total_chunks']} chunks")
        else:
            print("❌ Failed to clear database")
    else:
        print("Cancelled")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--clear":
        test_clear_db()
    else:
        test_processing()
