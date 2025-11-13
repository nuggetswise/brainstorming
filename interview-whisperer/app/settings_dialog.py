#!/usr/bin/env python3
"""
Settings Dialog for Interview Whisperer
Beautiful tabbed interface for all application settings
"""

import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
from typing import Optional, Callable
from settings_manager import SettingsManager


class SettingsDialog:
    """
    Modal settings dialog with tabbed interface.

    Features:
    - 4 tabs: Audio, Display, Document, LLM
    - Live validation
    - Save/Cancel/Reset buttons
    - Beautiful dark theme
    """

    def __init__(self, parent: tk.Tk, settings_manager: SettingsManager, on_save: Optional[Callable] = None):
        """
        Initialize settings dialog.

        Args:
            parent: Parent window
            settings_manager: SettingsManager instance
            on_save: Optional callback when settings are saved
        """
        self.parent = parent
        self.settings = settings_manager
        self.on_save = on_save
        self.result = None

        # Create dialog window
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("⚙️ Settings")
        self.dialog.geometry("700x600")
        self.dialog.resizable(False, False)
        self.dialog.transient(parent)
        self.dialog.grab_set()

        # Colors (match launcher theme)
        self.colors = {
            'bg_dark': '#1e1e2e',
            'bg_medium': '#2a2a3e',
            'bg_light': '#363650',
            'fg_primary': '#ffffff',
            'fg_secondary': '#b4b4c8',
            'accent_blue': '#89b4fa',
            'accent_green': '#a6e3a1',
            'accent_yellow': '#f9e2af',
            'accent_red': '#f38ba8'
        }

        self.dialog.configure(bg=self.colors['bg_dark'])

        # Setup styles
        self._setup_styles()

        # Create UI
        self._create_ui()

        # Center dialog
        self._center_dialog()

    def _setup_styles(self):
        """Configure custom styles"""
        style = ttk.Style()

        style.configure("Dark.TFrame", background=self.colors['bg_dark'])
        style.configure("Medium.TFrame", background=self.colors['bg_medium'])

        style.configure("Title.TLabel",
                       background=self.colors['bg_dark'],
                       foreground=self.colors['fg_primary'],
                       font=("Arial", 16, "bold"))

        style.configure("Header.TLabel",
                       background=self.colors['bg_medium'],
                       foreground=self.colors['fg_primary'],
                       font=("Arial", 11, "bold"))

        style.configure("Label.TLabel",
                       background=self.colors['bg_medium'],
                       foreground=self.colors['fg_secondary'],
                       font=("Arial", 10))

        style.configure("Info.TLabel",
                       background=self.colors['bg_medium'],
                       foreground=self.colors['accent_blue'],
                       font=("Arial", 9))

    def _create_ui(self):
        """Build the main user interface"""
        # Main container
        main_frame = ttk.Frame(self.dialog, style="Dark.TFrame", padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Header
        header = ttk.Label(main_frame,
                          text="⚙️ Application Settings",
                          style="Title.TLabel")
        header.pack(pady=(0, 20))

        # Notebook (tabs)
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

        # Create tabs
        self._create_audio_tab()
        self._create_display_tab()
        self._create_document_tab()
        self._create_llm_tab()

        # Buttons
        self._create_buttons(main_frame)

    def _create_audio_tab(self):
        """Create audio settings tab"""
        frame = ttk.Frame(self.notebook, style="Medium.TFrame", padding="20")
        self.notebook.add(frame, text="🎤 Audio")

        # Whisper Model
        self._create_label(frame, "Whisper Model:", 0)
        self.whisper_var = tk.StringVar(value=self.settings.audio.whisper_model)
        whisper_combo = ttk.Combobox(frame, textvariable=self.whisper_var,
                                     values=['tiny', 'base', 'small', 'medium', 'large'],
                                     state='readonly', width=30)
        whisper_combo.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        self._create_info(frame, "Tiny=fastest, Large=most accurate", 1)

        # Voice Activation Sensitivity
        self._create_label(frame, "Voice Activation Sensitivity:", 2)
        self.sensitivity_var = tk.DoubleVar(value=self.settings.audio.silence_threshold)
        sensitivity_scale = tk.Scale(frame,
                                     from_=0.001, to=0.1,
                                     resolution=0.001,
                                     orient=tk.HORIZONTAL,
                                     variable=self.sensitivity_var,
                                     bg=self.colors['bg_medium'],
                                     fg=self.colors['fg_primary'],
                                     highlightthickness=0,
                                     length=300)
        sensitivity_scale.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
        self._create_info(frame, "Lower=more sensitive, Higher=less sensitive", 3)

        # Chunk Duration
        self._create_label(frame, "Transcription Chunk (seconds):", 4)
        self.chunk_dur_var = tk.DoubleVar(value=self.settings.audio.chunk_duration)
        chunk_spin = tk.Spinbox(frame,
                               from_=1, to=30, increment=1,
                               textvariable=self.chunk_dur_var,
                               width=10,
                               bg=self.colors['bg_light'],
                               fg=self.colors['fg_primary'])
        chunk_spin.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)
        self._create_info(frame, "How often to transcribe audio", 5)

        # Silence Duration
        self._create_label(frame, "Silence Duration (seconds):", 6)
        self.silence_dur_var = tk.DoubleVar(value=self.settings.audio.silence_duration)
        silence_spin = tk.Spinbox(frame,
                                 from_=0.5, to=5.0, increment=0.5,
                                 textvariable=self.silence_dur_var,
                                 width=10,
                                 bg=self.colors['bg_light'],
                                 fg=self.colors['fg_primary'])
        silence_spin.grid(row=6, column=1, padx=10, pady=5, sticky=tk.W)
        self._create_info(frame, "Silence after speech to trigger question", 7)

        # Context Duration
        self._create_label(frame, "Context Window (seconds):", 8)
        self.context_dur_var = tk.DoubleVar(value=self.settings.audio.context_duration)
        context_spin = tk.Spinbox(frame,
                                 from_=10, to=120, increment=10,
                                 textvariable=self.context_dur_var,
                                 width=10,
                                 bg=self.colors['bg_light'],
                                 fg=self.colors['fg_primary'])
        context_spin.grid(row=8, column=1, padx=10, pady=5, sticky=tk.W)
        self._create_info(frame, "How much audio context to keep", 9)

    def _create_display_tab(self):
        """Create display preferences tab"""
        frame = ttk.Frame(self.notebook, style="Medium.TFrame", padding="20")
        self.notebook.add(frame, text="🖥️ Display")

        # Window Size
        self._create_label(frame, "Overlay Width (pixels):", 0)
        self.width_var = tk.IntVar(value=self.settings.display.width)
        width_spin = tk.Spinbox(frame,
                               from_=200, to=1000, increment=50,
                               textvariable=self.width_var,
                               width=10,
                               bg=self.colors['bg_light'],
                               fg=self.colors['fg_primary'])
        width_spin.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        self._create_label(frame, "Overlay Height (pixels):", 1)
        self.height_var = tk.IntVar(value=self.settings.display.height)
        height_spin = tk.Spinbox(frame,
                                from_=200, to=800, increment=50,
                                textvariable=self.height_var,
                                width=10,
                                bg=self.colors['bg_light'],
                                fg=self.colors['fg_primary'])
        height_spin.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        # Transparency
        self._create_label(frame, "Transparency:", 2)
        self.transparency_var = tk.DoubleVar(value=self.settings.display.transparency)
        transparency_scale = tk.Scale(frame,
                                     from_=0.3, to=1.0,
                                     resolution=0.05,
                                     orient=tk.HORIZONTAL,
                                     variable=self.transparency_var,
                                     bg=self.colors['bg_medium'],
                                     fg=self.colors['fg_primary'],
                                     highlightthickness=0,
                                     length=300)
        transparency_scale.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
        self._create_info(frame, "1.0 = fully opaque, 0.3 = very transparent", 3)

        # Position
        self._create_label(frame, "Overlay Position:", 4)
        self.position_var = tk.StringVar(value=self.settings.display.position)
        position_combo = ttk.Combobox(frame, textvariable=self.position_var,
                                     values=['top-right', 'top-left', 'bottom-right', 'bottom-left', 'center'],
                                     state='readonly', width=30)
        position_combo.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)

        # Font Size
        self._create_label(frame, "Font Size:", 5)
        self.fontsize_var = tk.IntVar(value=self.settings.display.font_size)
        fontsize_spin = tk.Spinbox(frame,
                                  from_=8, to=16, increment=1,
                                  textvariable=self.fontsize_var,
                                  width=10,
                                  bg=self.colors['bg_light'],
                                  fg=self.colors['fg_primary'])
        fontsize_spin.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)

        # Always on Top
        self._create_label(frame, "Always on Top:", 6)
        self.ontop_var = tk.BooleanVar(value=self.settings.display.always_on_top)
        ontop_check = tk.Checkbutton(frame,
                                    variable=self.ontop_var,
                                    bg=self.colors['bg_medium'],
                                    fg=self.colors['fg_primary'],
                                    selectcolor=self.colors['bg_light'])
        ontop_check.grid(row=6, column=1, padx=10, pady=5, sticky=tk.W)

        # Show Confidence
        self._create_label(frame, "Show Confidence Scores:", 7)
        self.confidence_var = tk.BooleanVar(value=self.settings.display.show_confidence)
        confidence_check = tk.Checkbutton(frame,
                                         variable=self.confidence_var,
                                         bg=self.colors['bg_medium'],
                                         fg=self.colors['fg_primary'],
                                         selectcolor=self.colors['bg_light'])
        confidence_check.grid(row=7, column=1, padx=10, pady=5, sticky=tk.W)

        # Show Sources
        self._create_label(frame, "Show Source Documents:", 8)
        self.sources_var = tk.BooleanVar(value=self.settings.display.show_sources)
        sources_check = tk.Checkbutton(frame,
                                      variable=self.sources_var,
                                      bg=self.colors['bg_medium'],
                                      fg=self.colors['fg_primary'],
                                      selectcolor=self.colors['bg_light'])
        sources_check.grid(row=8, column=1, padx=10, pady=5, sticky=tk.W)

    def _create_document_tab(self):
        """Create document processing tab"""
        frame = ttk.Frame(self.notebook, style="Medium.TFrame", padding="20")
        self.notebook.add(frame, text="📄 Documents")

        # Chunk Size
        self._create_label(frame, "Chunk Size (words):", 0)
        self.chunk_size_var = tk.IntVar(value=self.settings.document.chunk_size)
        chunk_size_spin = tk.Spinbox(frame,
                                    from_=100, to=1000, increment=50,
                                    textvariable=self.chunk_size_var,
                                    width=10,
                                    bg=self.colors['bg_light'],
                                    fg=self.colors['fg_primary'])
        chunk_size_spin.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        self._create_info(frame, "How many words per chunk", 1)

        # Chunk Overlap
        self._create_label(frame, "Chunk Overlap (words):", 2)
        self.chunk_overlap_var = tk.IntVar(value=self.settings.document.chunk_overlap)
        overlap_spin = tk.Spinbox(frame,
                                 from_=0, to=200, increment=10,
                                 textvariable=self.chunk_overlap_var,
                                 width=10,
                                 bg=self.colors['bg_light'],
                                 fg=self.colors['fg_primary'])
        overlap_spin.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
        self._create_info(frame, "Overlap between chunks for continuity", 3)

        # Supported Extensions
        self._create_label(frame, "Supported File Types:", 4)
        extensions_text = ", ".join(self.settings.document.supported_extensions)
        extensions_label = ttk.Label(frame,
                                    text=extensions_text,
                                    style="Info.TLabel")
        extensions_label.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)

        # Auto Process
        self._create_label(frame, "Auto-Process New Documents:", 5)
        self.auto_process_var = tk.BooleanVar(value=self.settings.document.auto_process)
        auto_check = tk.Checkbutton(frame,
                                   variable=self.auto_process_var,
                                   bg=self.colors['bg_medium'],
                                   fg=self.colors['fg_primary'],
                                   selectcolor=self.colors['bg_light'])
        auto_check.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)
        self._create_info(frame, "Automatically process when documents folder changes", 6)

    def _create_llm_tab(self):
        """Create LLM settings tab"""
        frame = ttk.Frame(self.notebook, style="Medium.TFrame", padding="20")
        self.notebook.add(frame, text="🤖 LLM")

        # LLM Model
        self._create_label(frame, "Ollama LLM Model:", 0)
        self.llm_model_var = tk.StringVar(value=self.settings.llm.ollama_llm_model)
        llm_entry = tk.Entry(frame,
                            textvariable=self.llm_model_var,
                            width=35,
                            bg=self.colors['bg_light'],
                            fg=self.colors['fg_primary'])
        llm_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        # Button to list models
        list_btn = tk.Button(frame,
                            text="📋 List Models",
                            command=self._list_ollama_models,
                            bg=self.colors['accent_blue'],
                            fg=self.colors['bg_dark'],
                            font=("Arial", 9),
                            relief=tk.FLAT,
                            cursor="hand2")
        list_btn.grid(row=0, column=2, padx=5)

        # Embedding Model
        self._create_label(frame, "Embedding Model:", 1)
        self.embed_model_var = tk.StringVar(value=self.settings.llm.ollama_embed_model)
        embed_entry = tk.Entry(frame,
                              textvariable=self.embed_model_var,
                              width=35,
                              bg=self.colors['bg_light'],
                              fg=self.colors['fg_primary'])
        embed_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        # Temperature
        self._create_label(frame, "Temperature:", 2)
        self.temperature_var = tk.DoubleVar(value=self.settings.llm.temperature)
        temp_scale = tk.Scale(frame,
                             from_=0.0, to=2.0,
                             resolution=0.1,
                             orient=tk.HORIZONTAL,
                             variable=self.temperature_var,
                             bg=self.colors['bg_medium'],
                             fg=self.colors['fg_primary'],
                             highlightthickness=0,
                             length=300)
        temp_scale.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
        self._create_info(frame, "0.0 = deterministic, 2.0 = very creative", 3)

        # Max Tokens
        self._create_label(frame, "Max Answer Tokens:", 4)
        self.max_tokens_var = tk.IntVar(value=self.settings.llm.max_tokens)
        tokens_spin = tk.Spinbox(frame,
                                from_=50, to=1000, increment=50,
                                textvariable=self.max_tokens_var,
                                width=10,
                                bg=self.colors['bg_light'],
                                fg=self.colors['fg_primary'])
        tokens_spin.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)
        self._create_info(frame, "Maximum length of generated answers", 5)

        # Context Results
        self._create_label(frame, "Context Chunks to Retrieve:", 6)
        self.n_results_var = tk.IntVar(value=self.settings.llm.n_results)
        results_spin = tk.Spinbox(frame,
                                 from_=1, to=10, increment=1,
                                 textvariable=self.n_results_var,
                                 width=10,
                                 bg=self.colors['bg_light'],
                                 fg=self.colors['fg_primary'])
        results_spin.grid(row=6, column=1, padx=10, pady=5, sticky=tk.W)
        self._create_info(frame, "How many document chunks to use for context", 7)

        # Ollama Host
        self._create_label(frame, "Ollama Host:", 8)
        self.ollama_host_var = tk.StringVar(value=self.settings.llm.ollama_host)
        host_entry = tk.Entry(frame,
                             textvariable=self.ollama_host_var,
                             width=35,
                             bg=self.colors['bg_light'],
                             fg=self.colors['fg_primary'])
        host_entry.grid(row=8, column=1, padx=10, pady=5, sticky=tk.W)

    def _create_buttons(self, parent):
        """Create action buttons"""
        btn_frame = ttk.Frame(parent, style="Dark.TFrame")
        btn_frame.pack(fill=tk.X)

        # Save button
        save_btn = tk.Button(btn_frame,
                            text="💾 Save Settings",
                            command=self._save_settings,
                            bg=self.colors['accent_green'],
                            fg=self.colors['bg_dark'],
                            font=("Arial", 12, "bold"),
                            relief=tk.FLAT,
                            cursor="hand2",
                            padx=20,
                            pady=10)
        save_btn.pack(side=tk.LEFT, padx=5)

        # Reset button
        reset_btn = tk.Button(btn_frame,
                             text="🔄 Reset to Defaults",
                             command=self._reset_settings,
                             bg=self.colors['accent_yellow'],
                             fg=self.colors['bg_dark'],
                             font=("Arial", 12, "bold"),
                             relief=tk.FLAT,
                             cursor="hand2",
                             padx=20,
                             pady=10)
        reset_btn.pack(side=tk.LEFT, padx=5)

        # Cancel button
        cancel_btn = tk.Button(btn_frame,
                              text="❌ Cancel",
                              command=self._cancel,
                              bg=self.colors['accent_red'],
                              fg=self.colors['bg_dark'],
                              font=("Arial", 12, "bold"),
                              relief=tk.FLAT,
                              cursor="hand2",
                              padx=20,
                              pady=10)
        cancel_btn.pack(side=tk.RIGHT, padx=5)

    def _create_label(self, parent, text, row):
        """Create a label in the grid"""
        label = ttk.Label(parent, text=text, style="Label.TLabel")
        label.grid(row=row, column=0, padx=10, pady=5, sticky=tk.W)

    def _create_info(self, parent, text, row):
        """Create an info label"""
        label = ttk.Label(parent, text=f"ℹ️ {text}", style="Info.TLabel")
        label.grid(row=row, column=1, padx=10, pady=2, sticky=tk.W)

    def _list_ollama_models(self):
        """Show available Ollama models"""
        try:
            result = subprocess.run(['ollama', 'list'],
                                  capture_output=True,
                                  text=True,
                                  timeout=5)
            if result.returncode == 0:
                messagebox.showinfo("Available Models", result.stdout)
            else:
                messagebox.showerror("Error", "Failed to list models")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to list models:\n{str(e)}")

    def _save_settings(self):
        """Save current settings"""
        # Update settings from UI
        self.settings.audio.whisper_model = self.whisper_var.get()
        self.settings.audio.silence_threshold = self.sensitivity_var.get()
        self.settings.audio.chunk_duration = self.chunk_dur_var.get()
        self.settings.audio.silence_duration = self.silence_dur_var.get()
        self.settings.audio.context_duration = self.context_dur_var.get()

        self.settings.display.width = self.width_var.get()
        self.settings.display.height = self.height_var.get()
        self.settings.display.transparency = self.transparency_var.get()
        self.settings.display.position = self.position_var.get()
        self.settings.display.font_size = self.fontsize_var.get()
        self.settings.display.always_on_top = self.ontop_var.get()
        self.settings.display.show_confidence = self.confidence_var.get()
        self.settings.display.show_sources = self.sources_var.get()

        self.settings.document.chunk_size = self.chunk_size_var.get()
        self.settings.document.chunk_overlap = self.chunk_overlap_var.get()
        self.settings.document.auto_process = self.auto_process_var.get()

        self.settings.llm.ollama_llm_model = self.llm_model_var.get()
        self.settings.llm.ollama_embed_model = self.embed_model_var.get()
        self.settings.llm.temperature = self.temperature_var.get()
        self.settings.llm.max_tokens = self.max_tokens_var.get()
        self.settings.llm.n_results = self.n_results_var.get()
        self.settings.llm.ollama_host = self.ollama_host_var.get()

        # Validate
        validation = self.settings.validate()

        if validation['errors']:
            error_text = "\n".join(validation['errors'])
            messagebox.showerror("Validation Errors", f"Please fix these errors:\n\n{error_text}")
            return

        if validation['warnings']:
            warning_text = "\n".join(validation['warnings'])
            confirm = messagebox.askyesno(
                "Validation Warnings",
                f"Settings have warnings:\n\n{warning_text}\n\nSave anyway?"
            )
            if not confirm:
                return

        # Save to file
        if self.settings.save():
            messagebox.showinfo("Success", "✅ Settings saved successfully!\n\nRestart Interview Mode for changes to take effect.")
            self.result = 'saved'

            # Call callback
            if self.on_save:
                self.on_save()

            self.dialog.destroy()
        else:
            messagebox.showerror("Error", "Failed to save settings")

    def _reset_settings(self):
        """Reset settings to defaults"""
        confirm = messagebox.askyesno(
            "Reset Settings",
            "Are you sure you want to reset all settings to defaults?\n\nThis cannot be undone."
        )

        if confirm:
            self.settings.reset_to_defaults()

            # Update UI
            self.whisper_var.set(self.settings.audio.whisper_model)
            self.sensitivity_var.set(self.settings.audio.silence_threshold)
            self.chunk_dur_var.set(self.settings.audio.chunk_duration)
            self.silence_dur_var.set(self.settings.audio.silence_duration)
            self.context_dur_var.set(self.settings.audio.context_duration)

            self.width_var.set(self.settings.display.width)
            self.height_var.set(self.settings.display.height)
            self.transparency_var.set(self.settings.display.transparency)
            self.position_var.set(self.settings.display.position)
            self.fontsize_var.set(self.settings.display.font_size)
            self.ontop_var.set(self.settings.display.always_on_top)
            self.confidence_var.set(self.settings.display.show_confidence)
            self.sources_var.set(self.settings.display.show_sources)

            self.chunk_size_var.set(self.settings.document.chunk_size)
            self.chunk_overlap_var.set(self.settings.document.chunk_overlap)
            self.auto_process_var.set(self.settings.document.auto_process)

            self.llm_model_var.set(self.settings.llm.ollama_llm_model)
            self.embed_model_var.set(self.settings.llm.ollama_embed_model)
            self.temperature_var.set(self.settings.llm.temperature)
            self.max_tokens_var.set(self.settings.llm.max_tokens)
            self.n_results_var.set(self.settings.llm.n_results)
            self.ollama_host_var.set(self.settings.llm.ollama_host)

            messagebox.showinfo("Reset", "Settings have been reset to defaults.\n\nClick 'Save' to apply.")

    def _cancel(self):
        """Cancel and close dialog"""
        self.result = 'cancelled'
        self.dialog.destroy()

    def _center_dialog(self):
        """Center dialog on parent window"""
        self.dialog.update_idletasks()

        parent_x = self.parent.winfo_x()
        parent_y = self.parent.winfo_y()
        parent_width = self.parent.winfo_width()
        parent_height = self.parent.winfo_height()

        dialog_width = self.dialog.winfo_width()
        dialog_height = self.dialog.winfo_height()

        x = parent_x + (parent_width - dialog_width) // 2
        y = parent_y + (parent_height - dialog_height) // 2

        self.dialog.geometry(f"+{x}+{y}")


if __name__ == "__main__":
    # Test settings dialog
    root = tk.Tk()
    root.withdraw()

    settings = SettingsManager()
    dialog = SettingsDialog(root, settings)

    root.mainloop()
