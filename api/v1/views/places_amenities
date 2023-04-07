#!/usr/bin/python3
"""
Defines the API actions for the Place/Amenity relationship
"""

from flask import abort, jsonify, request
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.amenity import Amenity


@app_views.route('/places/<place_id>/amenities', methods=['GET'],
                 strict_slashes=False)
def get_amenities_by_place(place_id):
    """Retrieves the list of all Amenity objects of a Place"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    amenities = []
    if storage_t == 'db':
        for amenity in place.amenities:
            amenities.append(amenity.to_dict())
    else:
        for amenity_id in place.amenity_ids:
            amenity = storage.get(Amenity, amenity_id)
            if amenity:
                amenities.append(amenity.to_dict())

    return jsonify(amenities)


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_amenity_from_place(place_id, amenity_id):
    """Deletes a Amenity object to a Place"""
    place = storage.get(Place, place_id)
    amenity = storage.get(Amenity, amenity_id)
    if place is None or amenity is None:
        abort(404)
    if amenity not in place.amenities and amenity_id not in place.amenity_ids:
        abort(404)

    if storage_t == 'db':
        place.amenities.remove(amenity)
        storage.save()
    else:
        place.amenity_ids.remove(amenity_id)
        storage.save(place)

    return jsonify({})


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=['POST'], strict_slashes=False)
def link_amenity_to_place(place_id, amenity_id):
    """Link a Amenity object to a Place"""
    place = storage.get(Place, place_id)
    amenity = storage.get(Amenity, amenity_id)
    if place is None or amenity is None:
        abort(404)

    if storage_t == 'db':
        if amenity in place.amenities:
            return jsonify(amenity.to_dict()), 200
        else:
            place.amenities.append(amenity)
            storage.save()
            return jsonify(amenity.to_dict()), 201
    else:
        if amenity_id in place.amenity_ids:
            return jsonify(amenity.to_dict()), 200
        else:
            place.amenity_ids.append(amenity_id)
            storage.save(place)
            return jsonify(amenity.to_dict()), 201
