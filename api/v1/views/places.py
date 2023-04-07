#!/usr/bin/python3
"""Endpoint for places"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.place import Place
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity


@app_views.route('/cities/<city_id>/places', methods=['GET'])
def get_places(city_id):
    """Retrieves the list of all Place objects of a City"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    places = [place.to_dict() for place in city.places]
    return jsonify(places)


@app_views.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    """Retrieves a Place object"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    """Deletes a Place object"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    storage.delete(place)
    storage.save()
    return jsonify({})


@app_views.route('/cities/<city_id>/places', methods=['POST'])
def create_place(city_id):
    """Creates a Place"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    if not request.json:
        abort(400, 'Not a JSON')
    if 'user_id' not in request.json:
        abort(400, 'Missing user_id')
    user_id = request.json['user_id']
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    if 'name' not in request.json:
        abort(400, 'Missing name')
    place = Place(**request.json)
    place.city_id = city_id
    place.user_id = user_id
    storage.new(place)
    storage.save()
    return jsonify(place.to_dict()), 201

@app_views.route('/places_search', methods=['POST'])
def search_places():
    """Search for Place objects"""
    if not request.json:
        abort(400, 'Not a JSON')
    states = request.json.get('states', [])
    cities = request.json.get('cities', [])
    amenities = request.json.get('amenities', [])
    if not states and not cities and not amenities:
        places = [place.to_dict() for place in storage.all(Place).values()]
        return jsonify(places)
    state_objs = [storage.get(State, state_id) for state_id in states]
    city_objs = [storage.get(City, city_id) for city_id in cities]
    place_objs = set()
    for state_obj in state_objs:
        if state_obj is None:
            continue
        for city_obj in state_obj.cities:
            place_objs.update(city_obj.places)
    for city_obj in city_objs:
        if city_obj is None:
            continue
        place_objs.update(city_obj.places)
    if not place_objs:
        return jsonify([])
    if amenities:
        amenity_objs = [storage.get(Amenity, amenity_id) for amenity_id in amenities]
        if None in amenity_objs:
            return jsonify([])
        place_objs = set(filter(lambda p: all([a in p.amenities for a in amenity_objs]), place_objs))
    places
