# -*- coding: utf-8 -*-

from ..core import Service, FogspoonError
from .models import Location, GeoLoc


class LocationsService(Service):
    __model__ = Location

    def add_geo_loc(self, location, geo_loc):
        if geo_loc in location.geo_locs:
            raise FogspoonError(u'Location exists')
        location.geo_locs.append(geo_loc)
        return self.save(location)


class GeoLocsService(Service):
    __model__ = GeoLoc
