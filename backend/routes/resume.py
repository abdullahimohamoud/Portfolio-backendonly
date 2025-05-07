from flask import Blueprint, jsonify, current_app, send_from_directory
import os

resume_bp = Blueprint('resume', __name__)

@resume_bp.route('/resume')
def resume():
    resume_path = os.path.join(current_app.static_folder or '', 'resume.pdf')
    if not os.path.exists(resume_path):
        os.makedirs(os.path.dirname(resume_path), exist_ok=True)
        with open(resume_path, 'wb') as f:
            f.write(b'%PDF-1.4\n%Placeholder resume\n')
    return send_from_directory(os.path.dirname(resume_path), 'resume.pdf', as_attachment=True)
