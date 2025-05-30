"""
Unit tests for the template_handler module.
"""

import os
import tempfile
import pytest
from unittest.mock import patch, mock_open, MagicMock
import datetime
from jinja2 import Environment, FileSystemLoader

from site_generator.template_handler import generate_html_files

class TestTemplateHandler:
    """Tests for the template_handler module."""
    
    @patch('site_generator.template_handler.Environment')
    @patch('site_generator.template_handler.open', new_callable=mock_open)
    def test_generate_html_files_posts(self, mock_file, mock_env_class):
        """Test generating HTML files for posts."""
        # Setup mock environment and templates
        mock_env = MagicMock()
        mock_env_class.return_value = mock_env
        
        mock_post_template = MagicMock()
        mock_post_template.render.return_value = "<html>Post content</html>"
        
        mock_posts_list_template = MagicMock()
        mock_posts_list_template.render.return_value = "<html>Posts list</html>"
        
        mock_index_template = MagicMock()
        mock_index_template.render.return_value = "<html>Index content</html>"
        
        mock_env.get_template.side_effect = lambda name: {
            'post.html': mock_post_template,
            'posts_list.html': mock_posts_list_template,
            'index.html': mock_index_template
        }[name]
        
        # Create test posts
        posts = [
            {
                'title': 'Test Post 1',
                'date': 'May 30, 2025',
                'date_obj': datetime.datetime(2025, 5, 30),
                'category': 'Test',
                'tags': ['test', 'markdown'],
                'content': '<h1>Test Content 1</h1>',
                'excerpt': 'Test excerpt 1',
                'slug': 'test-post-1',
                'url': 'posts/test-post-1.html'
            },
            {
                'title': 'Test Post 2',
                'date': 'May 29, 2025',
                'date_obj': datetime.datetime(2025, 5, 29),
                'category': 'Example',
                'tags': ['example', 'markdown'],
                'content': '<h1>Test Content 2</h1>',
                'excerpt': 'Test excerpt 2',
                'slug': 'test-post-2',
                'url': 'posts/test-post-2.html'
            }
        ]
        
        # Call the function
        generate_html_files(posts, [])
        
        # Verify template rendering was called correctly
        assert mock_post_template.render.call_count == 2
        assert mock_posts_list_template.render.call_count == 1
        assert mock_index_template.render.call_count == 1
        
        # Verify files were written
        assert mock_file.call_count == 4  # 2 posts + 1 posts list + 1 index
    
    @patch('site_generator.template_handler.Environment')
    @patch('site_generator.template_handler.open', new_callable=mock_open)
    def test_generate_html_files_pages(self, mock_file, mock_env_class):
        """Test generating HTML files for pages."""
        # Setup mock environment and templates
        mock_env = MagicMock()
        mock_env_class.return_value = mock_env
        
        mock_page_template = MagicMock()
        mock_page_template.render.return_value = "<html>Page content</html>"
        
        mock_env.get_template.side_effect = lambda name: {
            'page.html': mock_page_template
        }[name]
        
        # Create test pages
        pages = [
            {
                'title': 'About Page',
                'layout': 'page',
                'content': '<h1>About Me</h1>',
                'slug': 'about',
                'url': 'about.html'
            },
            {
                'title': 'Contact Page',
                'layout': 'page',
                'content': '<h1>Contact Me</h1>',
                'slug': 'contact',
                'url': 'contact.html'
            }
        ]
        
        # Call the function
        generate_html_files([], pages)
        
        # Verify template rendering was called correctly
        assert mock_page_template.render.call_count == 2
        
        # Verify files were written
        assert mock_file.call_count == 2  # 2 pages
    
    @patch('site_generator.template_handler.Environment')
    @patch('site_generator.template_handler.open', new_callable=mock_open)
    def test_generate_html_files_no_content(self, mock_file, mock_env_class):
        """Test generating HTML files with no content."""
        # Call the function with empty lists
        generate_html_files([], [])
        
        # Verify no templates were rendered
        mock_env_class.assert_not_called()
        
        # Verify no files were written
        mock_file.assert_not_called()
