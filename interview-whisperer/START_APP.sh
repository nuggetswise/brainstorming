#!/bin/bash

# Interview Whisperer - One-Click Launcher
# Starts the Interview Whisperer application with all prerequisites

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}  🎯 Interview Whisperer - Starting Application${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
echo ""

# =============================================================================
# 1. Check Python
# =============================================================================

echo -e "${YELLOW}[1/5]${NC} Checking Python..."

if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 not found${NC}"
    echo -e "   Please install Python 3.10 or higher"
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo -e "${GREEN}✓${NC} Python ${PYTHON_VERSION} found"

# =============================================================================
# 2. Check Virtual Environment
# =============================================================================

echo -e "${YELLOW}[2/5]${NC} Checking virtual environment..."

if [ ! -d "venv" ]; then
    echo -e "${YELLOW}⚠️  Virtual environment not found. Creating...${NC}"
    python3 -m venv venv
    echo -e "${GREEN}✓${NC} Virtual environment created"
fi

# Activate virtual environment
source venv/bin/activate
echo -e "${GREEN}✓${NC} Virtual environment activated"

# =============================================================================
# 3. Check Dependencies
# =============================================================================

echo -e "${YELLOW}[3/5]${NC} Checking Python dependencies..."

if [ -f "requirements.txt" ]; then
    # Check if dependencies are installed (basic check)
    if ! python3 -c "import whisper, ollama, chromadb" &> /dev/null; then
        echo -e "${YELLOW}⚠️  Installing dependencies (this may take a few minutes)...${NC}"
        pip install --upgrade pip > /dev/null 2>&1
        pip install -r requirements.txt
        echo -e "${GREEN}✓${NC} Dependencies installed"
    else
        echo -e "${GREEN}✓${NC} Dependencies already installed"
    fi
else
    echo -e "${YELLOW}⚠️  requirements.txt not found, skipping dependency check${NC}"
fi

# =============================================================================
# 4. Check Ollama
# =============================================================================

echo -e "${YELLOW}[4/5]${NC} Checking Ollama..."

if ! command -v ollama &> /dev/null; then
    echo -e "${YELLOW}⚠️  Ollama not found${NC}"
    echo -e "   Install from: ${BLUE}https://ollama.ai${NC}"
    echo -e "   Continuing anyway (some features may not work)..."
else
    echo -e "${GREEN}✓${NC} Ollama is installed"

    # Check if Ollama is running
    if ! curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
        echo -e "${YELLOW}⚠️  Ollama is not running. Starting...${NC}"

        # Try to start Ollama in background
        if command -v ollama &> /dev/null; then
            ollama serve > /dev/null 2>&1 &
            OLLAMA_PID=$!

            # Wait for Ollama to start (max 10 seconds)
            for i in {1..10}; do
                if curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
                    echo -e "${GREEN}✓${NC} Ollama started successfully"
                    break
                fi
                sleep 1
            done

            if ! curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
                echo -e "${YELLOW}⚠️  Ollama may not be ready yet${NC}"
            fi
        fi
    else
        echo -e "${GREEN}✓${NC} Ollama is running"
    fi
fi

# =============================================================================
# 5. Check Documents Directory
# =============================================================================

echo -e "${YELLOW}[5/5]${NC} Checking documents directory..."

if [ ! -d "documents" ]; then
    mkdir -p documents
    echo -e "${GREEN}✓${NC} Documents directory created"
else
    DOC_COUNT=$(find documents -type f \( -name "*.pdf" -o -name "*.txt" -o -name "*.docx" -o -name "*.md" \) 2>/dev/null | wc -l)
    echo -e "${GREEN}✓${NC} Documents directory exists (${DOC_COUNT} files)"
fi

# Create data directory if needed
mkdir -p data/chroma_db data/logs

echo ""
echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}✅ All checks complete!${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
echo ""

# =============================================================================
# Launch Application
# =============================================================================

echo -e "${BLUE}🚀 Launching Interview Whisperer...${NC}"
echo ""

# Set PYTHONPATH to include app directory
export PYTHONPATH="${SCRIPT_DIR}/app:${PYTHONPATH}"

# Launch the application
cd app
python3 launcher.py

# =============================================================================
# Cleanup
# =============================================================================

echo ""
echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}  👋 Thanks for using Interview Whisperer!${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
echo ""

# Stop Ollama if we started it
if [ ! -z "$OLLAMA_PID" ]; then
    echo -e "${YELLOW}Stopping Ollama (PID: $OLLAMA_PID)...${NC}"
    kill $OLLAMA_PID 2>/dev/null || true
fi

exit 0
