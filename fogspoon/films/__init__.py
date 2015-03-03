# -*- coding: utf-8 -*-

from ..core import Service, FogspoonError
from .models import Film


class FilmsService(Service):
    __model__ = Film
