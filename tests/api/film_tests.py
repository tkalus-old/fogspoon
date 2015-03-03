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
        self.assertEqual(1, len(actual_data))

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