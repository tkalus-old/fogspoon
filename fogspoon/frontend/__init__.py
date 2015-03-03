# -*- coding: utf-8 -*-

from functools import wraps

from .. import factory


def create_app(settings_override=None):
    """Returns the Fogspoon frontpage  application instance"""
    app = factory.create_app(__name__, __path__, settings_override)
    return app


def route(bp, *args, **kwargs):
    """
    decorator that does blueprint fun; parity with fogspoon api
    """
    def decorator(f):
        @bp.route(*args, **kwargs)
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return f

    return decorator
