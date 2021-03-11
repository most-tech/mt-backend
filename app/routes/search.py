from flask import Blueprint, abort, request
from flask_cors import cross_origin
from injector import inject

from app.models.search_query import SearchQuery
from app.service.search_service import SearchService

SEARCH = Blueprint("search", __name__, url_prefix="/search")


@SEARCH.route("/")
def hello():
    """Greetings endpoint."""
    return "Hello search!"


@inject
@SEARCH.route("/query", methods=["GET"])
@cross_origin()
def search_by_query(search_service: SearchService):
    search_query = SearchQuery.from_json(request.data)
    result = search_service.execute_search_query(search_query)
    if result is None:
        abort(404, description="Resource not found")
    return result
