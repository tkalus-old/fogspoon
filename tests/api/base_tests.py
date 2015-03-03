# -*- coding: utf-8 -*-

import simplejson as json

from . import FogspoonApiTestCase


class BaseApiTestCase(FogspoonApiTestCase):

    def test_api(self):
        r = self.get('/')
        self.assertOkJson(r)
        data = json.loads(r.data)
        self.assertEquals({'data': 'fogspoon'},
                          data)
