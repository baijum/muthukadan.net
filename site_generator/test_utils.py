"""
Unit tests for the utils module.
"""

import datetime
import pytest
from site_generator.utils import slugify, format_date, extract_excerpt

def test_slugify():
    """Test the slugify function."""
    # Test basic slugification
    assert slugify("Hello World") == "hello-world"
    
    # Test with special characters
    assert slugify("Hello, World!") == "hello-world"
    
    # Test with multiple spaces
    assert slugify("Hello  World") == "hello-world"
    
    # Test with uppercase
    assert slugify("HELLO WORLD") == "hello-world"
    
    # Test with numbers
    assert slugify("Hello World 123") == "hello-world-123"
    
    # Test with leading/trailing spaces
    assert slugify(" Hello World ") == "hello-world"

def test_format_date():
    """Test the format_date function."""
    # Test with a specific date
    date = datetime.datetime(2025, 5, 30)
    assert format_date(date) == "May 30, 2025"
    
    # Test with another date
    date = datetime.datetime(2024, 12, 25)
    assert format_date(date) == "December 25, 2024"

def test_extract_excerpt():
    """Test the extract_excerpt function."""
    # Test with short content
    content = "This is a short excerpt."
    assert extract_excerpt(content) == "This is a short excerpt."
    
    # Test with long content
    long_content = "This is a very long excerpt that should be truncated. " * 10
    excerpt = extract_excerpt(long_content, max_length=50)
    assert len(excerpt) <= 53  # 50 + "..."
    assert excerpt.endswith("...")
    
    # Test with HTML content
    html_content = "<p>This is <strong>formatted</strong> content.</p>"
    assert extract_excerpt(html_content) == "This is formatted content."
    
    # Test with Markdown content
    md_content = "# Heading\n\nThis is **bold** text."
    assert extract_excerpt(md_content) == " Heading\n\nThis is bold text."
