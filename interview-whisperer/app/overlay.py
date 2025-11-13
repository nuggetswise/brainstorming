#!/usr/bin/env python3
"""
Interview Whisperer - Overlay Window
====================================

Beautiful, always-on-top overlay that displays interview question suggestions
in real-time during interviews.

Features:
- Always on top, semi-transparent window
- Draggable and repositionable
- Real-time question and answer display
- Confidence indicators with color coding
- Smooth animations (fade in, pulse)
- Keyboard shortcuts (Ctrl+H, Ctrl+C, Esc)
- Thread-safe updates
- Modern dark theme design

Author: Interview Whisperer Team
"""

import tkinter as tk
from tkinter import ttk, font
import threading
import time
from typing import Optional, Tuple, Callable, Dict, Any
from dataclasses import dataclass


@dataclass
class Colors:
    """Dark theme color palette"""
    background: str = '#1e1e2e'
    panel: str = '#2a2a3e'
    header: str = '#363650'
    text_primary: str = '#ffffff'
    text_secondary: str = '#b4b4c8'
    accent_blue: str = '#89b4fa'
    accent_green: str = '#a6e3a1'
    accent_yellow: str = '#f9e2af'
    accent_red: str = '#f38ba8'
    border: str = '#45475a'


class OverlayWindow:
    """
    Always-on-top overlay window for displaying interview suggestions.

    Features:
    - Semi-transparent, draggable window
    - Real-time question/answer display
    - Confidence indicators with color coding
    - Smooth fade animations
    - Keyboard shortcuts
    - Thread-safe updates
    """

    def __init__(self, width: int = 400, height: int = 350, transparency: float = 0.95,
                 position: str = "top-right", font_size: int = 10, always_on_top: bool = True,
                 show_confidence: bool = True, show_sources: bool = True):
        """
        Initialize the overlay window.

        Args:
            width: Window width in pixels
            height: Window height in pixels
            transparency: Window transparency (0.0-1.0)
            position: Window position (top-right, top-left, bottom-right, bottom-left, center)
            font_size: Base font size
            always_on_top: Keep window always on top
            show_confidence: Display confidence scores
            show_sources: Display source documents
        """
        self.width = width
        self.height = height
        self.transparency = transparency
        self.position_pref = position
        self.font_size_base = font_size
        self.always_on_top = always_on_top
        self.show_confidence = show_confidence
        self.show_sources = show_sources
        self.colors = Colors()
        self.is_visible = True
        self.animation_id = None
        self._lock = threading.Lock()

        # Create main window
        self.window = tk.Tk()
        self.window.title("Interview Whisperer")
        self.window.geometry(f"{width}x{height}")

        # Window configuration
        self._configure_window()

        # Create UI elements
        self._create_widgets()

        # Setup drag functionality
        self._setup_drag()

        # Setup keyboard shortcuts
        self._setup_shortcuts()

        # Position window
        self._position_window()

    def _configure_window(self):
        """Configure window properties (transparency, always on top, etc.)"""
        # Always on top
        if self.always_on_top:
            self.window.attributes('-topmost', True)

        # Transparency (configurable)
        self.window.attributes('-alpha', self.transparency)

        # Remove window decorations (optional - comment out if you want title bar)
        self.window.overrideredirect(True)

        # Background color
        self.window.configure(bg=self.colors.background)

    def _create_widgets(self):
        """Create all UI widgets"""
        # Main container with padding
        self.main_frame = tk.Frame(
            self.window,
            bg=self.colors.background,
            highlightthickness=1,
            highlightbackground=self.colors.border
        )
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)

        # Header
        self._create_header()

        # Content area
        self._create_content()

    def _create_header(self):
        """Create draggable header with title and close button"""
        self.header_frame = tk.Frame(
            self.main_frame,
            bg=self.colors.header,
            height=40
        )
        self.header_frame.pack(fill=tk.X)
        self.header_frame.pack_propagate(False)

        # Title
        title_font = font.Font(family="Segoe UI", size=10, weight="bold")
        self.title_label = tk.Label(
            self.header_frame,
            text="🎯 Interview Whisperer",
            font=title_font,
            bg=self.colors.header,
            fg=self.colors.text_primary,
            anchor=tk.W,
            padx=10
        )
        self.title_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Close button
        self.close_btn = tk.Label(
            self.header_frame,
            text="✕",
            font=("Segoe UI", 12),
            bg=self.colors.header,
            fg=self.colors.text_secondary,
            cursor="hand2",
            padx=15
        )
        self.close_btn.pack(side=tk.RIGHT)
        self.close_btn.bind("<Button-1>", lambda e: self.hide())
        self.close_btn.bind("<Enter>", lambda e: self.close_btn.configure(
            fg=self.colors.accent_red,
            bg=self.colors.panel
        ))
        self.close_btn.bind("<Leave>", lambda e: self.close_btn.configure(
            fg=self.colors.text_secondary,
            bg=self.colors.header
        ))

    def _create_content(self):
        """Create content area with question, answer, and tips sections"""
        # Scrollable content frame
        content_canvas = tk.Canvas(
            self.main_frame,
            bg=self.colors.background,
            highlightthickness=0
        )
        scrollbar = tk.Scrollbar(
            self.main_frame,
            orient=tk.VERTICAL,
            command=content_canvas.yview
        )

        self.content_frame = tk.Frame(content_canvas, bg=self.colors.background)

        # Configure scroll
        self.content_frame.bind(
            "<Configure>",
            lambda e: content_canvas.configure(scrollregion=content_canvas.bbox("all"))
        )

        content_canvas.create_window((0, 0), window=self.content_frame, anchor=tk.NW)
        content_canvas.configure(yscrollcommand=scrollbar.set)

        # Pack scroll elements
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        content_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Question section
        self._create_question_section()

        # Answer section
        self._create_answer_section()

        # Tips section
        self._create_tips_section()

        # Mouse wheel scrolling
        content_canvas.bind_all("<MouseWheel>", lambda e: content_canvas.yview_scroll(
            int(-1*(e.delta/120)), "units"
        ))

    def _create_question_section(self):
        """Create question display section"""
        question_container = tk.Frame(
            self.content_frame,
            bg=self.colors.panel,
            highlightthickness=1,
            highlightbackground=self.colors.border
        )
        question_container.pack(fill=tk.X, padx=10, pady=(10, 5))

        # Label
        label_font = font.Font(family="Segoe UI", size=9, weight="bold")
        question_label = tk.Label(
            question_container,
            text="🎤 Question Detected:",
            font=label_font,
            bg=self.colors.panel,
            fg=self.colors.accent_blue,
            anchor=tk.W,
            padx=10,
            pady=5
        )
        question_label.pack(fill=tk.X)

        # Question text
        question_font = font.Font(family="Segoe UI", size=9, slant="italic")
        self.question_text = tk.Label(
            question_container,
            text="Waiting for question...",
            font=question_font,
            bg=self.colors.panel,
            fg=self.colors.text_primary,
            wraplength=360,
            justify=tk.LEFT,
            anchor=tk.W,
            padx=10,
            pady=5
        )
        self.question_text.pack(fill=tk.X)

    def _create_answer_section(self):
        """Create answer display section with confidence indicator"""
        answer_container = tk.Frame(
            self.content_frame,
            bg=self.colors.background
        )
        answer_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Header with confidence
        header_frame = tk.Frame(answer_container, bg=self.colors.background)
        header_frame.pack(fill=tk.X)

        # Label
        label_font = font.Font(family="Segoe UI", size=9, weight="bold")
        answer_label = tk.Label(
            header_frame,
            text="💡 Suggested Answer:",
            font=label_font,
            bg=self.colors.background,
            fg=self.colors.accent_green,
            anchor=tk.W
        )
        answer_label.pack(side=tk.LEFT)

        # Confidence indicator
        self.confidence_label = tk.Label(
            header_frame,
            text="[●●○] 85%",
            font=("Segoe UI", 8),
            bg=self.colors.background,
            fg=self.colors.accent_green,
            anchor=tk.E,
            padx=5
        )
        self.confidence_label.pack(side=tk.RIGHT)

        # Answer text box
        answer_box = tk.Frame(
            answer_container,
            bg=self.colors.panel,
            highlightthickness=1,
            highlightbackground=self.colors.border
        )
        answer_box.pack(fill=tk.BOTH, expand=True, pady=(5, 0))

        # Text widget with scrollbar
        answer_scroll = tk.Scrollbar(answer_box)
        answer_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.answer_text = tk.Text(
            answer_box,
            font=("Segoe UI", 9),
            bg=self.colors.panel,
            fg=self.colors.text_primary,
            wrap=tk.WORD,
            height=8,
            relief=tk.FLAT,
            padx=10,
            pady=10,
            yscrollcommand=answer_scroll.set,
            selectbackground=self.colors.accent_blue,
            insertbackground=self.colors.text_primary
        )
        self.answer_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        answer_scroll.config(command=self.answer_text.yview)

        # Make text read-only but copyable
        self.answer_text.insert("1.0", "Waiting for answer suggestion...")
        self.answer_text.config(state=tk.DISABLED)

    def _create_tips_section(self):
        """Create tips section"""
        tips_frame = tk.Frame(
            self.content_frame,
            bg=self.colors.background
        )
        tips_frame.pack(fill=tk.X, padx=10, pady=(5, 10))

        # Tips
        tips_font = font.Font(family="Segoe UI", size=8)

        self.tip_time = tk.Label(
            tips_frame,
            text="⏱️  60-90 seconds recommended",
            font=tips_font,
            bg=self.colors.background,
            fg=self.colors.text_secondary,
            anchor=tk.W
        )
        self.tip_time.pack(fill=tk.X)

        self.tip_method = tk.Label(
            tips_frame,
            text="📋 Use STAR method",
            font=tips_font,
            bg=self.colors.background,
            fg=self.colors.text_secondary,
            anchor=tk.W
        )
        self.tip_method.pack(fill=tk.X)

    def _setup_drag(self):
        """Setup window dragging functionality"""
        self.drag_start_x = 0
        self.drag_start_y = 0

        # Bind drag events to header
        self.header_frame.bind("<Button-1>", self._start_drag)
        self.header_frame.bind("<B1-Motion>", self._on_drag)
        self.title_label.bind("<Button-1>", self._start_drag)
        self.title_label.bind("<B1-Motion>", self._on_drag)

    def _start_drag(self, event):
        """Start dragging window"""
        self.drag_start_x = event.x
        self.drag_start_y = event.y

    def _on_drag(self, event):
        """Handle window dragging"""
        x = self.window.winfo_x() + event.x - self.drag_start_x
        y = self.window.winfo_y() + event.y - self.drag_start_y
        self.window.geometry(f"+{x}+{y}")

    def _setup_shortcuts(self):
        """Setup keyboard shortcuts"""
        self.window.bind("<Control-h>", lambda e: self.toggle_visibility())
        self.window.bind("<Control-c>", lambda e: self._copy_answer())
        self.window.bind("<Escape>", lambda e: self.clear())

    def _position_window(self):
        """Position window based on position preference"""
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        padding = 20

        # Calculate position based on preference
        if self.position_pref == "top-right":
            x = screen_width - self.width - padding
            y = padding
        elif self.position_pref == "top-left":
            x = padding
            y = padding
        elif self.position_pref == "bottom-right":
            x = screen_width - self.width - padding
            y = screen_height - self.height - padding
        elif self.position_pref == "bottom-left":
            x = padding
            y = screen_height - self.height - padding
        elif self.position_pref == "center":
            x = (screen_width - self.width) // 2
            y = (screen_height - self.height) // 2
        else:
            # Default to top-right
            x = screen_width - self.width - padding
            y = padding

        self.window.geometry(f"{self.width}x{self.height}+{x}+{y}")

    def show_suggestion(
        self,
        question: str,
        answer: str,
        confidence: float,
        tips: Optional[Dict[str, str]] = None
    ):
        """
        Update overlay with new suggestion.

        Args:
            question: The detected interview question
            answer: The AI-generated answer suggestion
            confidence: Confidence score (0.0 to 1.0)
            tips: Optional dict with 'time' and 'method' keys
        """
        with self._lock:
            # Schedule update on main thread
            self.window.after(0, self._update_suggestion, question, answer, confidence, tips)

    def _update_suggestion(
        self,
        question: str,
        answer: str,
        confidence: float,
        tips: Optional[Dict[str, str]]
    ):
        """Internal method to update UI (must run on main thread)"""
        # Update question
        self.question_text.config(text=question)

        # Update answer
        self.answer_text.config(state=tk.NORMAL)
        self.answer_text.delete("1.0", tk.END)
        self.answer_text.insert("1.0", answer)
        self.answer_text.config(state=tk.DISABLED)

        # Update confidence indicator
        self._update_confidence(confidence)

        # Update tips if provided
        if tips:
            if 'time' in tips:
                self.tip_time.config(text=f"⏱️  {tips['time']}")
            if 'method' in tips:
                self.tip_method.config(text=f"📋 {tips['method']}")

        # Fade in animation
        self._fade_in()

    def _update_confidence(self, confidence: float):
        """Update confidence indicator based on score"""
        percentage = int(confidence * 100)

        # Determine color and dots based on confidence
        if confidence >= 0.70:
            color = self.colors.accent_green
            dots = "[●●●]"
        elif confidence >= 0.50:
            color = self.colors.accent_yellow
            dots = "[●●○]"
        else:
            color = self.colors.accent_red
            dots = "[●○○]"

        # Update label
        self.confidence_label.config(
            text=f"{dots} {percentage}%",
            fg=color
        )

        # Subtle pulse animation
        self._pulse_confidence()

    def _fade_in(self):
        """Smooth fade-in animation"""
        # Start from 0.7 alpha and go to 0.95
        def animate(alpha=0.7):
            if alpha < 0.95:
                self.window.attributes('-alpha', alpha)
                self.animation_id = self.window.after(30, animate, alpha + 0.05)
            else:
                self.window.attributes('-alpha', 0.95)

        animate()

    def _pulse_confidence(self):
        """Subtle pulse animation for confidence indicator"""
        original_font = self.confidence_label.cget("font")

        def pulse(size=8, direction=1, count=0):
            if count < 6:  # 3 pulses
                new_size = size + direction
                if new_size >= 10:
                    direction = -1
                elif new_size <= 8:
                    direction = 1
                    count += 1

                self.confidence_label.config(font=("Segoe UI", new_size))
                self.animation_id = self.window.after(50, pulse, new_size, direction, count)
            else:
                self.confidence_label.config(font=("Segoe UI", 8))

        pulse()

    def clear(self):
        """Clear current suggestion and show waiting state"""
        with self._lock:
            self.window.after(0, self._clear_suggestion)

    def _clear_suggestion(self):
        """Internal method to clear UI"""
        # Reset question
        self.question_text.config(text="Waiting for question...")

        # Reset answer
        self.answer_text.config(state=tk.NORMAL)
        self.answer_text.delete("1.0", tk.END)
        self.answer_text.insert("1.0", "Waiting for answer suggestion...")
        self.answer_text.config(state=tk.DISABLED)

        # Reset confidence
        self.confidence_label.config(
            text="[○○○] --",
            fg=self.colors.text_secondary
        )

        # Reset tips
        self.tip_time.config(text="⏱️  60-90 seconds recommended")
        self.tip_method.config(text="📋 Use STAR method")

    def hide(self):
        """Hide the overlay window"""
        self.is_visible = False
        self.window.withdraw()

    def show(self):
        """Show the overlay window"""
        self.is_visible = True
        self.window.deiconify()

    def toggle_visibility(self):
        """Toggle overlay visibility"""
        if self.is_visible:
            self.hide()
        else:
            self.show()

    def set_position(self, x: int, y: int):
        """
        Set window position.

        Args:
            x: X coordinate
            y: Y coordinate
        """
        self.window.geometry(f"+{x}+{y}")

    def _copy_answer(self):
        """Copy answer text to clipboard"""
        try:
            answer = self.answer_text.get("1.0", tk.END).strip()
            self.window.clipboard_clear()
            self.window.clipboard_append(answer)

            # Brief feedback
            original_text = self.confidence_label.cget("text")
            self.confidence_label.config(text="✓ Copied!")
            self.window.after(1000, lambda: self.confidence_label.config(text=original_text))
        except Exception as e:
            print(f"Error copying to clipboard: {e}")

    def run(self):
        """Start the overlay window main loop"""
        self.window.mainloop()

    def destroy(self):
        """Clean shutdown of overlay"""
        if self.animation_id:
            self.window.after_cancel(self.animation_id)
        self.window.destroy()


