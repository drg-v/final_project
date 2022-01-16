import pytest
from app import create_app
from app import db


@pytest.fixture
def client():
    app = create_app('config.TestConfig')
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
