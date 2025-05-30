"""
Template handling functions for the site generator.
"""

import os
import datetime
import math
from jinja2 import Environment, FileSystemLoader

from site_generator.config import (
    BASE_DIR, TEMPLATES_DIR, POSTS_DIR, POSTS_LIST_FILE, INDEX_FILE,
    SITE_TITLE, SITE_DESCRIPTION
)

def generate_html_files(posts, pages):
    """Generate HTML files for posts, pages, and index."""
    if not posts and not pages:
        print("No content to generate.")
        return
    
    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    
    # Define posts per page for pagination
    POSTS_PER_PAGE = 5
    
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
        
        # Calculate total pages for pagination
        total_posts = len(posts)
        total_pages = math.ceil(total_posts / POSTS_PER_PAGE)
        
        # Generate main posts list page (page 1)
        first_page_posts = posts[:POSTS_PER_PAGE]
        html = posts_list_template.render(
            posts=first_page_posts,
            categories=all_categories,
            all_tags=all_tags,
            site_title=SITE_TITLE,
            site_description=SITE_DESCRIPTION,
            current_page=1,
            total_pages=total_pages,
            current_year=datetime.datetime.now().year,
            page_url="posts.html"
        )
        
        # Write the main posts list file
        with open(POSTS_LIST_FILE, "w") as f:
            f.write(html)
        
        print(f"Generated {POSTS_LIST_FILE}")
        
        # Generate additional pages if needed
        if total_pages > 1:
            # Create posts directory if it doesn't exist
            os.makedirs("pages", exist_ok=True)
            
            # Generate pages 2 to total_pages
            for page_num in range(2, total_pages + 1):
                start_idx = (page_num - 1) * POSTS_PER_PAGE
                end_idx = min(start_idx + POSTS_PER_PAGE, total_posts)
                page_posts = posts[start_idx:end_idx]
                
                page_html = posts_list_template.render(
                    posts=page_posts,
                    categories=all_categories,
                    all_tags=all_tags,
                    site_title=SITE_TITLE,
                    site_description=SITE_DESCRIPTION,
                    current_page=page_num,
                    total_pages=total_pages,
                    current_year=datetime.datetime.now().year,
                    page_url=f"posts-page-{page_num}.html"
                )
                
                # Write the paginated posts list file
                page_file = os.path.join(BASE_DIR, f"posts-page-{page_num}.html")
                with open(page_file, "w") as f:
                    f.write(page_html)
                
                print(f"Generated {page_file}")
    
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
