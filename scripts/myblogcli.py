import os
import sys
import datetime
import langid
import shutil
import re
from pathlib import Path

class JekyllPaths:
    def __init__(self):
        # Get the directory where the current script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Navigate up to the project root (blog directory)
        self.project_root = os.path.dirname(script_dir)
        
        # Define paths relative to project root
        self.drafts_folder = os.path.join(self.project_root, "_drafts")
        self.posts_folder = os.path.join(self.project_root, "_posts", "permanent")
        
        # Verify paths exist
        self._verify_paths()
    
    def _verify_paths(self):
        """Verify that the paths exist and create if necessary"""
        for folder in [self.drafts_folder, self.posts_folder]:
            if not os.path.exists(folder):
                raise RuntimeError(f"Directory not exists: {folder}")

class PostManager:
    def __init__(self):
        self.paths = JekyllPaths()

    def create_draft(self, name):
        filename = f"{name.replace(' ', '-').lower()}.md"
        filepath = os.path.join(self.paths.drafts_folder, filename)
        
        if os.path.exists(filepath):
            print(f"Error: Draft '{filename}' already exists.")
            return

        frontmatter = """---
title: 
author: leonson
---
"""
        
        with open(filepath, 'w') as f:
            f.write(frontmatter)
        
        print(f"Draft '{filename}' created in {self.paths.drafts_folder}")

    def publish_draft(self, name):
        draft_filename = f"{name.replace(' ', '-').lower()}.md"
        draft_filepath = os.path.join(self.paths.drafts_folder, draft_filename)
        
        if not os.path.exists(draft_filepath):
            print(f"Error: Draft '{draft_filename}' not found in {self.paths.drafts_folder}")
            return
        
        today = datetime.date.today()
        published_filename = f"{today.isoformat()}-{draft_filename}"
        published_filepath = os.path.join(self.paths.posts_folder, published_filename)
        
        with open(draft_filepath, 'r') as f:
            content = f.read()
            lang, score = langid.classify(content)
        
        # Update frontmatter
        permalink = f"/{today.year}/{today.month:02d}/{os.path.splitext(draft_filename)[0]}"
        updates = {
            'permalink': permalink,
            'lang': lang,
        }
        
        updated_content = self._update_frontmatter(draft_filepath, updates)
        
        with open(published_filepath, 'w') as f:
            f.write(updated_content)
        
        os.remove(draft_filepath)
        print(f"Draft '{draft_filename}' published as '{published_filename}' in {self.paths.posts_folder}")

    def _update_frontmatter(self, filename, updates):
        with open(filename, 'r') as file:
            content = file.read()
        
        # Extract the frontmatter
        match = re.match(r'(---\n)(.*?\n)---', content, re.DOTALL)
        if not match:
            print(f"Error: No frontmatter found in {filename}")
            return content
            
        frontmatter = match.group(2)
        rest_of_content = content[match.end():]
        
        # Process each key-value pair
        for key, value in updates.items():
            if re.search(rf'^{key}:', frontmatter, re.MULTILINE):
                # Update existing key
                frontmatter = re.sub(rf'^{key}:.*\n', f'{key}: {value}\n', frontmatter, flags=re.MULTILINE)
            else:
                # Add new key-value pair
                frontmatter += f'{key}: {value}\n'
        
        # Reconstruct the content
        updated_content = f'---\n{frontmatter}---\n{rest_of_content}'
        return updated_content


def print_usage():
    usage = """
    Jekyll Post Manager - Manage draft and published posts

    Usage:
        python script.py <command> <name>

    Commands:
        draft <name>     Create a new draft post
            - Creates a new markdown file in _drafts folder
            - Name will be converted to lowercase with spaces replaced by hyphens
            - Example: python script.py draft "My New Blog Post"
                    Creates: _drafts/my-new-blog-post.md

        publish <name>   Publish an existing draft
            - Moves draft from _drafts to _posts/permanent
            - Adds date prefix to filename
            - Automatically detects language
            - Adds permalink based on date and title
            - Example: python script.py publish "my-new-blog-post"
                    Creates: _posts/permanent/2024-03-05-my-new-blog-post.md

    Examples:
        1. Create a draft:
        python script.py draft "Getting Started with Python"
        
        2. Publish a draft:
        python script.py publish "getting-started-with-python"

    File Locations:
        - Drafts:  _drafts/
        - Published: _posts/permanent/

    Note:
        - Use the same name for publish as the draft filename (without .md)
        - Names are case-insensitive and will be converted to lowercase
        - Spaces in names will be converted to hyphens
        - For location detection, the file must end with .md extension
    """
    print(usage)


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help', 'help']:
        print_usage()
        return
        
    if len(sys.argv) < 3:
        print("Error: Not enough arguments")
        print_usage()
        return

    try:
        manager = PostManager()
        command = sys.argv[1]
        name = sys.argv[2]

        if command == "draft":
            manager.create_draft(name)
        elif command == "publish":
            manager.publish_draft(name)
        elif command == "locations":
            if not name.endswith('.md'):
                print("Error: File must have .md extension")
                return
            manager.find_locations(name)
        else:
            print("Invalid command. Use 'draft', 'publish', or 'locations'.")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()