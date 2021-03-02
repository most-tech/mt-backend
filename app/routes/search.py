from flask import Blueprint, abort
from app.models.search_query import SearchQuery
from app.service.search_service import execute_search_query

SEARCH = Blueprint("search", __name__, url_prefix="/search")


@SEARCH.route("/search/<request>", methods=["GET"])
def search_by_query(request):
    search_query = SearchQuery.from_json(request.json)
    result = execute_search_query(search_query)
    if result is None:
        abort(404, description="Resource not found")
    return result
