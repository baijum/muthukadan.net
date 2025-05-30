"""
Utility functions for the site generator.
"""

import re
import datetime

def slugify(text):
    """Convert text to slug format."""
    # Convert to lowercase
    text = text.lower()
    # Replace spaces with hyphens
    text = re.sub(r'\s+', '-', text)
    # Remove special characters
    text = re.sub(r'[^\w\-]', '', text)
    # Remove duplicate hyphens
    text = re.sub(r'\-+', '-', text)
    # Remove leading and trailing hyphens
    text = text.strip('-')
    return text

def format_date(date_obj):
    """Format date as Month DD, YYYY."""
    return date_obj.strftime('%B %d, %Y')

def extract_excerpt(content, max_length=150):
    """Extract a short excerpt from the content."""
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', content)
    # Remove Markdown formatting
    text = re.sub(r'[#*_~`]', '', text)
    # Truncate to max_length
    if len(text) > max_length:
        text = text[:max_length].rsplit(' ', 1)[0] + '...'
    return text
