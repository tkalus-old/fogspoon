# -*- coding: utf-8 -*-

import simplejson as json

from ..factories import LocationFactory
from . import FogspoonApiTestCase


class LocationApiTestCase(FogspoonApiTestCase):

    def _create_fixtures(self):
        super(LocationApiTestCase, self)._create_fixtures()
        self.location = LocationFactory()

    def test_get_all_locs(self):
        r = self.jget('/locations')
        self.assertOkJson(r)
        actual_data = json.loads(r.data)
        self.assertEqual(1, len(actual_data))

    def test_get_loc(self):
        r = self.jget('/location/%s' % self.location.id)
        self.assertOkJson(r)
        actual_data = json.loads(r.data)

        expected = self.location.id
        actual = actual_data['data']['id']
        self.assertEqual(expected, actual)
