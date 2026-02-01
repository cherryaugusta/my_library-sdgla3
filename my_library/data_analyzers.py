"""
data_analyzers.py

Basic data analysis utilities.
"""

from typing import List


def average(numbers: List[float]) -> float:
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (List[float]): List of numeric values.

    Returns:
        float: Average value.

    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list.")

    return sum(numbers) / len(numbers)


def word_count(text: str) -> int:
    """
    Count the number of words in a string.

    Args:
        text (str): Input text.

    Returns:
        int: Number of words.
    """
    return len(text.split())