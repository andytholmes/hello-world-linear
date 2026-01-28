#!/usr/bin/env python3
"""
Linear Hello World - Main Entry Point

AI-Native Hello World Application
Linear plans it. Cursor builds it. GitHub controls it. Python runs it.

Usage:
    python main.py --name Andy
    python main.py --name Andy --style casual
    python main.py --name Smith --style formal --title Dr.
"""

import sys
from pathlib import Path

# Add src to path for direct execution
sys.path.insert(0, str(Path(__file__).parent / "src"))

from hello_world.cli import app

if __name__ == "__main__":
    app()
