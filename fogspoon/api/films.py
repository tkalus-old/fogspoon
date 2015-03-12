# -*- coding: utf-8 -*-

from flask import Blueprint, current_app, request

from ..services import films
from . import route

bp = Blueprint('films', __name__, url_prefix=u'/film')


@route(bp, u's')
def list_films():
    """Selectively return complete information on all films.
    or simply a dict of film titles and their ids.

    /films?full -> return full info
    """
    app = current_app._get_current_object()
    if request.query_string == 'full' and app.config.get('DEBUG', True):
        return [f for f in films.all()]
    return list({'title': f.display_title,
                 'id': f.id} for f in films.all())


@route(bp, u'/<film_id>')
def get_film(film_id):
    """Returns a film instance."""
    film = films.get_or_404(film_id)
    callback = request.args.get('callback', False)
    if callback:
        return film.to_geo_json
    q_format = request.args.get('format', False)
    if q_format == 'geo_json':
        return film.to_geo_json
    return film
