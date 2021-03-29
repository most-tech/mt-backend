from flask import Flask
from flask_cors import CORS
from flask_injector import FlaskInjector

from app.dependencies import configure
from app.routes.search import SEARCH

app = Flask(__name__)
app.register_blueprint(SEARCH)
CORS(app)
FlaskInjector(app=app, modules=[configure])

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True, threaded=True)
