#!/usr/bin/env python3
"""
Generate HTML files from GitHub Flavored Markdown sources.
This script reads markdown files from the 'sources' directory,
converts them to HTML, and saves them in the 'posts' directory.
It also processes static pages from the 'pages' directory.
"""

import sys
from site_generator.config import SOURCES_DIR, PAGES_DIR
from site_generator.markdown_processor import process_markdown_files, process_page_files
from site_generator.template_handler import generate_html_files

def main():
    """Main function to run the site generator."""
    print("Starting site generation...")
    
    # Process markdown files for posts
    published_posts, all_posts = process_markdown_files()
    
    # Process markdown files for pages
    pages = process_page_files()
    
    # Generate HTML files (use all_posts to generate HTML for drafts too, but published_posts for listings)
    generate_html_files(published_posts, all_posts, pages)
    
    print("Site generation complete!")

if __name__ == "__main__":
    main()
