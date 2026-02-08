import pytest
from app import create_app
from config import DevelopmentConfig

@pytest.fixture
def app():

    app = create_app(DevelopmentConfig)
    yield app

@pytest.fixture
def client(app):
    return app.test_client()



