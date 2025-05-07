from flask import Blueprint
from backend.data.about_projects_data import projects

projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/projects')
def projects_page():
    return {"projects": projects}
