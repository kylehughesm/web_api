from flask import Blueprint, current_app, jsonify

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/tracks/')
def get_all_tracks():
    results = current_app.track_repo.get_all()
    return jsonify(results)
