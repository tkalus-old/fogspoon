# -*- coding: utf-8 -*-

import simplejson as json

from ..factories import FilmFactory, LocationFactory
from . import FogspoonApiTestCase


class FilmApiTestCase(FogspoonApiTestCase):

    def _create_fixtures(self):
        super(FilmApiTestCase, self)._create_fixtures()
        self.location0 = LocationFactory()
        self.location1 = LocationFactory()
        self.film = FilmFactory(locations=[self.location0, self.location1])

    def test_get_all_films(self):
        r = self.jget('/films')
        self.assertOkJson(r)
        actual_data = json.loads(r.data)
        # expecting one film
        self.assertEqual(1, len(actual_data['data']))

    def test_query_lc_film(self):
        query = self.film.title.split(' ')[0].lower()
        r = self.jget('/films?q=%s' % (query))
        self.assertOkJson(r)
        actual_data = json.loads(r.data)
        # expecting one film
        self.assertEqual(1, len(actual_data['data']))

    def test_query_uc_film(self):
        query = self.film.title.split(' ')[0].upper()
        r = self.jget('/films?q=%s' % (query))
        self.assertOkJson(r)
        actual_data = json.loads(r.data)
        # expecting one films
        self.assertEqual(1, len(actual_data['data']))

    def test_query_no_film(self):
        # No films in test factory contain 'Alpha'
        query = 'Alpha'
        r = self.jget('/films?q=%s' % (query))
        self.assertOkJson(r)
        actual_data = json.loads(r.data)
        # expecting no films
        self.assertEqual(0, len(actual_data['data']))

    def test_get_film(self):
        r = self.jget('/film/%s' % self.film.id)
        self.assertOkJson(r)
        actual_data = json.loads(r.data)
        expected = self.film.id
        actual = actual_data['data']['id']
        self.assertEqual(expected, actual)

    def test_get_film_check_locations(self):
        r = self.jget('/film/%s' % self.film.id)
        self.assertOkJson(r)
        actual_data = json.loads(r.data)

        expected = self.location0.id
        actual = actual_data['data']['locations'][0]['id']
        self.assertEqual(expected, actual)

        expected = self.location1.id
        actual = actual_data['data']['locations'][1]['id']
        self.assertEqual(expected, actual)

    def test_get_film_check_geo_json(self):
        r = self.jget('/film/%s?format=geo_json' % self.film.id)
        self.assertOkJson(r)
        actual_data = json.loads(r.data)

        self.assertEqual('FeatureCollection', actual_data['data']['type'])
        self.assertEqual('Feature', actual_data['data']['features'][0]['type'])
        self.assertEqual('MultiPoint', actual_data['data']['features'][0]['geometry']['type'])
        self.assertEqual(1, len(actual_data['data']['features'][0]['geometry']['coordinates']))
