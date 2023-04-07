#!/usr/bin/python3
"""
Create a blueprint
"""
from os import getenv
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

"""import views after defining app_views blueprint"""
from api.v1.views.index import *
from api.v1.views.amenities import *
from api.v1.views.states import *
from api.v1.views.places import *
from api.v1.views.cities import *
from api.v1.views.users import *
from api.v1.views.places_reviews import *
from api.v1.views.places_amenities import *

if getenv('HBNB_ENV') == 'test':
    app.config['TESTING'] = True

if getenv('HBNB_STORAGE') == 'db':
    storage_t = 'db'
else:
    storage_t = 'fs'

@app.teardown_appcontext
def close(self):
    """Close method"""
    self.reload()
