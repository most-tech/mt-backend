# pylint: disable=E1101,W0613
# Service interface. Disabled unused argument rule.
from abc import abstractmethod
from app.models.search_models import SearchRequest
from app.models.crud_models import LegalDocument


class SearchService:
    """Interface for Search Service"""

    @abstractmethod
    def execute_search_query(self, search_request: SearchRequest):
        """Evaluate given search query and return the list of results"""

    @abstractmethod
    def insert_document(self, legal_document: LegalDocument):
        "Insert new paragraph to db"
