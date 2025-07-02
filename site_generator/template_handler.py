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

def generate_html_files(published_posts, all_posts, pages):
    """Generate HTML files for posts, pages, and index."""
    if not all_posts and not pages:
        print("No content to generate.")
        return
    
    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    
    # Define posts per page for pagination
    POSTS_PER_PAGE = 5
    
    # Generate HTML for each post (including drafts)
    if all_posts:
        post_template = env.get_template('post.html')
        posts_list_template = env.get_template('posts_list.html')
        
        # Extract all categories and tags from published posts only
        all_categories = sorted(set(post['category'] for post in published_posts)) if published_posts else []
        all_tags = sorted(set(tag for post in published_posts for tag in post['tags'])) if published_posts else []
        
        # Generate HTML for all posts (including drafts)
        for i, post in enumerate(all_posts):
            # For navigation, only consider published posts
            published_post_index = None
            if not post['is_draft']:
                # Find the index of this post in the published posts list
                for j, pub_post in enumerate(published_posts):
                    if pub_post['slug'] == post['slug']:
                        published_post_index = j
                        break
            
            # Determine previous and next posts (only from published posts)
            prev_post = None
            next_post = None
            if published_post_index is not None:
                prev_post = published_posts[published_post_index + 1] if published_post_index < len(published_posts) - 1 else None
                next_post = published_posts[published_post_index - 1] if published_post_index > 0 else None
            
            # Add draft indicator to title if it's a draft
            display_title = post['title']
            if post['is_draft']:
                display_title = f"[DRAFT] {post['title']}"
            
            # Render the post template
            html = post_template.render(
                title=display_title,
                date=post['date'],
                category=post['category'],
                content=post['content'],
                prev_post=prev_post,
                next_post=next_post,
                site_title=SITE_TITLE,
                site_description=SITE_DESCRIPTION,
                categories=all_categories,
                recent_posts=published_posts[:5],  # Show 5 most recent published posts
                current_year=datetime.datetime.now().year,
                page_url=f"{post['slug']}.html",
                is_draft=post['is_draft']
            )
            
            # Write the HTML file
            output_path = os.path.join(POSTS_DIR, f"{post['slug']}.html")
            with open(output_path, "w") as f:
                f.write(html)
            
            draft_status = " (DRAFT)" if post['is_draft'] else ""
            print(f"Generated {output_path}{draft_status}")
        
        # Use only published posts for public listings
        if published_posts:
            # Calculate total pages for pagination
            total_posts = len(published_posts)
            total_pages = math.ceil(total_posts / POSTS_PER_PAGE)
            
            # Generate main posts list page (page 1)
            first_page_posts = published_posts[:POSTS_PER_PAGE]
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
                    page_posts = published_posts[start_idx:end_idx]
                    
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
    
    # Generate index.html (use only published posts)
    if published_posts:
        index_template = env.get_template('index.html')
        
        # Extract all categories from published posts
        all_categories = sorted(set(post['category'] for post in published_posts))
        
        # Render the index template
        html = index_template.render(
            latest_posts=published_posts[:3],  # Show 3 most recent published posts
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
