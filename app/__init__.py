from flask import Flask
from config import Config
from app.data.database import init_engine
from app.data.postgresql_repo import PostgresqlTrackRepository

def create_app(Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    init_engine()

    with app.app_context():
        app.track_repo = PostgresqlTrackRepository()

    from app.core.routes import core_bp
    from app.api.routes import api_bp

    app.register_blueprint(api_bp)
    app.register_blueprint(core_bp)

    return app
