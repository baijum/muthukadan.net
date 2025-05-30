#!/usr/bin/env python3
"""
Command-line interface for the site generator.
"""

import sys
from site_generator.markdown_processor import process_markdown_files, process_page_files
from site_generator.template_handler import generate_html_files


def main():
    """Main function to run the site generator."""
    print("Starting site generation...")
    
    # Process markdown files for posts
    posts = process_markdown_files()
    
    # Process markdown files for pages
    pages = process_page_files()
    
    # Generate HTML files
    generate_html_files(posts, pages)
    
    print("Site generation complete!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
