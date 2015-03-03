# -*- coding: utf-8 -*-

from .films import FilmsService
from .locations import LocationsService

#: An instance of the :class:`FilmsService` class
films = FilmsService()

#: An instance of the :class:`LocationsService` class
locations = LocationsService()
