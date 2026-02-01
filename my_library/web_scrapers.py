"""
web_scrapers.py

Simple web scraping utilities.
"""

import re
import requests


def fetch_html(url: str, timeout: int = 10) -> str:
    """
    Fetch raw HTML content from a URL.

    Args:
        url (str): Target URL.
        timeout (int): Request timeout in seconds.

    Returns:
        str: HTML content.

    Raises:
        requests.RequestException: For network-related errors.
    """
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.text


def extract_title(html: str) -> str:
    """
    Extract the <title> tag content from HTML.

    Args:
        html (str): Raw HTML string.

    Returns:
        str: Page title or empty string if not found.
    """
    match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else ""
