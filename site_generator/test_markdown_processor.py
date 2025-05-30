"""
Unit tests for the markdown_processor module.
"""

import os
import tempfile
import pytest
from unittest.mock import patch, mock_open
import frontmatter
import datetime

from site_generator.markdown_processor import (
    convert_markdown_to_html,
    process_markdown_file,
    process_page_file
)

def test_convert_markdown_to_html():
    """Test converting Markdown to HTML."""
    # Test basic Markdown
    md = "# Heading\n\nThis is a paragraph."
    html = convert_markdown_to_html(md)
    assert "<h1 id=\"heading\">Heading</h1>" in html
    assert "<p>This is a paragraph.</p>" in html
    
    # Test code blocks
    md = "```python\ndef hello():\n    print('Hello')\n```"
    html = convert_markdown_to_html(md)
    assert "<pre>" in html
    assert "hello" in html  # Just check for part of the function name
    
    # Test lists
    md = "- Item 1\n- Item 2\n- Item 3"
    html = convert_markdown_to_html(md)
    assert "<ul>" in html
    assert "<li>Item 1</li>" in html
    
    # Test links
    md = "[Link text](https://example.com)"
    html = convert_markdown_to_html(md)
    assert '<a href="https://example.com">Link text</a>' in html
    
    # Test emphasis
    md = "*Italic* and **Bold**"
    html = convert_markdown_to_html(md)
    assert "<em>Italic</em>" in html
    assert "<strong>Bold</strong>" in html
    
    # Test task lists
    md = "- [x] Completed task\n- [ ] Incomplete task"
    html = convert_markdown_to_html(md)
    assert 'input type="checkbox" disabled checked' in html
    assert 'input type="checkbox" disabled' in html
    assert 'task-list-item' in html

@patch('builtins.open', new_callable=mock_open, read_data='---\ntitle: Test Post\ndate: 2025-05-30\n---\n# Test Content')
@patch('frontmatter.load')
def test_process_markdown_file(mock_frontmatter_load, mock_file):
    """Test processing a Markdown file."""
    # Setup mock frontmatter
    mock_post = frontmatter.Post("# Test Content")
    mock_post.metadata = {
        'title': 'Test Post',
        'date': '2025-05-30',
        'category': 'Test',
        'tags': ['test', 'markdown']
    }
    mock_frontmatter_load.return_value = mock_post
    
    # Call the function
    result = process_markdown_file('/fake/path/test-post.md')
    
    # Verify the result
    assert result['title'] == 'Test Post'
    assert result['date'] == 'May 30, 2025'
    assert result['category'] == 'Test'
    assert result['tags'] == ['test', 'markdown']
    assert result['slug'] == 'test-post'
    assert result['url'] == 'posts/test-post.html'
    assert '<h1 id="test-content">Test Content</h1>' in result['content']

@patch('builtins.open', new_callable=mock_open, read_data='---\ntitle: About Page\nlayout: page\n---\n# About Me')
@patch('frontmatter.load')
def test_process_page_file(mock_frontmatter_load, mock_file):
    """Test processing a page Markdown file."""
    # Setup mock frontmatter
    mock_page = frontmatter.Post("# About Me")
    mock_page.metadata = {
        'title': 'About Page',
        'layout': 'page'
    }
    mock_frontmatter_load.return_value = mock_page
    
    # Call the function
    result = process_page_file('/fake/path/about.md')
    
    # Verify the result
    assert result['title'] == 'About Page'
    assert result['layout'] == 'page'
    assert result['slug'] == 'about'  # The slug is now generated from the filename
    assert result['url'] == 'about.html'
    assert '<h1 id="about-me">About Me</h1>' in result['content']
