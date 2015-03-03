# -*- coding: utf-8 -*-

from flask import Blueprint

from . import route
from ..services import locations

bp = Blueprint('locations', __name__, url_prefix='/location')


@route(bp, 's')
def list_films():
    """Returns all locations."""
    return [l for l in locations.all()]


@route(bp, '/<location_id>')
def get_film(location_id):
    """Returns a location instance."""
    return locations.get_or_404(location_id)
