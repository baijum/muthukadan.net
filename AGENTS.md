# Project: muthukadan.net

Personal blog of Baiju Muthukadan. A Python-based static site generator converts Markdown sources into HTML.

## Architecture

- `sources/` — Blog post markdown files, named `YYYY-MM-<slug>.md`
- `pages/` — Static page markdown files (e.g. About)
- `posts/` — Generated HTML for individual posts (do not edit by hand)
- `templates/` — Jinja2 templates (`index.html`, `post.html`, `posts_list.html`, `page.html`)
- `site_generator/` — Python package that processes markdown and generates the site
- `css/` — Stylesheets (Tailwind-based)
- `index.html`, `posts.html`, `about.html` — Generated top-level pages (do not edit by hand)

## Writing Blog Posts

1. Create a markdown file in `sources/` named `YYYY-MM-<slug>.md`
2. Include YAML front matter:
   ```yaml
   ---
   title: Post Title
   date: YYYY-MM-DD
   category: Category Name
   tags: Tag1, Tag2
   excerpt: One-sentence summary for listings.
   ---
   ```
3. Optional front matter fields: `draft: true` (hides from public listings), `math: true` (enables MathJax), `slug:` (custom URL slug), `author:`
4. Write content in GitHub Flavored Markdown below the front matter
5. Do not repeat the title as an H1 heading — the generator strips duplicate H1s matching the front matter title

## Generating the Site

Run from the project root with the virtualenv activated:

```
source venv/bin/activate
python -m site_generator.cli
```

Always regenerate after adding or editing posts. The generator updates `posts/`, `posts.html`, and `index.html`.

## Key Conventions

- Never edit files in `posts/` or the root-level `index.html`/`posts.html` directly — they are overwritten on generation.
- Source filenames use the format `YYYY-MM-<descriptive-slug>.md` based on the post's publication date.
- The slug used in URLs is derived from the `title` front matter field (or an explicit `slug:` field), not the filename.
- Drafts (`draft: true`) still get HTML generated for preview via direct URL, but are excluded from all public listings and navigation.
- The virtualenv at `venv/` contains all Python dependencies (frontmatter, markdown, pymdown-extensions, jinja2, pygments).

## Testing

```
source venv/bin/activate
python -m pytest
```

## Deployment

The site is hosted via GitHub Pages from the `master` branch. Pushing to `master` deploys automatically.
