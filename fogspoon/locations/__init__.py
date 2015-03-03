# -*- coding: utf-8 -*-

from ..core import Service
from .models import Location


class LocationsService(Service):
    __model__ = Location
