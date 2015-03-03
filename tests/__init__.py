# -*- coding: utf-8 -*-

from unittest import TestCase

from fogspoon.core import db

from .utils import FlaskTestCaseMixin


class FogspoonTestCase(TestCase):
    pass


class FogspoonAppTestCase(FlaskTestCaseMixin, FogspoonTestCase):

    def _create_app(self):
        raise NotImplementedError

    def _create_fixtures(self):
        pass

    def setUp(self):
        super(FogspoonAppTestCase, self).setUp()
        self.app = self._create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self._create_fixtures()

    def tearDown(self):
        super(FogspoonAppTestCase, self).tearDown()
        db.drop_all()
        self.app_context.pop()
