"""
Configuration settings for the site generator.
"""

import os

# Base directory (project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Directory paths
SOURCES_DIR = os.path.join(BASE_DIR, "sources")
POSTS_DIR = os.path.join(BASE_DIR, "posts")
PAGES_DIR = os.path.join(BASE_DIR, "pages")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# Output files
POSTS_LIST_FILE = os.path.join(BASE_DIR, "posts.html")
INDEX_FILE = os.path.join(BASE_DIR, "index.html")

# Site information
SITE_TITLE = "Baiju Muthukadan"
SITE_DESCRIPTION = "Personal Blog"
DEFAULT_AUTHOR = "Baiju Muthukadan"

# Ensure directories exist
os.makedirs(SOURCES_DIR, exist_ok=True)
os.makedirs(POSTS_DIR, exist_ok=True)
os.makedirs(PAGES_DIR, exist_ok=True)
os.makedirs(TEMPLATES_DIR, exist_ok=True)
