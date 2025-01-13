# Jekyll Blog Template

This is a template exported from [my personal blog](https://leonson.me). It's hosted by GitHub Pages, linked with my domain name. It has following features:

- One command deployment to Github Pages.
- Multi-language support (e.g. English and Chinese)
- Link preview functionality
- Map embedding in posts
- Tag system
- Handy tools for post management

If you are interested in this template and want to use this to either use GitHub Pages to start blogging, or revive your blog based on GitHub Pages, feel free to give it a try! If you encounter any issues(I am sure you will, but I can't predict what you will encounter), feel free to open an issue and I'll take a look when I have time.

I'll also find time to expand the document to include other features I currently have on my blog. And when I add new features to my blog, I'll include here too.

## Setup

1. Make sure you have Ruby environment setup. I use [asdf](https://asdf-vm.com/) to manage mine.
2. Clone this repository
3. Install dependencies:
   ```bash
   bundle install
   ```
4. Update `_config.yml` with your information
5. Run locally:
   ```bash
   bundle exec jekyll serve
   ```

You should be able to visit the demo blog site at http://127.0.0.1:4000 now.

## Features

### Multi-language Support
Support for multi language content with proper language tags.

### Link Preview
Hovering over internal links shows a preview of the target post.

### Map Integration
Show locations on a map in posts. Use the `locations.yml` file to define locations.

## Scripts

Handy tools I created to manage this blog:
- myblogcli.py : I use "draft" option to start writing a blog. When I finish, I use "publish" option.
- locationpick.html : When I need to add a location to a blog post, I open this html, search for the location, and by simply click the location I copy the data for me to add to `locations.yml` file for Map Integration

## License

This template is available under the MIT License.

## Appreciation

I am grateful for:

1. [Jekyll Framework](https://jekyllrb.com/), on which my blog has depended [since 2018](https://leonson.me/2020/09/blog-migration-history#migration-from-wordpress-to-jekyll2018-or-earlier).
2. [Minimal Mistakes](https://mademistakes.com/work/jekyll-themes/minimal-mistakes/), a minimalist and beautiful Jekyll theme [since 2020](https://leonson.me/2020/09/blog-migration-history#migrating-jekyll-theme-from-minima-to-minimal-mistakes-2020).
3. GitHub Pages, on which my blog host.
4. ChatGPT and Claude, which has been helpful for me to add more features.