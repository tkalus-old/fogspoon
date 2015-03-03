# -*- coding: utf-8 -*-

from factory import Sequence, LazyAttribute
from factory.alchemy import SQLAlchemyModelFactory

from fogspoon.core import db
from fogspoon.films import Film
from fogspoon.locations import Location, GeoLoc


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
    place_name = Sequence(lambda n: u'{0} Market St.'.format(n))
    fun_fact = Sequence(lambda n: u'{0} Market St. was the place where Beta Film {1} was also shot'.format(n, n))

    geo_locs = LazyAttribute(lambda _: [GeoLocFactory()])

class GeoLocFactory(BaseFactory):
    class Meta:
        model = GeoLoc

    id = Sequence(lambda n: n)
    service = Sequence(lambda _: u'geothingy')
    service = Sequence(lambda n: u'Space! Deep Space {0}'.format(n))
    altitude = Sequence(lambda n: 0.0 + float(n))
    altitude = Sequence(lambda n: 0.0 + float(n))
    latitude = Sequence(lambda n: float(n*0.01) + 37.77928)
    latitude = Sequence(lambda n: float(n*0.01) + -122.41922)
    raw = Sequence(lambda n: u'Some raw payload from geothingy {0}'.format(n))
