import os

import pytest
from function.app import app

TEST_CONFIG = {
    'TESTING': True,
    'DEBUG': True,
    'PORT': 1337,
    'NAME': 'test',
    'SQLALCHEMY_DATABASE_URI': (f"postgresql://{os.getenv('PGUSER')}:{os.getenv('PGPASSWORD')}@"
                                f"{os.getenv('PGHOST')}:{os.getenv('PGPORT')}/{os.getenv('PGDATABASE')}"),
    'SQLALCHEMY_TRACK_MODIFICATIONS': False
}


@pytest.fixture
def test_app():
    with app.app_context():
        yield app


@pytest.fixture(scope="function")
def test_client(test_app):
    return test_app.test_client()
