# -*- coding: utf-8 -*-

from . import FogspoonAppTestCase, settings
from fogspoon.frontend import create_app


class FogspoonFrontendTestCase(FogspoonAppTestCase):

    def test_front(self):
        r = self.get('/')
        self.assertOkHtml(r)
        self.assertEquals(1793, len(r.data))

    def _create_app(self):
        return create_app(settings)

    def setUp(self):
        super(FogspoonFrontendTestCase, self).setUp()
