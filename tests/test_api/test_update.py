from unittest.mock import patch

from tests.db.test_db import get_session_test


@patch('db_transactions.crud.get_session', get_session_test)
def test_update_user_route(client):
    name = "test_user_name"
    response = client.post(f"/user/?name={name}")
    assert response.status_code == 200
    created_id = response.json()
    new_name = "updated_user_name"
    response = client.post(f"/update_user/?id={created_id}&name={new_name}")
    assert response.status_code == 200
    updated_name = response.json()
    assert updated_name == new_name
