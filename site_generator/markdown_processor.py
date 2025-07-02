"""
Markdown processing functions for the site generator.
"""

import os
import datetime
import frontmatter
import markdown
from markdown.extensions import fenced_code, tables, toc, codehilite, nl2br, sane_lists
import pymdownx.superfences
import pymdownx.tabbed
import pymdownx.tasklist
import pymdownx.emoji
import pymdownx.mark
import pymdownx.highlight

from site_generator.config import DEFAULT_AUTHOR, SOURCES_DIR, PAGES_DIR, POSTS_DIR
from site_generator.utils import slugify, format_date, extract_excerpt

def convert_markdown_to_html(content):
    """Convert GitHub Flavored Markdown to HTML."""
    # Configure extensions for GitHub Flavored Markdown
    extensions = [
        'markdown.extensions.fenced_code',
        'markdown.extensions.tables',
        'markdown.extensions.toc',
        'markdown.extensions.codehilite',
        'markdown.extensions.nl2br',
        'markdown.extensions.sane_lists',
        'pymdownx.superfences',
        'pymdownx.tabbed',
        'pymdownx.tasklist',
        'pymdownx.emoji',
        'pymdownx.mark',
        'pymdownx.highlight'
    ]
    
    # Configure extension settings
    extension_configs = {
        'markdown.extensions.codehilite': {
            'linenums': False,
            'css_class': 'highlight'
        },
        'pymdownx.tasklist': {
            'custom_checkbox': True
        },
        'pymdownx.emoji': {
            'emoji_index': pymdownx.emoji.twemoji,
            'emoji_generator': pymdownx.emoji.to_alt
        }
    }
    
    # Convert Markdown to HTML
    md = markdown.Markdown(extensions=extensions, extension_configs=extension_configs)
    html_content = md.convert(content)
    
    return html_content

def process_markdown_file(file_path):
    """Process a single Markdown file and extract its metadata and content."""
    try:
        # Read frontmatter and content
        post = frontmatter.load(file_path)
        
        # Extract metadata
        title = post.get('title', os.path.basename(file_path).replace('.md', '').replace('-', ' ').title())
        date_str = post.get('date', datetime.datetime.now().strftime('%Y-%m-%d'))
        
        # Parse date
        if isinstance(date_str, datetime.datetime) or isinstance(date_str, datetime.date):
            # If it's already a datetime object
            date_obj = date_str if isinstance(date_str, datetime.datetime) else datetime.datetime.combine(date_str, datetime.time())
            date = format_date(date_obj)
        else:
            # If it's a string
            try:
                date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
                date = format_date(date_obj)
            except ValueError:
                try:
                    date_obj = datetime.datetime.strptime(date_str, '%B %d, %Y')
                    date = format_date(date_obj)
                except ValueError:
                    date_obj = datetime.datetime.now()
                    date = format_date(date_obj)
        
        # Get other metadata
        author = post.get('author', DEFAULT_AUTHOR)
        category = post.get('category', 'Uncategorized')
        tags = post.get('tags', [])
        if isinstance(tags, str):
            tags = [tag.strip() for tag in tags.split(',')]
        
        # Check if post is a draft
        is_draft = post.get('draft', False)
        
        # Convert content to HTML
        content_html = convert_markdown_to_html(post.content)
        
        # Generate slug
        slug = post.get('slug', slugify(title))
        
        # Extract excerpt
        excerpt = post.get('excerpt', extract_excerpt(post.content))
        
        # Create post object
        post_data = {
            'title': title,
            'date': date,
            'date_obj': date_obj,
            'author': author,
            'category': category,
            'tags': tags,
            'content': content_html,
            'excerpt': excerpt,
            'slug': slug,
            'url': f"posts/{slug}.html",
            'is_draft': is_draft
        }
        
        return post_data
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def process_page_file(file_path):
    """Process a single page Markdown file and extract its metadata and content."""
    try:
        # Read frontmatter and content
        page = frontmatter.load(file_path)
        
        # Extract metadata
        title = page.get('title', os.path.basename(file_path).replace('.md', '').replace('-', ' ').title())
        layout = page.get('layout', 'page')
        
        # Convert content to HTML
        content_html = convert_markdown_to_html(page.content)
        
        # Generate slug - use filename (without extension) as default
        filename = os.path.basename(file_path)
        filename_without_ext = os.path.splitext(filename)[0]
        slug = page.get('slug', filename_without_ext)
        
        # Create page object
        page_data = {
            'title': title,
            'layout': layout,
            'content': content_html,
            'slug': slug,
            'url': f"{slug}.html"
        }
        
        return page_data
    except Exception as e:
        print(f"Error processing page {file_path}: {e}")
        return None

def process_markdown_files():
    """Process all Markdown files in the sources directory."""
    all_posts = []
    draft_posts = []
    
    print(f"Looking for markdown files in: {os.path.abspath(SOURCES_DIR)}")
    
    # Check if directory exists
    if not os.path.exists(SOURCES_DIR):
        print(f"Error: Sources directory {SOURCES_DIR} does not exist!")
        return all_posts, draft_posts
    
    # Get all Markdown files
    md_files = [f for f in os.listdir(SOURCES_DIR) if f.endswith(".md")]
    print(f"Found {len(md_files)} markdown files: {md_files}")
    
    # Process each file
    for md_file in md_files:
        file_path = os.path.join(SOURCES_DIR, md_file)
        print(f"Processing file: {file_path}")
        post = process_markdown_file(file_path)
        if post:
            all_posts.append(post)
            if post['is_draft']:
                draft_posts.append(post)
                print(f"Successfully processed DRAFT post: {post['title']}")
            else:
                print(f"Successfully processed post: {post['title']}")
        else:
            print(f"Failed to process post: {file_path}")
    
    # Separate published posts from drafts
    published_posts = [post for post in all_posts if not post['is_draft']]
    
    print(f"Total posts processed: {len(all_posts)}")
    print(f"Published posts: {len(published_posts)}")
    print(f"Draft posts: {len(draft_posts)}")
    
    if draft_posts:
        print("Draft posts (hidden from public listings):")
        for draft in draft_posts:
            print(f"  - {draft['title']} (accessible at posts/{draft['slug']}.html)")
    
    # Sort posts by date (newest first)
    published_posts.sort(key=lambda x: x['date_obj'], reverse=True)
    all_posts.sort(key=lambda x: x['date_obj'], reverse=True)
    
    return published_posts, all_posts

def process_page_files():
    """Process all Markdown files in the pages directory."""
    pages = []
    
    # Get all Markdown files
    md_files = [f for f in os.listdir(PAGES_DIR) if f.endswith(".md")]
    
    # Process each file
    for md_file in md_files:
        file_path = os.path.join(PAGES_DIR, md_file)
        page = process_page_file(file_path)
        if page:
            pages.append(page)
    
    return pages
