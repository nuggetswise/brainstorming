#!/usr/bin/env python3
"""
Interview Whisperer - Main Launcher GUI
A beautiful, modern interface for managing your AI interview copilot
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import subprocess
import json
import threading
from pathlib import Path

# Import copilot
from interview_copilot import InterviewCopilot


class InterviewWhispererLauncher:
    """Main launcher window for Interview Whisperer"""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Interview Whisperer")
        self.root.geometry("600x550")
        self.root.resizable(False, False)

        # Paths
        self.base_dir = Path("/home/user/interview-whisperer")
        self.docs_dir = self.base_dir / "documents"
        self.vector_db_dir = self.base_dir / "data" / "chroma_db"

        # Status variables
        self.ollama_status = tk.StringVar(value="Checking...")
        self.doc_count = tk.StringVar(value="Checking...")
        self.ready_status = tk.StringVar(value="Initializing...")

        # Interview copilot
        self.copilot = InterviewCopilot()
        self.interview_active = False

        # Setup UI
        self._setup_styles()
        self._create_ui()

        # Cleanup on close
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Initial status check
        self.root.after(500, self.refresh_status)

    def _setup_styles(self):
        """Configure modern dark theme styles"""
        style = ttk.Style()

        # Configure colors
        bg_dark = "#1e1e2e"
        bg_medium = "#2a2a3e"
        bg_light = "#363650"
        fg_primary = "#ffffff"
        fg_secondary = "#b4b4c8"
        accent_blue = "#89b4fa"
        accent_green = "#a6e3a1"
        accent_yellow = "#f9e2af"
        accent_red = "#f38ba8"

        # Configure root background
        self.root.configure(bg=bg_dark)

        # Configure custom styles
        style.configure("Dark.TFrame", background=bg_dark)
        style.configure("Medium.TFrame", background=bg_medium, relief="flat")
        style.configure("Light.TFrame", background=bg_light, relief="flat")

        style.configure("Title.TLabel",
                       background=bg_dark,
                       foreground=fg_primary,
                       font=("Arial", 24, "bold"))

        style.configure("Subtitle.TLabel",
                       background=bg_dark,
                       foreground=fg_secondary,
                       font=("Arial", 11))

        style.configure("Header.TLabel",
                       background=bg_medium,
                       foreground=fg_primary,
                       font=("Arial", 12, "bold"))

        style.configure("Status.TLabel",
                       background=bg_medium,
                       foreground=fg_secondary,
                       font=("Arial", 10))

        style.configure("Info.TLabel",
                       background=bg_dark,
                       foreground=fg_secondary,
                       font=("Arial", 9))

        # Store colors for later use
        self.colors = {
            'bg_dark': bg_dark,
            'bg_medium': bg_medium,
            'bg_light': bg_light,
            'fg_primary': fg_primary,
            'fg_secondary': fg_secondary,
            'accent_blue': accent_blue,
            'accent_green': accent_green,
            'accent_yellow': accent_yellow,
            'accent_red': accent_red
        }

    def _create_ui(self):
        """Build the main user interface"""
        # Main container
        main_frame = ttk.Frame(self.root, style="Dark.TFrame", padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Header Section
        self._create_header(main_frame)

        # Status Section
        self._create_status_section(main_frame)

        # Action Buttons Section
        self._create_action_section(main_frame)

        # Footer Info Section
        self._create_footer(main_frame)

    def _create_header(self, parent):
        """Create the header with title and subtitle"""
        header_frame = ttk.Frame(parent, style="Dark.TFrame")
        header_frame.pack(fill=tk.X, pady=(0, 20))

        # Title
        title = ttk.Label(header_frame,
                         text="🎯 Interview Whisperer",
                         style="Title.TLabel")
        title.pack()

        # Subtitle
        subtitle = ttk.Label(header_frame,
                            text="AI-Powered Interview Copilot (100% Local & Private)",
                            style="Subtitle.TLabel")
        subtitle.pack(pady=(5, 0))

    def _create_status_section(self, parent):
        """Create the status display section"""
        status_frame = ttk.Frame(parent, style="Medium.TFrame", padding="15")
        status_frame.pack(fill=tk.X, pady=(0, 15))

        # Section header
        header = ttk.Label(status_frame,
                          text="System Status",
                          style="Header.TLabel")
        header.pack(anchor=tk.W, pady=(0, 10))

        # Status items
        self.status_ready = self._create_status_item(status_frame, "Ready Status:", self.ready_status)
        self.status_ollama = self._create_status_item(status_frame, "🤖 Ollama:", self.ollama_status)
        self.status_docs = self._create_status_item(status_frame, "📄 Documents:", self.doc_count)

        # Refresh button
        refresh_btn = tk.Button(status_frame,
                               text="🔄 Refresh Status",
                               command=self.refresh_status,
                               bg=self.colors['bg_light'],
                               fg=self.colors['fg_primary'],
                               activebackground=self.colors['accent_blue'],
                               activeforeground=self.colors['fg_primary'],
                               font=("Arial", 9),
                               relief=tk.FLAT,
                               cursor="hand2",
                               padx=10,
                               pady=5)
        refresh_btn.pack(anchor=tk.E, pady=(10, 0))

    def _create_status_item(self, parent, label_text, var):
        """Create a single status display item"""
        frame = ttk.Frame(parent, style="Medium.TFrame")
        frame.pack(fill=tk.X, pady=3)

        label = ttk.Label(frame,
                         text=label_text,
                         style="Status.TLabel",
                         width=15)
        label.pack(side=tk.LEFT)

        value = ttk.Label(frame,
                         textvariable=var,
                         style="Status.TLabel")
        value.pack(side=tk.LEFT, padx=(10, 0))

        return value

    def _create_action_section(self, parent):
        """Create the main action buttons"""
        action_frame = ttk.Frame(parent, style="Dark.TFrame")
        action_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Manage Documents Button
        self.btn_manage = tk.Button(action_frame,
                                    text="📁 Manage Documents",
                                    command=self.open_document_manager,
                                    bg=self.colors['accent_blue'],
                                    fg=self.colors['bg_dark'],
                                    activebackground=self.colors['bg_light'],
                                    activeforeground=self.colors['fg_primary'],
                                    font=("Arial", 14, "bold"),
                                    relief=tk.FLAT,
                                    cursor="hand2",
                                    padx=20,
                                    pady=15)
        self.btn_manage.pack(fill=tk.X, pady=8)

        # Start Interview Mode Button
        self.btn_start = tk.Button(action_frame,
                                   text="🎯 Start Interview Mode",
                                   command=self.start_interview_mode,
                                   bg=self.colors['accent_green'],
                                   fg=self.colors['bg_dark'],
                                   activebackground=self.colors['bg_light'],
                                   activeforeground=self.colors['fg_primary'],
                                   font=("Arial", 14, "bold"),
                                   relief=tk.FLAT,
                                   cursor="hand2",
                                   padx=20,
                                   pady=15)
        self.btn_start.pack(fill=tk.X, pady=8)

        # Settings Button
        self.btn_settings = tk.Button(action_frame,
                                      text="⚙️ Settings",
                                      command=self.open_settings,
                                      bg=self.colors['bg_light'],
                                      fg=self.colors['fg_primary'],
                                      activebackground=self.colors['bg_medium'],
                                      activeforeground=self.colors['fg_primary'],
                                      font=("Arial", 12),
                                      relief=tk.FLAT,
                                      cursor="hand2",
                                      padx=20,
                                      pady=12)
        self.btn_settings.pack(fill=tk.X, pady=8)

    def _create_footer(self, parent):
        """Create the footer info section"""
        footer_frame = ttk.Frame(parent, style="Dark.TFrame")
        footer_frame.pack(fill=tk.X, pady=(15, 0))

        # Separator line
        separator = ttk.Frame(footer_frame, style="Light.TFrame", height=1)
        separator.pack(fill=tk.X, pady=(0, 10))

        # Documents folder info
        docs_info = ttk.Label(footer_frame,
                             text=f"📂 Documents folder: {self.docs_dir}",
                             style="Info.TLabel")
        docs_info.pack(anchor=tk.W)

        # Help text
        help_text = ttk.Label(footer_frame,
                             text="💡 Click 'Manage Documents' to add your interview prep materials",
                             style="Info.TLabel")
        help_text.pack(anchor=tk.W, pady=(5, 0))

    def check_ollama_status(self):
        """Check if Ollama is installed and running"""
        try:
            # Check if ollama command exists
            result = subprocess.run(['which', 'ollama'],
                                  capture_output=True,
                                  text=True,
                                  timeout=2)

            if result.returncode != 0:
                return "Not installed", False

            # Check if Ollama service is running
            result = subprocess.run(['ollama', 'list'],
                                  capture_output=True,
                                  text=True,
                                  timeout=5)

            if result.returncode == 0:
                return "✅ Connected", True
            else:
                return "⚠️ Not running", False

        except subprocess.TimeoutExpired:
            return "⏱️ Timeout", False
        except Exception as e:
            return "❌ Error", False

    def check_documents_status(self):
        """Check document processing status"""
        try:
            # Count files in documents directory
            if not self.docs_dir.exists():
                return "📂 No documents folder", 0, False

            doc_files = list(self.docs_dir.glob('**/*'))
            doc_files = [f for f in doc_files if f.is_file() and f.suffix in ['.pdf', '.txt', '.docx', '.md']]

            # Check if vector database exists
            vectordb_exists = self.vector_db_dir.exists()

            if len(doc_files) == 0:
                return "📄 No documents (0 files)", 0, False
            elif not vectordb_exists:
                return f"⚠️ {len(doc_files)} files (not processed)", len(doc_files), False
            else:
                # Try to count chunks
                try:
                    # This is a placeholder - actual implementation would check vectordb
                    chunks = "unknown"
                    return f"✅ {len(doc_files)} files processed", len(doc_files), True
                except:
                    return f"✅ {len(doc_files)} files processed", len(doc_files), True

        except Exception as e:
            return f"❌ Error checking documents", 0, False

    def refresh_status(self):
        """Refresh all status indicators"""
        # Check Ollama
        ollama_text, ollama_ok = self.check_ollama_status()
        self.ollama_status.set(ollama_text)

        # Check Documents
        docs_text, doc_count, docs_ok = self.check_documents_status()
        self.doc_count.set(docs_text)

        # Update ready status
        if ollama_ok and docs_ok:
            self.ready_status.set("✅ Ready to start!")
            self.btn_start.config(state=tk.NORMAL)
        elif not ollama_ok:
            self.ready_status.set("⚠️ Ollama not available")
            self.btn_start.config(state=tk.DISABLED)
        elif not docs_ok:
            if doc_count == 0:
                self.ready_status.set("📄 Please add documents first")
            else:
                self.ready_status.set("⚙️ Please process documents first")
            self.btn_start.config(state=tk.DISABLED)
        else:
            self.ready_status.set("⚠️ System not ready")
            self.btn_start.config(state=tk.DISABLED)

    def open_document_manager(self):
        """Open the document management window"""
        # Create a new window
        doc_window = tk.Toplevel(self.root)
        doc_window.title("Document Manager")
        doc_window.geometry("700x500")
        doc_window.configure(bg=self.colors['bg_dark'])

        # Main frame
        main_frame = ttk.Frame(doc_window, style="Dark.TFrame", padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Header
        header = ttk.Label(
            main_frame,
            text="📁 Document Manager",
            style="Title.TLabel"
        )
        header.pack(pady=(0, 20))

        # Info text
        info_frame = ttk.Frame(main_frame, style="Medium.TFrame", padding="15")
        info_frame.pack(fill=tk.X, pady=(0, 15))

        info_text = ttk.Label(
            info_frame,
            text=f"Documents folder: {self.docs_dir}\n\n"
                 "Add PDF, DOCX, TXT, or MD files to this folder, then click 'Process Documents'.",
            style="Status.TLabel",
            wraplength=650,
            justify=tk.LEFT
        )
        info_text.pack()

        # Action buttons
        btn_frame = ttk.Frame(main_frame, style="Dark.TFrame")
        btn_frame.pack(fill=tk.X, pady=10)

        # Open folder button
        open_btn = tk.Button(
            btn_frame,
            text="📂 Open Documents Folder",
            command=lambda: subprocess.run(['open', str(self.docs_dir)]),
            bg=self.colors['accent_blue'],
            fg=self.colors['bg_dark'],
            font=("Arial", 12, "bold"),
            relief=tk.FLAT,
            cursor="hand2",
            padx=15,
            pady=10
        )
        open_btn.pack(fill=tk.X, pady=5)

        # Process documents button
        process_btn = tk.Button(
            btn_frame,
            text="⚙️ Process Documents",
            command=lambda: self.process_documents(doc_window),
            bg=self.colors['accent_green'],
            fg=self.colors['bg_dark'],
            font=("Arial", 12, "bold"),
            relief=tk.FLAT,
            cursor="hand2",
            padx=15,
            pady=10
        )
        process_btn.pack(fill=tk.X, pady=5)

        # Clear database button
        clear_btn = tk.Button(
            btn_frame,
            text="🗑️ Clear Database",
            command=self.clear_database,
            bg=self.colors['accent_red'],
            fg=self.colors['bg_dark'],
            font=("Arial", 12, "bold"),
            relief=tk.FLAT,
            cursor="hand2",
            padx=15,
            pady=10
        )
        clear_btn.pack(fill=tk.X, pady=5)

        # Status display
        status_frame = ttk.Frame(main_frame, style="Medium.TFrame", padding="15")
        status_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))

        status_label = ttk.Label(
            status_frame,
            text="Status:",
            style="Header.TLabel"
        )
        status_label.pack(anchor=tk.W, pady=(0, 10))

        # Get current stats
        if self.copilot.document_processor is None:
            try:
                from document_processor import DocumentProcessor
                from config import DOCUMENTS_DIR, CHROMA_DB_DIR
                self.copilot.document_processor = DocumentProcessor(
                    str(DOCUMENTS_DIR), str(CHROMA_DB_DIR)
                )
            except Exception as e:
                pass

        if self.copilot.document_processor:
            stats = self.copilot.document_processor.get_stats()
            status_text = f"Files processed: {stats['files_processed']}\n"
            status_text += f"Total chunks: {stats['total_chunks']}\n"
            status_text += f"Last updated: {stats['last_updated']}"
        else:
            status_text = "Document processor not initialized"

        status_info = ttk.Label(
            status_frame,
            text=status_text,
            style="Status.TLabel",
            justify=tk.LEFT
        )
        status_info.pack(anchor=tk.W)

    def process_documents(self, parent_window):
        """Process documents in a background thread"""
        # Create progress window
        progress_window = tk.Toplevel(parent_window)
        progress_window.title("Processing Documents")
        progress_window.geometry("500x200")
        progress_window.configure(bg=self.colors['bg_dark'])

        frame = ttk.Frame(progress_window, style="Dark.TFrame", padding="20")
        frame.pack(fill=tk.BOTH, expand=True)

        title = ttk.Label(
            frame,
            text="⚙️ Processing Documents...",
            style="Title.TLabel"
        )
        title.pack(pady=(0, 20))

        progress_text = tk.StringVar(value="Starting...")
        progress_label = ttk.Label(
            frame,
            textvariable=progress_text,
            style="Status.TLabel"
        )
        progress_label.pack()

        progress_bar = ttk.Progressbar(
            frame,
            mode='determinate',
            length=400
        )
        progress_bar.pack(pady=20)

        def progress_callback(current, total, message):
            progress_text.set(f"[{current}/{total}] {message}")
            progress_bar['maximum'] = total
            progress_bar['value'] = current
            progress_window.update()

        def do_processing():
            try:
                if self.copilot.document_processor is None:
                    from document_processor import DocumentProcessor
                    from config import DOCUMENTS_DIR, CHROMA_DB_DIR
                    self.copilot.document_processor = DocumentProcessor(
                        str(DOCUMENTS_DIR), str(CHROMA_DB_DIR)
                    )

                results = self.copilot.document_processor.process_all_documents(
                    progress_callback=progress_callback
                )

                progress_window.destroy()

                # Show results
                messagebox.showinfo(
                    "Processing Complete",
                    f"✅ Successfully processed {results['processed_files']} files!\n\n"
                    f"Total chunks: {results['total_chunks']}\n"
                    f"Failed: {results['failed_files']}"
                )

                # Refresh status
                self.refresh_status()

            except Exception as e:
                progress_window.destroy()
                messagebox.showerror("Error", f"Processing failed:\n{str(e)}")

        # Run in background thread
        threading.Thread(target=do_processing, daemon=True).start()

    def clear_database(self):
        """Clear the vector database"""
        confirm = messagebox.askyesno(
            "Clear Database",
            "Are you sure you want to clear the vector database?\n\n"
            "This will remove all processed documents.\n"
            "You'll need to reprocess your documents."
        )

        if confirm:
            try:
                if self.copilot.document_processor:
                    self.copilot.document_processor.clear_database()
                    messagebox.showinfo("Success", "Database cleared successfully!")
                    self.refresh_status()
                else:
                    messagebox.showerror("Error", "Document processor not initialized")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to clear database:\n{str(e)}")

    def start_interview_mode(self):
        """Launch the interview copilot"""
        if self.interview_active:
            # Stop interview mode
            self.stop_interview_mode()
            return

        # Check prerequisites
        prereqs = self.copilot.check_prerequisites()

        if not prereqs['ready']:
            issues_text = "\n".join(f"• {issue}" for issue in prereqs['issues'])
            messagebox.showwarning(
                "Not Ready",
                f"Cannot start Interview Mode:\n\n{issues_text}"
            )
            return

        try:
            # Start interview mode
            if self.copilot.start_interview_mode():
                self.interview_active = True
                self.btn_start.config(
                    text="🛑 Stop Interview Mode",
                    bg=self.colors['accent_red']
                )
                self.ready_status.set("🎯 Interview Mode Active")

                messagebox.showinfo(
                    "Interview Mode Started",
                    "✅ Interview Copilot is now listening!\n\n"
                    "Speak your interview questions naturally.\n"
                    "Suggestions will appear in the overlay window.\n\n"
                    "Click 'Stop Interview Mode' when done."
                )
            else:
                messagebox.showerror(
                    "Error",
                    "Failed to start Interview Mode.\n"
                    "Check the logs for details."
                )

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Failed to start Interview Mode:\n{str(e)}"
            )

    def stop_interview_mode(self):
        """Stop the interview copilot"""
        try:
            if self.copilot.stop_interview_mode():
                self.interview_active = False
                self.btn_start.config(
                    text="🎯 Start Interview Mode",
                    bg=self.colors['accent_green']
                )

                # Get session stats
                status = self.copilot.get_status()

                messagebox.showinfo(
                    "Interview Mode Stopped",
                    f"Session complete!\n\n"
                    f"Questions answered: {status['questions_answered']}\n"
                    f"Duration: {status['session_duration']:.0f} seconds"
                )

                self.refresh_status()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to stop Interview Mode:\n{str(e)}")

    def open_settings(self):
        """Open settings window"""
        messagebox.showinfo(
            "Settings",
            "Settings panel will be implemented next.\n\n"
            "Planned settings:\n"
            "• Ollama model selection\n"
            "• Voice activation sensitivity\n"
            "• Display preferences\n"
            "• Document processing options"
        )

    def on_close(self):
        """Handle window close"""
        if self.interview_active:
            confirm = messagebox.askyesno(
                "Interview Active",
                "Interview mode is active. Stop and exit?"
            )
            if confirm:
                self.stop_interview_mode()
            else:
                return

        # Cleanup copilot
        try:
            self.copilot.cleanup()
        except:
            pass

        self.root.destroy()

    def run(self):
        """Start the application"""
        self.root.mainloop()


def main():
    """Application entry point"""
    app = InterviewWhispererLauncher()
    app.run()


if __name__ == "__main__":
    main()
