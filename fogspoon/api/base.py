# -*- coding: utf-8 -*-

from flask import Blueprint

from . import route

bp = Blueprint('base', __name__)


@route(bp, '/')
def api():
    """
    Base API call that returns name of service.

    @param None
    @return: json detailing the name of the service
    """
    return 'fogspoon'
