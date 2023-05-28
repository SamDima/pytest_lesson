from unittest.mock import patch
from tests.db.test_db import get_session_test

user_id = None


@patch('db_transactions.crud.get_session', get_session_test)
def test_create_user_route(client):
    """Tests creating new user and that returned value for request is not None"""
    global user_id
    name = "Sherlock Holmes"
    response = client.post(f"/user/?name={name}")
    assert response.text is not None
    user_id = response.text
    print(f"Returned user_id is {user_id} for created user name {name}")


@patch('db_transactions.crud.get_session', get_session_test)
def test_update_user_route(client):
    """Tests updating existing user name and that returned value for request is new name"""
    """Depends on and should only be run after previous test"""
    global user_id
    new_name = 'Dr. Moriarty'
    response = client.post(f"/update_user/?id={user_id}&name={new_name}")
    returned_name = response.text.replace('"','')
    print(f"Returned name is {returned_name} for previously created user with user_id {user_id}")
    assert new_name == returned_name
