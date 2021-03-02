from flask import Flask


def create_app():
    app = Flask(__name__)
    from mt_backend.errors.handlers import errors
    from mt_backend.searcher.searcher import searcher
    app.register_blueprint(searcher)
    app.register_blueprint(errors)
    return app