# =============================================================================
# TESTING & DEMO
# =============================================================================

def demo_basic():
    """Basic demo - single suggestion"""
    overlay = OverlayWindow()

    # Show test suggestion after 1 second
    def show_test_suggestion():
        overlay.show_suggestion(
            question="Tell me about your experience with product management?",
            answer=(
                "I have 5 years of PM experience at leading tech companies. "
                "At my last role, I owned the product roadmap for a B2B SaaS platform "
                "serving 10K+ users.\n\n"
                "In one notable project, I led the development of a new feature that "
                "increased user engagement by 35%. I used the RICE framework to "
                "prioritize features, conducted 20+ customer interviews to validate "
                "assumptions, and worked closely with engineering and design teams "
                "to deliver on time.\n\n"
                "The key challenge was balancing stakeholder requests with user needs. "
                "I resolved this by implementing a transparent prioritization system "
                "and regular roadmap reviews with leadership."
            ),
            confidence=0.92,
            tips={
                'time': '90-120 seconds recommended',
                'method': 'Use STAR method (Situation, Task, Action, Result)'
            }
        )

    overlay.window.after(1000, show_test_suggestion)

    print("=" * 60)
    print("Interview Whisperer - Basic Overlay Demo")
    print("=" * 60)
    print("\nKeyboard Shortcuts:")
    print("  Ctrl+H     - Hide/Show overlay")
    print("  Ctrl+C     - Copy answer to clipboard")
    print("  Esc        - Clear suggestion")
    print("\nWindow is draggable - click and drag the header!")
    print("\nClose the window or press the X button to exit.")
    print("=" * 60)

    overlay.run()


