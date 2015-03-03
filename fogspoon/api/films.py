# -*- coding: utf-8 -*-

from flask import Blueprint

from ..services import films
from . import route

bp = Blueprint('films', __name__, url_prefix=u'/film')


@route(bp, u's')
def list_films():
    """Returns all films."""
    return [f for f in films.all()]


@route(bp, u'/<film_id>')
def get_film(film_id):
    """Returns a film instance."""
    return films.get_or_404(film_id)
