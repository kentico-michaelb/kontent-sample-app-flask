def test_articles_page_with_fixture(test_client):
    response = test_client.get('/articles')
    assert response.status_code == 200
    assert b"Articles" in response.data

def test_article_detail_with_fixture(test_client):
    response = test_client.get('/articles/coffee-beverages-explained')
    assert response.status_code == 200
    assert b"Coffee Beverages Explained" in response.data