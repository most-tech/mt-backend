from abc import ABC

from app.models.search_models import SearchRequest
from app.service.search_service import SearchService

TEST_DATA = {
    "test1": '[{"paragraph": "test paragraph 1"}, {"paragraph": "test paragraph 2"}]'
}


class SearchServiceMock(ABC, SearchService):
    def execute_search_query(self, search_query: SearchRequest):
        return TEST_DATA[search_query.search_term]
