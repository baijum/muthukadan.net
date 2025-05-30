#!/usr/bin/env python3
"""
Script to generate sample blog posts for testing pagination.
"""

import os
import random
import datetime
from pathlib import Path

# Categories and tags for random selection
CATEGORIES = ["Technology", "Programming", "Web Development", "Python", "JavaScript", "Data Science"]
TAGS = ["coding", "tutorial", "beginner", "advanced", "framework", "library", "tools", 
        "best practices", "tips", "guide", "machine learning", "web", "frontend", "backend"]

# Sample post titles
POST_TITLES = [
    "Getting Started with Python: A Beginner's Guide",
    "10 JavaScript Tricks You Should Know",
    "Building Responsive Websites with CSS Grid",
    "Understanding Data Structures and Algorithms",
    "Introduction to Machine Learning with Python",
    "Web Development Best Practices for 2025",
    "How to Build a RESTful API with Flask",
    "React vs Vue: Choosing the Right Framework",
    "Mastering Git for Effective Collaboration",
    "The Future of Web Development: Trends to Watch",
    "Building Scalable Applications with Microservices",
    "Python for Data Analysis: A Comprehensive Guide",
    "Modern CSS Techniques for Web Designers",
    "Test-Driven Development: A Practical Approach",
    "Understanding Asynchronous JavaScript",
    "Building Progressive Web Apps in 2025",
    "The Complete Guide to Docker Containers",
    "Functional Programming with JavaScript",
    "Building Real-time Applications with WebSockets",
    "Introduction to TypeScript for JavaScript Developers",
    "Creating Accessible Web Applications",
    "Database Design Principles for Developers",
    "Optimizing Website Performance: Tips and Tricks",
    "Building Cross-platform Mobile Apps with React Native",
    "Understanding Blockchain Technology",
    "Serverless Architecture: Benefits and Challenges",
    "Introduction to Natural Language Processing",
    "Building Secure Web Applications",
    "The Art of Code Review: Best Practices",
    "DevOps for Web Developers"
]

# Sample post content (lorem ipsum)
POST_CONTENT_TEMPLATE = """
# {title}

*Published on {date} in {category}*

{intro}

## What You'll Learn

{what_youll_learn}

## Getting Started

{getting_started}

## Key Concepts

{key_concepts}

## Advanced Techniques

{advanced_techniques}

## Conclusion

{conclusion}

"""

LOREM_PARAGRAPHS = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam auctor, nisl eget ultricies aliquam, nunc nisl aliquet nunc, quis aliquam nisl nunc quis nisl. Nullam auctor, nisl eget ultricies aliquam, nunc nisl aliquet nunc, quis aliquam nisl nunc quis nisl.",
    
    "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.",
    
    "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga.",
    
    "Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae.",
    
    "Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam.",
    
    "Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam.",
    
    "Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur? Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
]

def random_date(start_date, end_date):
    """Generate a random date between start_date and end_date."""
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + datetime.timedelta(days=random_number_of_days)

def generate_post_content(title, date, category):
    """Generate random post content."""
    return POST_CONTENT_TEMPLATE.format(
        title=title,
        date=date.strftime("%B %d, %Y"),
        category=category,
        intro=random.choice(LOREM_PARAGRAPHS),
        what_youll_learn=random.choice(LOREM_PARAGRAPHS),
        getting_started=random.choice(LOREM_PARAGRAPHS),
        key_concepts=random.choice(LOREM_PARAGRAPHS),
        advanced_techniques=random.choice(LOREM_PARAGRAPHS),
        conclusion=random.choice(LOREM_PARAGRAPHS)
    )

def generate_sample_posts(num_posts=20):
    """Generate sample blog posts."""
    # Create sources directory if it doesn't exist
    sources_dir = Path("sources")
    sources_dir.mkdir(exist_ok=True)
    
    # Generate posts
    start_date = datetime.date(2024, 1, 1)
    end_date = datetime.date(2025, 5, 30)
    
    # Use titles from our list or generate more if needed
    titles = POST_TITLES.copy()
    if num_posts > len(titles):
        for i in range(len(titles), num_posts):
            titles.append(f"Sample Blog Post {i+1}")
    
    # Shuffle titles to randomize
    random.shuffle(titles)
    
    for i in range(num_posts):
        title = titles[i]
        date = random_date(start_date, end_date)
        category = random.choice(CATEGORIES)
        tags = random.sample(TAGS, k=random.randint(2, 5))
        
        # Generate slug from title
        slug = title.lower().replace(" ", "-").replace(":", "").replace("'", "")
        
        # Generate content
        content = generate_post_content(title, date, category)
        
        # Create frontmatter
        frontmatter = f"""---
title: "{title}"
date: {date.strftime("%Y-%m-%d")}
category: {category}
tags: [{", ".join(f'"{tag}"' for tag in tags)}]
---

"""
        
        # Write to file
        file_path = sources_dir / f"{slug}.md"
        with open(file_path, "w") as f:
            f.write(frontmatter + content)
        
        print(f"Generated post: {file_path}")

if __name__ == "__main__":
    # Generate 20 sample posts
    generate_sample_posts(20)
    print("Sample posts generation complete!")
