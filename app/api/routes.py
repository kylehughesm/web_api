from flask import Blueprint, current_app, jsonify, request

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/tracks', strict_slashes=False)
def get_tracks():
    genre_name = request.args.get('genre_name')
    results = current_app.track_repo.get_tracks(genre_name=genre_name)
    return jsonify(results)
