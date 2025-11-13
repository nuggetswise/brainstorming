"""
Interview Whisperer Configuration Module

Centralized configuration for all application settings including paths,
audio processing parameters, LLM models, and utility functions.
"""

import os
import logging
import requests
from pathlib import Path
from datetime import datetime


# =============================================================================
# PATHS CONFIGURATION
# =============================================================================

# Base directories
BASE_DIR = Path(__file__).parent.parent
APP_DIR = BASE_DIR / "app"
DOCUMENTS_DIR = BASE_DIR / "documents"
DATA_DIR = BASE_DIR / "data"
CHROMA_DB_DIR = DATA_DIR / "chroma_db"
LOGS_DIR = DATA_DIR / "logs"
ASSETS_DIR = BASE_DIR / "assets"

# Ensure directories exist
for dir_path in [DOCUMENTS_DIR, DATA_DIR, CHROMA_DB_DIR, LOGS_DIR, ASSETS_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)


# =============================================================================
# AUDIO SETTINGS
# =============================================================================

# Audio processing parameters
SAMPLE_RATE = 16000  # Hz
CHANNELS = 1  # Mono
CHUNK_DURATION_SECONDS = 5  # Duration per audio chunk


# =============================================================================
# WHISPER SETTINGS
# =============================================================================

# OpenAI Whisper configuration
WHISPER_MODEL = "base"  # Options: tiny, base, small, medium, large
WHISPER_LANGUAGE = "en"  # Language code for transcription


# =============================================================================
# OLLAMA SETTINGS
# =============================================================================

# Ollama LLM configuration
OLLAMA_LLM_MODEL = "llama3.1:8b"  # Main language model
OLLAMA_EMBED_MODEL = "nomic-embed-text"  # Embedding model
OLLAMA_HOST = "http://localhost:11434"  # Ollama server address


# =============================================================================
# CHROMADB SETTINGS
# =============================================================================

# Vector database configuration
CHROMA_COLLECTION_NAME = "interview_context"


# =============================================================================
# DOCUMENT PROCESSING SETTINGS
# =============================================================================

# Text chunking parameters
CHUNK_SIZE = 500  # Size in words
CHUNK_OVERLAP = 50  # Overlap in words

# Supported document formats
SUPPORTED_EXTENSIONS = ['.pdf', '.docx', '.txt', '.md']


# =============================================================================
# UI SETTINGS
# =============================================================================

# Main window dimensions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500

# Overlay/secondary window dimensions
OVERLAY_WIDTH = 400
OVERLAY_HEIGHT = 300


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def setup_logging():
    """
    Configure logging for the application.

    Sets up both file and console logging with timestamps and log levels.
    Logs are stored in DATA_DIR/logs/ with daily rotation.

    Returns:
        logging.Logger: Configured logger instance
    """
    log_file = LOGS_DIR / f"interview_whisperer_{datetime.now().strftime('%Y%m%d')}.log"

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger('InterviewWhisperer')


def check_ollama_running():
    """
    Check if Ollama service is running and accessible.

    Attempts to connect to the Ollama API endpoint with a 2-second timeout.

    Returns:
        bool: True if Ollama is accessible, False otherwise
    """
    try:
        response = requests.get(f"{OLLAMA_HOST}/api/tags", timeout=2)
        return response.status_code == 200
    except Exception:
        return False


def get_available_models():
    """
    Retrieve list of available models from Ollama.

    Queries the Ollama API to get all installed models.

    Returns:
        list: List of model names available in Ollama, empty list if unavailable
    """
    try:
        response = requests.get(f"{OLLAMA_HOST}/api/tags", timeout=2)
        if response.status_code == 200:
            models = response.json().get('models', [])
            return [model['name'] for model in models]
    except Exception:
        pass
    return []


# =============================================================================
# LOGGING INITIALIZATION
# =============================================================================

# Initialize logger on module import
logger = setup_logging()

# Log configuration on startup
logger.info(f"Interview Whisperer configuration loaded")
logger.info(f"Base directory: {BASE_DIR}")
logger.info(f"Whisper model: {WHISPER_MODEL}")
logger.info(f"Ollama LLM: {OLLAMA_LLM_MODEL}")
logger.info(f"Ollama embedding model: {OLLAMA_EMBED_MODEL}")
