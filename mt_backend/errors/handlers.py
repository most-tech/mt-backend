from flask import Blueprint
from flask import render_template

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(500)
def handle_500(error):
    """Handle error."""
    return render_template("error500.html", title="błąd serwera"), 500


@errors.app_errorhandler(404)
def handle_404(error):
    """Handle error."""
    return render_template("error404.html", title="page not found"),404