from unittest.mock import patch

from tests.db.test_db import get_session_test


@patch('db_transactions.crud.get_session', get_session_test)
def test_update_user_route(client):
    # create a new user
    name = "new_user"
    response = client.post(f"/user/?name={name}")
    id = response.json()
    assert id is not None

    # updated above created user
    upd_name = "upd_user"
    upd_response = client.post(f"/update_user/?id={id}&name={upd_name}")
    name = upd_response.json()
    assert name == upd_name
