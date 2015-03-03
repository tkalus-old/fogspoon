# -*- coding: utf-8 -*-

import simplejson as json

from ..factories import FilmFactory
from . import FogspoonApiTestCase


class FilmApiTestCase(FogspoonApiTestCase):

    def _create_fixtures(self):
        super(FilmApiTestCase, self)._create_fixtures()
        self.film = FilmFactory()

    def test_get_all_films(self):
        r = self.jget(u'/films')
        self.assertOkJson(r)
        actual_data = json.loads(r.data)
        # expecting one film
        self.assertEqual(1, len(actual_data))

    def test_get_film(self):
        r = self.jget(u'/film/{}'.format(self.film.id))
        self.assertOkJson(r)
        actual_data = json.loads(r.data)
        expected = self.film.id
        actual = actual_data['data']['id']
        self.assertEqual(expected, actual)
