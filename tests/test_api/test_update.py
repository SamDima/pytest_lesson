from unittest.mock import patch

from tests.db.test_db import get_session_test


@patch('db_transactions.crud.get_session', get_session_test)
def test_create_user_route(client):
    name = "George Lucas"
    response = client.post(f"/user/?name={name}")
    assert response.status_code == 200
    user_id = response.json()
    assert user_id is not None

    #Update by id
    new_name = "Obi Wan"
    response = client.post(f"/update_user/?id={user_id}&name={new_name}")
    assert response.status_code == 200
    updated_name = response.json()
    assert updated_name == new_name


