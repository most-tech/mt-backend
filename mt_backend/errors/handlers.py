from flask import Blueprint


errors = Blueprint("errors", __name__)


@errors.app_errorhandler(500)
def handle_500(error):
    """Handle error."""
    return str(error), 500


@errors.app_errorhandler(404)
def handle_404(error):
    """Handle error."""
    return str(error), 404