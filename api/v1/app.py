#!/usr/bin/python3
"""This module defines a Flask application that serves a RESTful API"""

import os
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify

app = Flask(__name__)

app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def teardown_storage(exception):
    """Closes the storage"""
    storage.close()


@app.errorhandler(404)
def error_not_found(error):
    """404 error"""
    return jsonify({"error": "Not found"}
