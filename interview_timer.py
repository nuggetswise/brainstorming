#!/usr/bin/env python3
"""
Interview Answer Timer - Auto-detects when you start speaking
Changes color: Green (0-60s) -> Yellow (60-90s) -> Red (90s+)
"""

import tkinter as tk
from tkinter import font as tkfont
import sounddevice as sd
import numpy as np
import threading
import time

class InterviewTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Interview Timer")

        # Make window float on top
        self.root.attributes('-topmost', True)

        # Remove window decorations for cleaner look
        self.root.overrideredirect(True)

        # Set window size and make it circular-ish
        self.window_size = 150
        self.root.geometry(f'{self.window_size}x{self.window_size}+100+100')

        # Make window draggable
        self.root.bind('<Button-1>', self.start_drag)
        self.root.bind('<B1-Motion>', self.drag_motion)

        # Timer state
        self.is_running = False
        self.start_time = None
        self.elapsed_seconds = 0

        # Voice detection state
        self.is_listening = True
        self.voice_detected = False
        self.audio_threshold = 0.02  # Adjust if too sensitive/insensitive
        self.speech_duration_needed = 2.5  # seconds of speech to trigger
        self.speech_start_time = None

        # Setup UI
        self.setup_ui()

        # Start audio monitoring in background
        self.audio_thread = threading.Thread(target=self.monitor_audio, daemon=True)
        self.audio_thread.start()

        # Start UI update loop
        self.update_timer()

    def setup_ui(self):
        # Main canvas (circular background)
        self.canvas = tk.Canvas(
            self.root,
            width=self.window_size,
            height=self.window_size,
            highlightthickness=0
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Draw circular background
        self.circle = self.canvas.create_oval(
            10, 10,
            self.window_size-10,
            self.window_size-10,
            fill='#4CAF50',  # Green initially
            outline='#2E7D32',
            width=4
        )

        # Timer text
        self.timer_font = tkfont.Font(family='Arial', size=24, weight='bold')
        self.timer_text = self.canvas.create_text(
            self.window_size//2,
            self.window_size//2 - 10,
            text="00:00",
            font=self.timer_font,
            fill='white'
        )

        # Status text
        self.status_font = tkfont.Font(family='Arial', size=9)
        self.status_text = self.canvas.create_text(
            self.window_size//2,
            self.window_size//2 + 25,
            text="Listening...",
            font=self.status_font,
            fill='white'
        )

        # Reset button (double-click to reset)
        self.canvas.bind('<Double-Button-1>', self.reset_timer)

    def start_drag(self, event):
        self.drag_x = event.x
        self.drag_y = event.y

    def drag_motion(self, event):
        x = self.root.winfo_x() + (event.x - self.drag_x)
        y = self.root.winfo_y() + (event.y - self.drag_y)
        self.root.geometry(f'+{x}+{y}')

    def monitor_audio(self):
        """Monitor microphone for voice activity"""
        try:
            with sd.InputStream(callback=self.audio_callback, channels=1, samplerate=16000):
                while self.is_listening:
                    time.sleep(0.1)
        except Exception as e:
            print(f"Audio error: {e}")
            print("Make sure your microphone is accessible!")

    def audio_callback(self, indata, frames, time_info, status):
        """Called continuously with audio data"""
        if self.is_running:
            return  # Already running, don't need to detect

        # Calculate volume (RMS)
        volume = np.sqrt(np.mean(indata**2))

        # Check if voice detected
        if volume > self.audio_threshold:
            if self.speech_start_time is None:
                self.speech_start_time = time.time()
            else:
                # Check if we've had sustained speech
                duration = time.time() - self.speech_start_time
                if duration >= self.speech_duration_needed and not self.is_running:
                    self.start_timer()
        else:
            # Reset if silence
            self.speech_start_time = None

    def start_timer(self):
        """Start the timer"""
        if not self.is_running:
            self.is_running = True
            self.start_time = time.time()
            print("🎤 Timer started!")

    def reset_timer(self, event=None):
        """Reset timer to zero"""
        self.is_running = False
        self.start_time = None
        self.elapsed_seconds = 0
        self.speech_start_time = None
        self.update_display(0)
        print("🔄 Timer reset!")

    def update_timer(self):
        """Update timer display every 100ms"""
        if self.is_running:
            self.elapsed_seconds = time.time() - self.start_time

        self.update_display(self.elapsed_seconds)

        # Schedule next update
        self.root.after(100, self.update_timer)

    def update_display(self, seconds):
        """Update the visual display based on elapsed time"""
        # Format time
        minutes = int(seconds // 60)
        secs = int(seconds % 60)
        time_str = f"{minutes:02d}:{secs:02d}"

        # Update text
        self.canvas.itemconfig(self.timer_text, text=time_str)

        # Update color based on time
        if seconds < 60:
            # Green (0-60s)
            color = '#4CAF50'
            outline = '#2E7D32'
            status = "On track ✓"
        elif seconds < 90:
            # Yellow (60-90s)
            color = '#FFC107'
            outline = '#F57F17'
            status = "Wrap up!"
        else:
            # Red (90s+)
            color = '#F44336'
            outline = '#C62828'
            status = "Finish now!"

        # Update circle color
        self.canvas.itemconfig(self.circle, fill=color, outline=outline)

        # Update status text
        if not self.is_running:
            status = "Listening..."
        self.canvas.itemconfig(self.status_text, text=status)

    def run(self):
        """Start the application"""
        print("🎯 Interview Timer Started!")
        print("📍 Drag the window to reposition")
        print("🎤 Start speaking to auto-start timer")
        print("⏸️  Double-click to reset")
        print("❌ Close window to exit")
        self.root.mainloop()
        self.is_listening = False

if __name__ == "__main__":
    print("\n" + "="*50)
    print("INTERVIEW ANSWER TIMER")
    print("="*50)

    try:
        app = InterviewTimer()
        app.run()
    except KeyboardInterrupt:
        print("\n👋 Timer closed!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nTroubleshooting:")
        print("1. Install dependencies: pip install sounddevice numpy")
        print("2. Check microphone permissions")
        print("3. Try adjusting audio_threshold in code (line 41)")
