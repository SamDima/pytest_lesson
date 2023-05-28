from unittest.mock import patch

from tests.db.test_db import get_session_test

@patch('db_transactions.crud.get_session', get_session_test)
def test_update_user(client):
    # Step 1: Create test user. Expected response: int — user id
    old_name = "User 1"
    response = client.post(f"/user/?name={old_name}")
    assert response.status_code == 200
    uid = response.json()
    assert isinstance(uid, int)

    # Requirement: "2. Create new user (assert id is not null)". Explicitly.
    assert uid is not None

    # Step 2: Update user name: Expected response: new name set
    new_name = "User 2"
    response = client.post(f"/update_user/?id={uid}&name={new_name}")
    assert response.status_code == 200
    assert response.json() == new_name
