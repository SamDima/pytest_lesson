from unittest.mock import patch

from tests.db.test_db import get_session_test


@patch('db_transactions.crud.get_session', get_session_test)
def test_create_user_route(client):
    name = "test_user_name"
    response = client.post(f"/user/?name={name}")
    assert response.status_code == 200
