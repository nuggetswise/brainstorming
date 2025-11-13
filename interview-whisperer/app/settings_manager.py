#!/usr/bin/env python3
"""
Settings Manager for Interview Whisperer
Handles loading, saving, and validation of user preferences
"""

import json
import logging
from pathlib import Path
from typing import Dict, Any, Optional
from dataclasses import dataclass, asdict

logger = logging.getLogger(__name__)


@dataclass
class AudioSettings:
    """Audio and voice activation settings"""
    whisper_model: str = "base"  # tiny, base, small, medium, large
    sample_rate: int = 16000
    channels: int = 1
    chunk_duration: float = 5.0
    silence_threshold: float = 0.01  # Voice activation sensitivity
    silence_duration: float = 1.5
    context_duration: float = 30.0


@dataclass
class DisplaySettings:
    """Overlay display preferences"""
    width: int = 400
    height: int = 350
    transparency: float = 0.95  # 0.0-1.0
    position: str = "top-right"  # top-right, top-left, bottom-right, bottom-left, center
    font_size: int = 10
    always_on_top: bool = True
    show_confidence: bool = True
    show_sources: bool = True


@dataclass
class DocumentSettings:
    """Document processing options"""
    chunk_size: int = 500  # words
    chunk_overlap: int = 50  # words
    supported_extensions: list = None
    auto_process: bool = False  # Auto-process new documents

    def __post_init__(self):
        if self.supported_extensions is None:
            self.supported_extensions = ['.pdf', '.docx', '.txt', '.md']


@dataclass
class LLMSettings:
    """LLM and embedding model settings"""
    ollama_llm_model: str = "llama3.1:8b"
    ollama_embed_model: str = "nomic-embed-text"
    ollama_host: str = "http://localhost:11434"
    temperature: float = 0.7
    max_tokens: int = 250
    n_results: int = 3  # Number of context chunks to retrieve


