# pylint: disable=E1101,W0613
# Service interface. Disabled unused argument rule.
from abc import abstractmethod
from app.models.search_models import SearchRequest


class SearchService:
    """Interface for Search Service"""

    @abstractmethod
    def execute_search_query(self, search_request: SearchRequest):
        """Evaluate given search query and return the list of results"""
