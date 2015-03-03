# -*- coding: utf-8 -*-

from .. import FogspoonAppTestCase, settings
from fogspoon.api import create_app


class FogspoonApiTestCase(FogspoonAppTestCase):

    def _create_app(self):
        return create_app(settings)