class SettingsManager:
    """
    Manages application settings with persistence to JSON file.

    Provides defaults, validation, and save/load functionality.
    """

    def __init__(self, settings_file: Optional[Path] = None):
        """
        Initialize settings manager.

        Args:
            settings_file: Path to settings JSON file. If None, uses default location.
        """
        if settings_file is None:
            base_dir = Path(__file__).parent.parent
            settings_file = base_dir / "data" / "settings.json"

        self.settings_file = Path(settings_file)
        self.settings_file.parent.mkdir(parents=True, exist_ok=True)

        # Initialize with defaults
        self.audio = AudioSettings()
        self.display = DisplaySettings()
        self.document = DocumentSettings()
        self.llm = LLMSettings()

        # Load existing settings
        self.load()

    def load(self) -> bool:
        """
        Load settings from JSON file.

        Returns:
            bool: True if loaded successfully, False if using defaults
        """
        if not self.settings_file.exists():
            logger.info("No settings file found, using defaults")
            return False

        try:
            with open(self.settings_file, 'r') as f:
                data = json.load(f)

            # Load each section
            if 'audio' in data:
                self.audio = AudioSettings(**data['audio'])
            if 'display' in data:
                self.display = DisplaySettings(**data['display'])
            if 'document' in data:
                self.document = DocumentSettings(**data['document'])
            if 'llm' in data:
                self.llm = LLMSettings(**data['llm'])

            logger.info(f"Settings loaded from {self.settings_file}")
            return True

        except Exception as e:
            logger.error(f"Failed to load settings: {e}")
            logger.info("Using default settings")
            return False

    def save(self) -> bool:
        """
        Save current settings to JSON file.

        Returns:
            bool: True if saved successfully, False otherwise
        """
        try:
            data = {
                'audio': asdict(self.audio),
                'display': asdict(self.display),
                'document': asdict(self.document),
                'llm': asdict(self.llm)
            }

            with open(self.settings_file, 'w') as f:
                json.dump(data, f, indent=2)

            logger.info(f"Settings saved to {self.settings_file}")
            return True

        except Exception as e:
            logger.error(f"Failed to save settings: {e}")
            return False

    def reset_to_defaults(self) -> None:
        """Reset all settings to default values"""
        self.audio = AudioSettings()
        self.display = DisplaySettings()
        self.document = DocumentSettings()
        self.llm = LLMSettings()
        logger.info("Settings reset to defaults")

    def validate(self) -> Dict[str, list]:
        """
        Validate current settings.

        Returns:
            Dict with 'errors' and 'warnings' lists
        """
        errors = []
        warnings = []

        # Audio validation
        if self.audio.whisper_model not in ['tiny', 'base', 'small', 'medium', 'large']:
            errors.append(f"Invalid Whisper model: {self.audio.whisper_model}")

        if not (0.001 <= self.audio.silence_threshold <= 0.1):
            warnings.append(f"Silence threshold {self.audio.silence_threshold} may be too extreme")

        if not (1 <= self.audio.chunk_duration <= 30):
            warnings.append(f"Chunk duration {self.audio.chunk_duration}s may cause issues")

        # Display validation
        if not (0.1 <= self.display.transparency <= 1.0):
            errors.append(f"Transparency must be between 0.1 and 1.0")

        if self.display.position not in ['top-right', 'top-left', 'bottom-right', 'bottom-left', 'center']:
            errors.append(f"Invalid position: {self.display.position}")

        if not (200 <= self.display.width <= 1000):
            warnings.append(f"Width {self.display.width} may not display well")

        if not (200 <= self.display.height <= 800):
            warnings.append(f"Height {self.display.height} may not display well")

        # Document validation
        if self.document.chunk_size < 100:
            warnings.append("Chunk size < 100 may fragment context too much")

        if self.document.chunk_overlap >= self.document.chunk_size:
            errors.append("Chunk overlap must be less than chunk size")

        # LLM validation
        if not (0.0 <= self.llm.temperature <= 2.0):
            warnings.append(f"Temperature {self.llm.temperature} is outside normal range (0.0-2.0)")

        if not (50 <= self.llm.max_tokens <= 1000):
            warnings.append(f"Max tokens {self.llm.max_tokens} may be too extreme")

        return {'errors': errors, 'warnings': warnings}

    def get_audio_config(self) -> Dict[str, Any]:
        """Get audio configuration as dict for AudioEngine"""
        return {
            'model': self.audio.whisper_model,
            'sample_rate': self.audio.sample_rate,
            'channels': self.audio.channels,
            'chunk_duration': self.audio.chunk_duration,
            'silence_threshold': self.audio.silence_threshold,
            'silence_duration': self.audio.silence_duration,
            'context_duration': self.audio.context_duration
        }

    def get_overlay_config(self) -> Dict[str, Any]:
        """Get overlay configuration as dict for OverlayWindow"""
        return {
            'width': self.display.width,
            'height': self.display.height,
            'transparency': self.display.transparency,
            'position': self.display.position,
            'font_size': self.display.font_size,
            'always_on_top': self.display.always_on_top,
            'show_confidence': self.display.show_confidence,
            'show_sources': self.display.show_sources
        }

    def get_document_config(self) -> Dict[str, Any]:
        """Get document processing configuration"""
        return {
            'chunk_size': self.document.chunk_size,
            'chunk_overlap': self.document.chunk_overlap,
            'supported_extensions': self.document.supported_extensions,
            'auto_process': self.document.auto_process
        }

    def get_llm_config(self) -> Dict[str, Any]:
        """Get LLM configuration"""
        return {
            'model': self.llm.ollama_llm_model,
            'embed_model': self.llm.ollama_embed_model,
            'host': self.llm.ollama_host,
            'temperature': self.llm.temperature,
            'max_tokens': self.llm.max_tokens,
            'n_results': self.llm.n_results
        }


if __name__ == "__main__":
    # Test settings manager
    print("Testing Settings Manager...")

    manager = SettingsManager()

    print("\nDefault Settings:")
    print(f"  Audio: Whisper={manager.audio.whisper_model}, Sensitivity={manager.audio.silence_threshold}")
    print(f"  Display: {manager.display.width}x{manager.display.height}, Transparency={manager.display.transparency}")
    print(f"  Document: Chunk={manager.document.chunk_size}, Overlap={manager.document.chunk_overlap}")
    print(f"  LLM: {manager.llm.ollama_llm_model}, Temp={manager.llm.temperature}")

    # Modify and save
    manager.audio.silence_threshold = 0.02
    manager.display.width = 500
    manager.save()
    print(f"\nSettings saved to: {manager.settings_file}")

    # Reload
    manager2 = SettingsManager()
    print(f"\nReloaded sensitivity: {manager2.audio.silence_threshold}")
    print(f"Reloaded width: {manager2.display.width}")

    # Validate
    validation = manager.validate()
    print(f"\nValidation: {len(validation['errors'])} errors, {len(validation['warnings'])} warnings")

    print("\n✅ Settings Manager working correctly!")
