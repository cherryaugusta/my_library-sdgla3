"""
my_library

A personal Python utility library containing helpers for:
- File operations
- Web scraping
- Data analysis

This package is designed for educational and portfolio purposes.
"""

# Version of the package
__version__ = "1.0.0"

# Public API exports
from .file_helpers import read_text, write_text
from .web_scrapers import fetch_html, extract_title
from .data_analyzers import average, word_count