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


@app_views.route('/api/v1/stats', methods=['GET'])
def stats():
    """Count the number of objects """
    amenities = storage.count(Amenity)
    cities = storage.count(City)
    places = storage.count(Place)
    reviews = storage.count(Review)
    states = storage.count(State)
    users = storage.count(User)
    return jsonify({"amenities": amenities, "cities": cities,
                    "places": places, "reviews": reviews,
                    "states": states, "users": users})
