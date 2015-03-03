# -*- coding: utf-8 -*-

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
