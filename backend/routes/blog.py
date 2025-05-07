import os
import markdown
from flask import Blueprint

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/blog')
def blog():
    posts = []
    blog_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'blog')
    if not os.path.exists(blog_dir):
        os.makedirs(blog_dir)
    for filename in os.listdir(blog_dir):
        if filename.endswith('.md'):
            with open(os.path.join(blog_dir, filename), 'r') as f:
                content = f.read()
                html_content = markdown.markdown(content)
                posts.append({
                    'title': filename.replace('.md', '').replace('-', ' ').title(),
                    'content': html_content
                })
    return {"posts": posts}
