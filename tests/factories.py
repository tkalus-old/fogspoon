# -*- coding: utf-8 -*-

from factory import Sequence
from factory.alchemy import SQLAlchemyModelFactory

from fogspoon.core import db
from fogspoon.films import Film


class BaseFactory(SQLAlchemyModelFactory):
        class Meta:
            abstract = True
            sqlalchemy_session = db.session


class FilmFactory(BaseFactory):
    class Meta:
        model = Film

    id = Sequence(lambda n: n)
    title = Sequence(lambda n: u'Gamma Film {0}'.format(n))
    release_year = Sequence(lambda n: 1950 + n)
