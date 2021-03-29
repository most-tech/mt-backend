from app.models.search_models import SearchRequest

SEARCH_ENDPOINT = "/search/"
QUERY_ENDPOINT = SEARCH_ENDPOINT + "query"


def test_hello(test_client):
    response = test_client.get(SEARCH_ENDPOINT)
    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Hello search!"


def test_search_query(test_client):
    sq = SearchRequest(search_term="test1", labels="testlabel").to_json()
    response = test_client.post(
        QUERY_ENDPOINT, data=sq, content_type="application/json"
    )
    assert response.status_code == 200
    assert (
        response.get_data(as_text=True)
        == '[{"paragraph": "test paragraph 1"}, {"paragraph": "test paragraph 2"}]'
    )
