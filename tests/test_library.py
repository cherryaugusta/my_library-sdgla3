"""
test_library.py

Unit tests for my_library package.
"""

from my_library.file_helpers import write_text, read_text
from my_library.data_analyzers import average, word_count


def test_file_helpers(tmp_path):
    """
    Test file reading and writing.
    """
    file_path = tmp_path / "sample.txt"

    write_text(file_path, "Hello World")
    content = read_text(file_path)

    assert content == "Hello World"


def test_average():
    """
    Test average calculation.
    """
    assert average([2, 4, 6]) == 4.0


def test_word_count():
    """
    Test word counting.
    """
    assert word_count("Hello world from Python") == 4
