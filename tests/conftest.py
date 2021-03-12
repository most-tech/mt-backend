import os
import pytest
from flask import Flask
from flask_cors import CORS
from flask_injector import FlaskInjector

from app.routes.search import SEARCH
from tests.test_dependencies import configure

app = Flask(__name__)
app.register_blueprint(SEARCH)
FlaskInjector(app=app, modules=[configure])


@pytest.fixture(scope="session")
def test_client():
    """Start the app for test purposes."""
    testing_client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()
