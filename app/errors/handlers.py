from flask import Blueprint
from flask import jsonify

errors = Blueprint("errors", __name__)


@errors.errorhandler(404)
def resource_not_found(error):
    return jsonify(error=str(error)), 404


@errors.errorhandler(500)
def handle_500(error):
    """Handle error."""
    return str(error), 500
