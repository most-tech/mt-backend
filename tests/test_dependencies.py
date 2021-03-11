from flask import Config
from injector import singleton, inject

from app.service.elasticsearch_service import ElasticsearchService
from app.service.search_service import SearchService
from tests.mocks.search_service_mock import SearchServiceMock


def configure(binder):
    binder.bind(
        SearchService,
        to=SearchServiceMock,
        scope=singleton,
    )
