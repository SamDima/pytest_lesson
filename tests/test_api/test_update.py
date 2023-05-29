from unittest.mock import patch
from tests.db.test_db import get_session_test


@patch('db_transactions.crud.get_session', get_session_test)
def test_update_user_route(client):
    name = "test_user_name"
    response = client.post(f"/user/?name={name}")
    assert response.status_code == 200
    assert response.content is not None

    user_id = int(response.content)
    update_response = client.post(f"/update_user/?id={user_id}&name={name}_updated")
    assert update_response.status_code == 200
    assert update_response.content.decode('ascii') == f'"{name}_updated"'
    