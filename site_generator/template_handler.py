"""
Template handling functions for the site generator.
"""

import os
import datetime
from jinja2 import Environment, FileSystemLoader

from site_generator.config import (
    TEMPLATES_DIR, POSTS_DIR, POSTS_LIST_FILE, INDEX_FILE,
    SITE_TITLE, SITE_DESCRIPTION
)

def generate_html_files(posts, pages):
    """Generate HTML files for posts, pages, and index."""
    if not posts and not pages:
        print("No content to generate.")
        return
    
    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    
    # Generate HTML for each post
    if posts:
        post_template = env.get_template('post.html')
        posts_list_template = env.get_template('posts_list.html')
        
        # Extract all categories and tags
        all_categories = sorted(set(post['category'] for post in posts))
        all_tags = sorted(set(tag for post in posts for tag in post['tags']))
        
        for i, post in enumerate(posts):
            # Determine previous and next posts
            prev_post = posts[i+1] if i < len(posts)-1 else None
            next_post = posts[i-1] if i > 0 else None
            
            # Render the post template
            html = post_template.render(
                title=post['title'],
                date=post['date'],
                category=post['category'],
                content=post['content'],
                prev_post=prev_post,
                next_post=next_post,
                site_title=SITE_TITLE,
                site_description=SITE_DESCRIPTION,
                categories=all_categories,
                recent_posts=posts[:5],  # Show 5 most recent posts
                current_year=datetime.datetime.now().year,
                page_url=f"{post['slug']}.html"
            )
            
            # Write the HTML file
            output_path = os.path.join(POSTS_DIR, f"{post['slug']}.html")
            with open(output_path, "w") as f:
                f.write(html)
            
            print(f"Generated {output_path}")
        
        # Generate posts list page
        html = posts_list_template.render(
            posts=posts,
            categories=all_categories,
            all_tags=all_tags,
            site_title=SITE_TITLE,
            site_description=SITE_DESCRIPTION,
            current_page=1,
            total_pages=1,
            current_year=datetime.datetime.now().year,
            page_url="posts.html"
        )
        
        # Write the posts list file
        with open(POSTS_LIST_FILE, "w") as f:
            f.write(html)
        
        print(f"Generated {POSTS_LIST_FILE}")
    
    # Generate HTML for each page
    if pages:
        page_template = env.get_template('page.html')
        
        for page in pages:
            # Render the page template
            html = page_template.render(
                page_title=page['title'],
                content=page['content'],
                site_title=SITE_TITLE,
                site_description=SITE_DESCRIPTION,
                current_year=datetime.datetime.now().year,
                page_url=f"{page['slug']}.html"
            )
            
            # Write the HTML file
            output_path = f"{page['slug']}.html"
            with open(output_path, "w") as f:
                f.write(html)
            
            print(f"Generated {output_path}")
    
    # Generate index.html
    if posts:
        index_template = env.get_template('index.html')
        
        # Extract all categories
        all_categories = sorted(set(post['category'] for post in posts))
        
        # Render the index template
        html = index_template.render(
            latest_posts=posts[:3],  # Show 3 most recent posts
            categories=all_categories,
            site_title=SITE_TITLE,
            site_description=SITE_DESCRIPTION,
            current_year=datetime.datetime.now().year,
            page_url="index.html"
        )
        
        # Write the index file
        with open(INDEX_FILE, "w") as f:
            f.write(html)
        
        print(f"Generated {INDEX_FILE}")
