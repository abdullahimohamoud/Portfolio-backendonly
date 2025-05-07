from flask import Blueprint
from backend.data.about_projects_data import about_data

about_bp = Blueprint('about', __name__)

@about_bp.route('/about')
def about():
    return about_data