def demo_interactive():
    """Interactive demo - simulates real interview flow"""
    overlay = OverlayWindow()

    # Simulate interview questions over time
    questions = [
        {
            "question": "Tell me about yourself and your background.",
            "answer": (
                "I'm a product manager with 7 years of experience in B2B SaaS. "
                "I started my career as a software engineer, which gave me strong "
                "technical foundations, then transitioned to PM because I enjoyed "
                "solving user problems and driving product strategy.\n\n"
                "Most recently at TechCorp, I led a team that shipped 3 major features "
                "that increased revenue by 25%. I'm passionate about user-centric "
                "product development and data-driven decision making."
            ),
            "confidence": 0.88,
            "tips": {
                'time': '60-90 seconds',
                'method': 'Brief chronological summary'
            }
        },
        {
            "question": "Describe a time when you had to make a difficult prioritization decision.",
            "answer": (
                "At my previous company, we had limited engineering resources and "
                "stakeholders pushing for 5 different features. I used the RICE framework "
                "(Reach, Impact, Confidence, Effort) to objectively score each feature.\n\n"
                "One high-profile stakeholder wanted a feature that scored low on RICE. "
                "I scheduled a 1:1 to walk through the data, showed customer research "
                "indicating minimal demand, and proposed an alternative that addressed "
                "the underlying need.\n\n"
                "Result: We prioritized based on data, shipped features that drove "
                "30% more engagement, and maintained strong stakeholder relationships "
                "through transparent communication."
            ),
            "confidence": 0.95,
            "tips": {
                'time': '90-120 seconds',
                'method': 'STAR method (Situation, Task, Action, Result)'
            }
        },
        {
            "question": "How do you handle disagreements with engineers or designers?",
            "answer": (
                "I believe disagreements are opportunities for better solutions. "
                "When I disagree with teammates, I start by understanding their perspective "
                "through active listening.\n\n"
                "For example, our design team once proposed a UI change I thought would "
                "hurt usability. Instead of pushing back immediately, I asked them to walk "
                "me through their reasoning. They had user research I hadn't seen.\n\n"
                "We ran an A/B test to validate both approaches. Their design performed "
                "20% better. This taught me to assume positive intent, stay data-driven, "
                "and recognize that diverse perspectives lead to better products."
            ),
            "confidence": 0.75,
            "tips": {
                'time': '75-90 seconds',
                'method': 'CAR method (Context, Action, Result)'
            }
        }
    ]

    def show_question(index):
        if index < len(questions):
            q = questions[index]
            overlay.show_suggestion(
                question=q["question"],
                answer=q["answer"],
                confidence=q["confidence"],
                tips=q["tips"]
            )

            # Show next question after 15 seconds
            overlay.window.after(15000, lambda: show_question(index + 1))
        else:
            # All questions shown, clear after 10 seconds
            overlay.window.after(10000, overlay.clear)

    # Start showing questions after 2 seconds
    overlay.window.after(2000, lambda: show_question(0))

    print("=" * 60)
    print("Interview Whisperer - Interactive Demo")
    print("=" * 60)
    print("\nSimulating real interview with 3 questions...")
    print("Each question will appear for 15 seconds.\n")
    print("Keyboard Shortcuts:")
    print("  Ctrl+H     - Hide/Show overlay")
    print("  Ctrl+C     - Copy answer to clipboard")
    print("  Esc        - Clear suggestion")
    print("\nWindow is draggable - click and drag the header!")
    print("=" * 60)

    overlay.run()


if __name__ == "__main__":
    import sys

    print("\n" + "=" * 60)
    print("INTERVIEW WHISPERER - OVERLAY WINDOW")
    print("=" * 60)
    print("\nChoose demo mode:")
    print("  1. Basic Demo (single suggestion)")
    print("  2. Interactive Demo (simulated interview)")
    print()

    choice = input("Enter choice (1 or 2, default=1): ").strip()

    if choice == "2":
        demo_interactive()
    else:
        demo_basic()
