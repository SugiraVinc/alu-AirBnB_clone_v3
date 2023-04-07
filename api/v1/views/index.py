#!/usr/bin/python3
"""Create a route on the object app_views that returns a JSON: "status":OK """
from flask import Flask, jsonify
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app_views.route('/status', methods=['GET'])
def status():
    """Status of the API"""
    print("status function called")
    return jsonify({'status': 'OK'})
