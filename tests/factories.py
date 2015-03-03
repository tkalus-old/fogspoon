# -*- coding: utf-8 -*-

from factory import Sequence, LazyAttribute
from factory.alchemy import SQLAlchemyModelFactory

from fogspoon.core import db
from fogspoon.films import Film
from fogspoon.locations import Location


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

    locations = LazyAttribute(lambda _: [LocationFactory()])


class LocationFactory(BaseFactory):
    class Meta:
        model = Location

    id = Sequence(lambda n: n)
    place_name = Sequence(lambda n: '{0} Market St.'.format(n))
    fun_fact = Sequence(lambda n: '{0} Market St. was the place where Beta Film {1} was also shot'.format(n, n))
