from flask import Blueprint, abort, request
from flask_cors import cross_origin
from injector import inject

from app.models.search_models import SearchRequest
from app.service.search_service import SearchService

SEARCH = Blueprint("search", __name__, url_prefix="/search")
MANAGE = Blueprint("manage",__name__, url_prefix="/manage")

@SEARCH.route("/")
def hello():
    """Greetings endpoint."""
    return "Hello search!"


@inject
@SEARCH.route("/query", methods=["POST"])
@cross_origin()
def search_by_query(search_service: SearchService):
    search_query = SearchRequest.from_json(request.data)
    result = search_service.execute_search_query(search_query)
    if result is None:
        abort(404, description="Resource not found")
    return result


@MANAGE.route("/")
def hello():
    """Greetings endpoint."""
    return "yo, yo, manage speaking!"


@inject
@MANAGE.route("/insert", methods=["POST"])
@cross_origin()
def insert_new_document(search_service: SearchService):
    search_query = SearchQuery.from_json(request.data)
    result = search_service.execute_search_query(search_query)
    if result is None:
        abort(404, description="Resource not found")
    return SearchResponse.from_result(result).to_json()