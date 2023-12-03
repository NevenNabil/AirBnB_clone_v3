#!/usr/bin/python3
"""
This module that contains API endpoints
"""
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """It is func that returns status in json format"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def count():
    """It is func that retrieves number of each objects by type"""
    return jsonify({"amenities": storage.count("Amenity"),
                    "cities": storage.count("City"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")})
