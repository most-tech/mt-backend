# -*- coding: utf-8 -*-

from mt_backend import create_app

app = create_app()

@app.errorhandler(500)
def handle_500(error):
    """Handle error."""
    return str(error), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, threaded=True)