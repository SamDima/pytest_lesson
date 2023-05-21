def test_get_starwars_people(mock_requests_get, client):
    mock_requests_get.return_value.json.return_value = {"name": "Luke Skywalker"}
    # with TestClient(app) as client:
    response = client.get("/people?number=1")

    assert response.status_code == 200
    assert response.json() == {"message": {"name": "Luke Skywalker"}}
    mock_requests_get.assert_called_once_with("https://swapi.dev/api/people/1/")