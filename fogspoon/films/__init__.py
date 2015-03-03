# -*- coding: utf-8 -*-

from ..core import Service, FogspoonError
from .models import Film


class FilmsService(Service):
    __model__ = Film

    def add_location(self, film, location):
        if location in film.locations:
            raise FogspoonError(u'Location exists')
        film.locations.append(location)
        return self.save(film)
