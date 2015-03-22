# -*- coding: utf-8 -*-

from geojson import FeatureCollection

from ..core import db
from ..helpers import JsonSerializer


films_locations = db.Table(
    'films_locations',
    db.Column('film_id', db.Integer(), db.ForeignKey('films.id')),
    db.Column('location_id', db.Integer(), db.ForeignKey('locations.id')),
)


class Film(JsonSerializer, db.Model):
    __tablename__ = 'films'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255, convert_unicode=True))
    release_year = db.Column(db.Integer())

    locations = db.relationship('Location', secondary=films_locations,
                                backref=db.backref('films', lazy='dynamic'))

    @property
    def display_title(self):
        return u'{title} ({year})'.format(title=self.title, year=self.release_year)

    @property
    def to_geo_json(self):
        """Return GeoJSON objects.
           Could have also used the GeoAlchemy module, but it seemed heavy...
           TODO Investigate a way to hide this in a base class, similar to JsonSerializer
        """
        if self.locations:
            properties = dict([(u'id', self.id),
                               (u'title', self.display_title)])
            return FeatureCollection(
                filter(None,[l.to_geo_json(self.display_title) for l in self.locations]),
                properties=properties)
        return None
