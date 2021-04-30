def test_home_page_with_fixture(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Dancing Goat" in response.data
    assert b"Latest Article" in response.data
