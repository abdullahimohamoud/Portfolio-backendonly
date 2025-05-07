from flask import Blueprint, jsonify, request
from backend.services.unsplash import fetch_unsplash_photos

gallery_bp = Blueprint('gallery', __name__)

@gallery_bp.route('/gallery')
def gallery():
    keyword = request.args.get('keyword', 'Nature')
    photos = fetch_unsplash_photos(keyword)
    return {"photos": photos, "keyword": keyword}
