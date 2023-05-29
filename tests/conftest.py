from unittest.mock import patch
import pytest
from fastapi.testclient import TestClient

import db
from main import app
from tests.db.test_db import get_session_test, Base_test


@pytest.fixture
def client():
    client = TestClient(app)
    yield client



@pytest.fixture(scope='session', autouse=True)
def setup_and_teardown():
    print("Setup")

    yield

    with get_session_test() as session:
        users = session.query(db.User).all()
        for user in users:
            session.delete(user)
            session.commit()
    print('TearDown')


@pytest.fixture(autouse=True)
def session():
    with get_session_test() as session:
        yield session


@pytest.fixture
def mock_requests_get():
    with patch("requests.get") as mock_get:
        yield mock_get


@pytest.fixture
def patched_get_session(monkeypatch):
    monkeypatch.setattr(db, "get_session", get_session_test)


@pytest.fixture
def data():
    return [1, 2, 3]





