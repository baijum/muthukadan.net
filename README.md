# Personal Blog - Baiju Muthukadan

A static site generator that converts Markdown to HTML for a personal blog, built with Python and Jinja2 templates.


## Features

- Python-based static site generator
- Responsive design that works on all devices
- Material Design inspired UI
- Blog post listing page
- Individual blog post pages
- Static pages support (About page, etc.)
- Clean and modern aesthetic
- **GitHub Flavored Markdown support** with extensive extensions
- **MathJax integration** for rendering mathematical equations
- Automatic HTML generation from Markdown sources
- Jinja2 templating system
- Installable as a Python package

## Development Setup

### Prerequisites

- Python 3.6 or higher
- Required Python packages (installed via pip):
  - markdown
  - pymdown-extensions
  - python-frontmatter
  - pygments
  - jinja2
  - pytest (for development)

### Installation

You can install the site generator in development mode:

```bash
# Clone the repository
git clone https://github.com/yourusername/muthukadan.net.git
cd muthukadan.net

# Install in development mode
pip install -e .

# Or install with development dependencies
pip install -e ".[dev]"
```

### Running the Site Generator

After installation, you can generate the site using the command-line interface:

```bash
# Generate the site
generate-site
```

Or run the module directly:

```bash
python -m site_generator.cli
```

### Development Server

For local development, you can use Python's built-in HTTP server:

```bash
# Start the server on port 8000 (default)
python -m http.server

# Or specify a custom port
python -m http.server 8080
```

After running the command, you can access the blog by opening your web browser and navigating to:
- http://localhost:8000 (or the custom port you specified)

### Development Workflow

1. Write or edit content in Markdown format in the `sources/` or `pages/` directories
2. Run the site generator to convert Markdown to HTML
3. Start the development server
4. View your changes in the browser
5. To stop the server, press Ctrl+C in the terminal

## Content Management

### Blog Posts

1. Write your blog posts in GitHub Flavored Markdown format and save them in the `sources/` directory
2. Run the site generator to convert Markdown to HTML:
   ```bash
   # Run the generator command
   generate-site
   ```
3. The generator will automatically create HTML files in the `posts/` directory and update the posts listing page

#### Draft Posts

You can create draft posts that are hidden from public listings but still accessible via direct URL for preview:

1. **Creating a Draft**: Add `draft: true` to your post's front matter:
   ```yaml
   ---
   title: My Work in Progress
   date: 2025-06-01
   category: Technology
   tags: Draft, Example
   draft: true
   ---
   ```

2. **Draft Behavior**:
   - ✅ HTML files are generated for drafts (accessible at `posts/your-post-slug.html`)
   - ✅ Draft posts show `[DRAFT]` prefix in the title when viewed directly
   - ❌ Drafts don't appear in the posts list page
   - ❌ Drafts don't appear on the homepage recent posts
   - ❌ Drafts are excluded from pagination and category filtering
   - ❌ Drafts are skipped in post navigation (prev/next links)

3. **Publishing a Draft**: Remove the `draft: true` line or change it to `draft: false`, then regenerate the site

4. **Preview Drafts**: You can share draft URLs for review without affecting your public site

### Static Pages

1. Write your pages in Markdown format and save them in the `pages/` directory
2. Run the site generator to convert them to HTML
3. Pages will be generated at the root level of the site

### Writing Content in Markdown

#### File Location

- Blog posts should be placed in the `sources/` directory
- Static pages should be placed in the `pages/` directory

#### Front Matter

Each Markdown file should begin with front matter - a YAML section at the top of the file that defines metadata. The front matter is enclosed between triple dashes (`---`).

##### For Blog Posts:

```yaml
---
title: My Awesome Blog Post
date: 2025-06-01
category: Technology
tags: Programming, Python, Web Development
excerpt: A brief description of your post that will appear in the posts listing.
draft: false  # Optional: set to true to hide from public listings
---
```

Required front matter fields for posts:
- `title`: The title of your blog post
- `date`: The publication date in YYYY-MM-DD format
- `category`: The primary category for your post

Optional front matter fields for posts:
- `author`: The author name (defaults to the site author)
- `tags`: Comma-separated list of tags
- `excerpt`: A brief description (if not provided, it will be extracted from the content)
- `slug`: Custom URL slug (if not provided, it will be generated from the title)
- `draft`: Set to `true` to hide the post from public listings (defaults to `false`)

##### For Pages:

```yaml
---
title: About Me
layout: page
---
```

Required front matter fields for pages:
- `title`: The title of your page

Optional front matter fields for pages:
- `layout`: The template to use (defaults to 'page')
- `slug`: Custom URL slug (if not provided, it will use the filename)

#### Markdown Features

The site generator supports GitHub Flavored Markdown with extensive extensions, including:

