# Personal Blog - Baiju Muthukadan

A simple personal blog built with plain HTML and CSS, following Material Design principles.

## Structure

```
muthukadan.net/
├── css/
│   └── styles.css
├── images/
│   └── profile-placeholder.jpg
├── js/
│   └── main.js
├── posts/
│   ├── hello-world.html
│   └── sample-post.html
├── about.html
├── connect.html
├── index.html
├── posts.html
└── README.md
```

## Features

- Responsive design that works on all devices
- Material Design inspired UI
- Blog post listing page
- Individual blog post pages
- About page
- Contact form
- Clean and modern aesthetic
- Development server with auto-refresh capability

## Development Setup

### Prerequisites

- Python 3.6 or higher (comes with built-in http.server module)

### Running the Development Server

This blog uses Python's built-in HTTP server for local development, which is simple and requires no installation:

```bash
# Navigate to the project directory
cd /path/to/muthukadan.net

# Start the server on port 8000 (default)
python3 -m http.server

# Or specify a custom port
python3 -m http.server 8080
```

After running the command, you can access the blog by opening your web browser and navigating to:
- http://localhost:8000 (or the custom port you specified)

### Development Workflow

1. Start the server using the command above
2. Make changes to your HTML, CSS, or JavaScript files
3. Refresh your browser to see the changes
4. To stop the server, press Ctrl+C in the terminal

### Development Features

- **Simple setup**: No dependencies or installation required
- **Cross-platform**: Works on macOS, Linux, and Windows
- **Lightweight**: Minimal resource usage
- **Easy to use**: Single command to start development

## Content Management

1. To add a new blog post, create a new HTML file in the `posts/` directory
2. Update the posts listing on the homepage and posts.html page
3. Customize the content, images, and links to match your preferences
4. Replace the profile-placeholder.jpg with your own image

## Customization

You can customize the colors by modifying the CSS variables in the `styles.css` file:

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

## Deployment

To deploy this blog to a production environment:

1. No build step is required for this static site
2. Upload all the HTML, CSS, JavaScript, and image files to your web hosting provider
3. Ensure your web server is configured to serve index.html as the default page

## Troubleshooting

### Port Already in Use

If you see an error like "Address already in use", try the following:

1. Use a different port: `python3 -m http.server 8080` (or any other available port)
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
