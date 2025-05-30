"""
Configuration settings for the site generator.
"""

import os

# Directory paths
SOURCES_DIR = "sources"
POSTS_DIR = "posts"
PAGES_DIR = "pages"
TEMPLATES_DIR = "templates"

# Output files
POSTS_LIST_FILE = "posts.html"
INDEX_FILE = "index.html"

# Site information
SITE_TITLE = "Baiju Muthukadan"
SITE_DESCRIPTION = "Personal Blog"
DEFAULT_AUTHOR = "Baiju Muthukadan"

# Ensure directories exist
os.makedirs(SOURCES_DIR, exist_ok=True)
os.makedirs(POSTS_DIR, exist_ok=True)
os.makedirs(PAGES_DIR, exist_ok=True)
os.makedirs(TEMPLATES_DIR, exist_ok=True)
