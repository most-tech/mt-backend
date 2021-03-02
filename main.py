from flask import Flask
from app.routes.search import SEARCH

app = Flask(__name__)
app.register_blueprint(SEARCH)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True, threaded=True)
