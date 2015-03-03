# -*- coding: utf-8 -*-

import simplejson as json

from ..factories import LocationFactory, GeoLocFactory
from . import FogspoonApiTestCase


class LocationApiTestCase(FogspoonApiTestCase):

    def _create_fixtures(self):
        super(LocationApiTestCase, self)._create_fixtures()
        self.location = LocationFactory()
        self.geo_loc = self.location.geo_locs[0]

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
        actual = actual_data.get('data', {}).get('id', None)
        self.assertEqual(expected, actual)

    def test_get_geo_loc(self):
        r = self.jget('/location/%s' % self.location.id)
        self.assertOkJson(r)
        actual_data = json.loads(r.data)

        expected = self.geo_loc.id
        actual = actual_data.get('data', {}).get('geo_locs', [])[0].get('id')
        self.assertEqual(expected, actual)
