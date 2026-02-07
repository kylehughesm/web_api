from flask import Flask
from config import Config

def create_app(Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.core.routes import core_bp

    app.register_blueprint(core_bp)

    return app
