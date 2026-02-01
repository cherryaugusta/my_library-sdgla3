"""
file_helpers.py

Utility functions for reading and writing text files.
"""

from pathlib import Path
from typing import Union


def read_text(path: Union[str, Path]) -> str:
    """
    Read and return the contents of a text file.

    Args:
        path (str | Path): Path to the text file.

    Returns:
        str: Contents of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If the file cannot be read.
    """
    # Convert input to Path object for consistency
    file_path = Path(path)

    # Read text using UTF-8 encoding
    return file_path.read_text(encoding="utf-8")


def write_text(path: Union[str, Path], content: str) -> None:
    """
    Write text content to a file.

    Args:
        path (str | Path): Path where the file will be written.
        content (str): Text content to write.

    Raises:
        IOError: If the file cannot be written.
    """
    file_path = Path(path)

    # Write text using UTF-8 encoding
    file_path.write_text(content, encoding="utf-8")
