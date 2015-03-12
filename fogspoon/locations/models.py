# -*- coding: utf-8 -*-

from geojson import Feature, LineString, MultiPoint

from ..core import db
from ..helpers import JsonSerializer

locations_geolocs = db.Table(
    'locations_geolocs',
    db.Column('location_id', db.Integer(), db.ForeignKey('locations.id')),
    db.Column('geo_loc_id', db.Integer(), db.ForeignKey('geo_locs.id')),
)

class Location(JsonSerializer, db.Model):
    __tablename__ = 'locations'
    __json_hidden__ = ['films']

    id = db.Column(db.Integer(), primary_key=True)
    place_name = db.Column(db.String(255, convert_unicode=True))
    fun_fact = db.Column(db.String(1024, convert_unicode=True))

    geo_locs = db.relationship('GeoLoc', secondary=locations_geolocs)

    def to_geo_json(self, film):
        if self.geo_locs:
            properties = dict([(u'film', film),
                               (u'place_name', self.place_name),
                               (u'fun_fact', self.fun_fact)])
            if len(self.geo_locs) > 1:
                geometry = LineString([g.lon_lat for g in self.geo_locs])
            else:
                geometry = MultiPoint([g.lon_lat for g in self.geo_locs])
            return Feature(geometry=geometry, id=self.id, properties=properties)
        return None


class GeoLoc(JsonSerializer, db.Model):
    __tablename__ = 'geo_locs'
    #__json_hidden__ = ['raw']

    id = db.Column(db.Integer(), primary_key=True)
    service = db.Column(db.String(16, convert_unicode=True))
    location = db.Column(db.String(255, convert_unicode=True))
    altitude = db.Column(db.Float())
    latitude = db.Column(db.Float())
    longitude = db.Column(db.Float())
    raw = db.Column(db.String(1024, convert_unicode=True))

    # Weridly, GeoJSON wants the coords in lon,lat format; x,y I guess?
    @property
    def lon_lat(self):
        return (self.longitude, self.latitude)

    @property
    def lat_lon(self):
        return (self.latitude, self.longitude)