- **Headings** (# H1, ## H2, etc.)
- **Text formatting** (bold, italic, strikethrough)
- **Lists** (ordered and unordered)
- **Links** and images
- **Code blocks** with syntax highlighting via Pygments
- **Tables**
- **Blockquotes**
- **Task lists** ([x] Done, [ ] Todo)
- **Tabbed content** via pymdownx.tabbed
- **Emoji support** via pymdownx.emoji
- **Highlighted text** via pymdownx.mark
- **Mathematical equations** with MathJax

#### Example Markdown Post

```markdown
---
title: Hello World
date: 2025-05-29
category: Personal
tags: Introduction, Blog
draft: false  # Set to true to keep as draft
---

# Hello World

Welcome to my first blog post! This is written in **Markdown** and converted to HTML.

## Features

Here are some things I can do:

- Write lists
- Add [links](https://example.com)
- Include code snippets:

```python
def hello():
    return "Hello, World!"
```

> This is a blockquote with some wisdom.
```

### Template Customization

The templates used for generating HTML are located in the `templates/` directory:
- `index.html`: Template for the homepage
- `post.html`: Template for individual post pages
- `posts_list.html`: Template for the posts listing page
- `page.html`: Template for static pages

These are Jinja2 templates that you can modify to customize the appearance of your site.

## Customization

### Site Information

You can customize the site information by modifying the variables in `site_generator/config.py`:

```python
# Site information
SITE_TITLE = "Baiju Muthukadan"
SITE_DESCRIPTION = "Personal Blog"
DEFAULT_AUTHOR = "Baiju Muthukadan"
```

### Styling

You can customize the colors and styles by modifying the CSS variables in the `css/styles.css` file:

```css
:root {
    --primary-color: #6200ee;
    --primary-dark: #3700b3;
    --primary-light: #bb86fc;
    --secondary-color: #03dac6;
    --secondary-dark: #018786;
    /* ... other variables ... */
}
```

### Templates

The site uses Jinja2 templates that you can customize to change the layout and appearance of your site. The templates are located in the `templates/` directory.

## Project Structure

### Core Components

- `site_generator/`: Python package containing the site generator code
  - `cli.py`: Command-line interface for the site generator
  - `config.py`: Configuration settings
  - `markdown_processor.py`: Functions for processing Markdown files
  - `template_handler.py`: Functions for generating HTML from templates
  - `utils.py`: Utility functions

### Content Directories

- `sources/`: Markdown files for blog posts
- `pages/`: Markdown files for static pages
- `posts/`: Generated HTML files for blog posts
- `templates/`: Jinja2 templates for the site

### Configuration

The site configuration is defined in `site_generator/config.py` and includes:

- Directory paths
- Output file names
- Site information (title, description, author)

You can modify these settings to customize your site.

## Advanced Features

### Mathematical Equations with MathJax

The site generator supports mathematical equations using MathJax, which renders LaTeX syntax. Here's how to use it:

#### Inline Equations

For inline equations, use single dollar signs:

```markdown
Einstein's famous equation: $E = mc^2$
```

This will render as: Einstein's famous equation: $E = mc^2$

#### Display Equations

For standalone equations, use double dollar signs:

```markdown
$$
\frac{d}{dx}\left( \int_{a}^{x} f(u)\,du\right)=f(x)
$$
```

This will render as a centered equation on its own line.

#### LaTeX Support

MathJax supports most LaTeX math commands, including:

- Fractions: `\frac{numerator}{denominator}`
- Greek letters: `\alpha`, `\beta`, `\gamma`, etc.
- Superscripts and subscripts: `x^2`, `y_i`
- Matrices, integrals, summations, and more

See the `math-example.md` file in the sources directory for more examples.

## Deployment

To deploy this blog to a production environment:

1. Generate the HTML files using the site generator
2. Upload all the HTML, CSS, JavaScript, and image files to your web hosting provider
3. Ensure your web server is configured to serve index.html as the default page

## Testing

The project includes unit tests for the site generator components. You can run the tests using pytest:

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
python -m pytest
```

## Troubleshooting

### Port Already in Use

If you see an error like "Address already in use" when starting the development server, try the following:

1. Use a different port: `python -m http.server 8080` (or any other available port)
2. Find and stop the process using the current port:
   ```bash
   # Find the process using port 8000
   lsof -i :8000
   
   # Kill the process
   kill <PID>
   ```

### Browser Caching Issues

If you don't see your changes after refreshing:

1. Try a hard refresh (Ctrl+F5 or Cmd+Shift+R)
2. Clear your browser cache
3. Open the site in an incognito/private browsing window

### Markdown Conversion Issues

If you encounter issues with the Markdown-to-HTML conversion:

1. Make sure your Markdown files have valid front matter
2. Check that all dependencies are installed correctly
3. Look for error messages in the generator output
4. Verify that your Markdown syntax is correct

### Draft Posts Not Working

If draft posts are still appearing in public listings:

1. Ensure the `draft: true` field is properly formatted in the YAML front matter
2. Check that there are no spaces or special characters in the draft field
3. Regenerate the site after making changes to the draft status
4. Verify the generator output shows the post as "DRAFT" during processing

### Missing Draft Posts

If you can't find your draft posts:

1. Check the generator output for the direct URL (e.g., `posts/your-post-slug.html`)
2. Ensure the draft post was processed successfully (look for "Successfully processed DRAFT post" message)
3. Navigate directly to the draft URL in your browser
4. Remember that drafts won't appear in any public listings or navigation
