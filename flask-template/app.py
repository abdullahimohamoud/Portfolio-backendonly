import os
import requests
import markdown
from datetime import datetime
from flask import Flask, send_from_directory
from backend.routes.about import about_bp
from backend.routes.projects import projects_bp
from backend.routes.resume import resume_bp
from backend.routes.gallery import gallery_bp
from backend.routes.blog import blog_bp

app = Flask(__name__)

UNSPLASH_ACCESS_KEY = os.environ.get('UNSPLASH_ACCESS_KEY', 'YOUR_UNSPLASH_ACCESS_KEY')

def fetch_unsplash_photos(query="Nature", per_page=9):
    url = "https://api.unsplash.com/search/photos"
    params = {
        "query": query,
        "per_page": per_page,
        "client_id": UNSPLASH_ACCESS_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return [photo['urls']['small'] for photo in data['results']]
    return []

about_data = {
    "education": [
        {"degree": "B.Sc. Computer Science", "institution": "Example University", "year": "2020"},
        {"degree": "M.Sc. Data Science", "institution": "Sample Institute", "year": "2022"}
    ],
    "work_experience": [
        {"role": "Software Engineer", "company": "TechCorp", "years": "2022-Present"},
        {"role": "Intern", "company": "WebStart", "years": "2020-2021"}
    ],
    "skills": ["Python", "Flask", "HTML", "CSS", "JavaScript", "SQL"]
}

projects = [
    {
        "title": "Personal Portfolio Website",
        "tech_stack": ["Python", "Flask", "HTML", "CSS"],
        "description": "A personal website to showcase my work, skills, and blog posts."
    },
    {
        "title": "Photo Gallery App",
        "tech_stack": ["Python", "Flask", "Unsplash API"],
        "description": "A web app that displays photos from Unsplash based on user-selected keywords."
    },
    {
        "title": "Blog Platform",
        "tech_stack": ["Flask", "Markdown", "Bootstrap"],
        "description": "A simple blog platform with Markdown support."
    }
]

@app.context_processor
def inject_year():
    return {'current_year': datetime.now().year}

app.register_blueprint(about_bp)
app.register_blueprint(projects_bp)
app.register_blueprint(resume_bp)
app.register_blueprint(gallery_bp)
app.register_blueprint(blog_bp)

@app.route("/")
def home():
    return "Backend is running."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)
