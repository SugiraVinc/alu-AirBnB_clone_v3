#!/usr/bin/python3
"""
This module defines a Flask application that serves a RESTful API
"""
import os
from flask import Flask
from api.v1.views import app_views
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def teardown_app(exception):
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """handler for routes that don't exist"""
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    host = os.environ.get("HBNB_API_HOST", "0.0.0.0")
    port = os.environ.get("HBNB_API_PORT", 5000)
    app.run(host=host, port=port, threaded=True)
