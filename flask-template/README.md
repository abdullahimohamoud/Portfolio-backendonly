# Flask Portfolio Backend

A modular Python Flask backend for a personal portfolio API. Provides endpoints for about info, projects, Unsplash-powered gallery, and blog posts.

## Project Structure

```
backend/
    data/
        about_projects_data.py
    routes/
        about.py
        blog.py
        gallery.py
        projects.py
        resume.py
    services/
        unsplash.py
flask-template/
    app.py
    requirements.txt
    dev-requirements.txt
    pyproject.toml
    README.md
```

## Quick Start

1. **Install dependencies:**
   ```sh
   python3 -m pip install -r flask-template/requirements.txt
   ```
2. **(Optional) Set Unsplash API key:**
   ```sh
   export UNSPLASH_ACCESS_KEY=your_actual_unsplash_access_key
   ```
3. **Run the backend:**
   ```sh
   cd flask-template
   python3 app.py
   ```
4. **Test endpoints:**
   - About:         `GET /about`
   - Projects:      `GET /projects`
   - Gallery:       `GET /gallery`
   - Blog:          `GET /blog`
   - Resume:        `GET /resume`

---
Made with love by @uncannystranger
