from unittest.mock import patch
from tests.db.test_db import get_session_test

@patch('db_transactions.crud.get_session', get_session_test)
def test_update_user_route(client):
    response = client.post('/user/', json={'name': 'User_Megi'})
    assert response.status_code == 200
    user_id = response.json()
    updated_response = client.post(f'/update_user/{user_id}', json={'name': 'Updated_Megi'})
    assert updated_response.status_code == 200
    update_data = updated_response.json()
    assert update_data == 'Updated_Megi'
