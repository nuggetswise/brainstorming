#!/usr/bin/env python3
"""
Audio Engine Demo - Integration Example
Shows how to use AudioEngine in Interview Whisperer
"""

import time
import sys
from audio_engine import AudioEngine


class InterviewCopilot:
    """
    Example integration of AudioEngine with the interview copilot.
    Demonstrates question detection and answer retrieval flow.
    """

    def __init__(self):
        """Initialize the copilot with audio engine."""
        print("🚀 Initializing Interview Copilot...")

        # Initialize audio engine
        self.audio_engine = AudioEngine(model="base", language="en")

        # Question history
        self.questions = []
        self.current_question = None

        print("✓ Ready!")

    def on_transcript(self, text: str, is_question: bool) -> None:
        """
        Callback when new transcript is available.

        Args:
            text: Transcribed text
            is_question: True if detected as question
        """
        timestamp = time.strftime("%H:%M:%S")

        if is_question:
            # Question detected
            self.current_question = text
            self.questions.append({
                'text': text,
                'timestamp': timestamp
            })

            print(f"\n{'=' * 70}")
            print(f"❓ QUESTION DETECTED [{timestamp}]")
            print(f"{'=' * 70}")
            print(f"Q: {text}")
            print(f"{'=' * 70}")
            print()

            # TODO: Integrate with document processor to retrieve answer
            # answer = self.document_processor.retrieve_answer(text)
            # self.show_answer(answer)

            print("🔍 Searching knowledge base for relevant answers...")
            print("   (This would call document_processor.retrieve_answer())")
            print()

        else:
            # Regular speech (context)
            print(f"[{timestamp}] 💬 {text}")

    def start(self) -> None:
        """Start the copilot."""
        print("\n🎤 Starting audio capture...")
        print("=" * 70)
        print("INSTRUCTIONS:")
        print("- Speak naturally into your microphone")
        print("- Ask questions ending with '?' to trigger answer retrieval")
        print("- Press Ctrl+C to stop")
        print("=" * 70)
        print()

        self.audio_engine.start_listening(self.on_transcript)

    def stop(self) -> None:
        """Stop the copilot."""
        self.audio_engine.stop_listening()

        # Show summary
        print("\n" + "=" * 70)
        print("📊 SESSION SUMMARY")
        print("=" * 70)
        print(f"Questions detected: {len(self.questions)}")
        print()

        if self.questions:
            print("Questions asked:")
            for i, q in enumerate(self.questions, 1):
                print(f"  {i}. [{q['timestamp']}] {q['text']}")

        print("=" * 70)

    def run(self) -> None:
        """Run the copilot (blocking)."""
        try:
            self.start()

            # Keep running
            while True:
                time.sleep(1)

                # Show status
                status = self.audio_engine.get_status()
                level = status['audio_level']
                bar_length = int(level * 40)
                bar = "█" * bar_length + "░" * (40 - bar_length)

                sys.stdout.write(
                    f"\r🎚️  {bar} | "
                    f"Chunks: {status['chunks_processed']} | "
                    f"Questions: {len(self.questions)}"
                )
                sys.stdout.flush()

        except KeyboardInterrupt:
            print("\n")
            print("🛑 Stopping copilot...")
            self.stop()


# ============================================================================
# DEMO SCENARIOS
# ============================================================================

def demo_basic():
    """Demo 1: Basic transcription."""
    print("\n" + "=" * 70)
    print("DEMO 1: Basic Transcription")
    print("=" * 70)
    print("This demo shows basic real-time transcription.")
    print("Speak into your microphone. Questions will be highlighted.")
    print()

    copilot = InterviewCopilot()
    copilot.run()


def demo_advanced():
    """Demo 2: Advanced - with context awareness."""
    print("\n" + "=" * 70)
    print("DEMO 2: Advanced - Context Awareness")
    print("=" * 70)
    print("This demo shows context accumulation and retrieval.")
    print()

    def on_transcript_with_context(text: str, is_question: bool):
        timestamp = time.strftime("%H:%M:%S")

        if is_question:
            # Get recent context
            context = engine.get_recent_context(duration=15.0)

            print(f"\n{'=' * 70}")
            print(f"❓ QUESTION [{timestamp}]")
            print(f"{'=' * 70}")
            print(f"Q: {text}")
            print()
            print(f"📝 Recent Context (last 15s):")
            print(f"   {context}")
            print(f"{'=' * 70}")
            print()
        else:
            print(f"[{timestamp}] 💬 {text}")

    try:
        engine = AudioEngine(model="base")
        print("🎤 Starting audio capture with context awareness...")
        print()

        engine.start_listening(on_transcript_with_context)

        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n🛑 Stopping...")
        engine.stop_listening()


def demo_minimal():
    """Demo 3: Minimal example."""
    print("\n" + "=" * 70)
    print("DEMO 3: Minimal Example")
    print("=" * 70)
    print("Simplest possible integration.")
    print()

    def callback(text, is_question):
        marker = "❓" if is_question else "💬"
        print(f"{marker} {text}")

    try:
        engine = AudioEngine()
        engine.start_listening(callback)

        print("🎤 Listening... (Press Ctrl+C to stop)")
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        engine.stop_listening()
        print("✓ Done")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Audio Engine Demo - Interview Whisperer"
    )
    parser.add_argument(
        "--demo",
        type=str,
        choices=["basic", "advanced", "minimal"],
        default="basic",
        help="Demo scenario to run"
    )

    args = parser.parse_args()

    print("=" * 70)
    print("🎤 INTERVIEW WHISPERER - AUDIO ENGINE DEMO")
    print("=" * 70)
    print()
    print("This demo shows real-time audio transcription with Whisper.")
    print("Make sure your microphone is connected and working.")
    print()
    print(f"Selected demo: {args.demo}")
    print()

    # Run selected demo
    if args.demo == "basic":
        demo_basic()
    elif args.demo == "advanced":
        demo_advanced()
    elif args.demo == "minimal":
        demo_minimal()
