# -*- coding: utf-8 -*-
"""
bootstrap_db.py

This file takes the CSV file detailing filming locations in SF and loads it
into a dict, massages and normalizes the location information, uses the GeoPy
module to get latitude and longitude information, then saves that information
into a database via fogspoon's models.
"""

from __future__ import print_function

import argparse
import csv
import geopy
import logging

from fogspoon.api import create_app
from fogspoon.core import db
from fogspoon.services import films, locations, geo_locs

LOGGING_FORMAT = u'\033[1;36m%(levelname)s:\033[0;37m %(message)s'
logging.basicConfig(format=LOGGING_FORMAT,
                    level=logging.DEBUG)
logging.basicConfig(format=LOGGING_FORMAT,
                    level=logging.ERROR)
logging.getLogger('geopy').setLevel(logging.DEBUG)


class GeoLoc(object):
    """
    Given a Location Description, do a best effort to get a lat-lon pair
    leveraging the GeoPy library.
    """
    default_lat_lon = (37.77928, -122.41922)  # TODO use better location; SF City Hall for now

    def __init__(self, loc_string=None):
        self.raw_loc_string = loc_string
        self.location = None
        self.service = ''

        self.geolocators = {
            'geocoderdotus': {},
            #'googlev3': {'api_key':''},  # Requires API Key
        }

        self.log = logging.getLogger()

    @property
    def lat_lon(self):
        for s in self.geolocators.keys():
            if self.geolocator_results.get(s):
                return (self.geolocator_results.get(s).latitude,
                        self.geolocator_results.get(s).longitude)
            return self.default_lat_lon

    @property
    def results_to_dict(self):
        results = dict()
        if self.location:
            results.update({'service': self.service,
                            'location': self.raw_loc_string})
            results.update(dict((k, str(getattr(self.location, k))) for k in [
                'altitude',
                'latitude',
                'longitude',
                'raw']))
        return results

    def process(self):
        for geolocator, kwargs in self.geolocators.iteritems():
            try:
                self.location = None
                geo_service = geopy.geocoders.get_geocoder_for_service(geolocator)(**kwargs)
                location = geo_service.geocode(self.raw_loc_string)
                if location:
                    self.location = location
                    self.service = geolocator
                    self.log.info(u'service {}: {}: {})'.format(
                        geolocator,
                        self.raw_loc_string,
                        self.location))
                else:
                    self.log.warn(u'service {} no location : {}: None'.format(
                        geolocator,
                        self.raw_loc_string)
                    )
            except geopy.exc.GeocoderTimedOut:
                self.log.warn(u'service {} Timeout: {}: None'.format(
                    geolocator,
                    self.raw_loc_string)
                )
            except Exception as detail:
                self.log.exception(u'service "{geolocator}" Exception with raw_loc_string "{raw_loc_string}" \n{detail}'.format(
                    geolocator=geolocator,
                    raw_loc_string=self.raw_loc_string,
                    detail=detail))


class SFGeoLoc(GeoLoc):
    """
    San Francisco-specific GeoLocator class.
    """
    default_lat_lon = (37.77928, -122.41922)  # SF City Hall
    default_lat_lon = None

    def __init__(self, loc_string=None):
        if loc_string:
            super(SFGeoLoc, self).__init__(u'{}, San Francisco, CA'.format(loc_string))
        else:
            super(SFGeoLoc, self).__init__()


class CSVToDict(object):
    """
    Convert a CSV file to a list of dicts
    Assumes that the first line of the file details the keys and subsequent lines
    are values.
    """
    def __init__(self, filename):
        with open(filename, 'rU') as input_file:
            fieldnames = []
            dict_keys = input_file.readline()
            split_keys = dict_keys.rstrip(u'\r\n').split(u',')
            for key in split_keys:
                if u' ' in key:
                    edited_key = key.replace(u' ', u'_').lower()
                    fieldnames.append(edited_key)
                else:
                    edited_key = key.lower()
                    fieldnames.append(edited_key)
            fieldnames = tuple(fieldnames)
            csvInstance = csv.DictReader(input_file, fieldnames=fieldnames)
            self.data = [dict((k, unicode(v, 'utf-8')) for k, v in row.iteritems()) for row in csvInstance]


def bootstrap_db(bootstrap_csv_file):
    app = create_app()
    with app.app_context():
        db.create_all()

        location_entries = CSVToDict(bootstrap_csv_file).data
        for location_entry in location_entries:
            film_args = {'title': location_entry.get('title'),
                         'release_year': location_entry.get('release_year')}
            film = films.first_or_create(**film_args)
            # TODO Add director, writer, producer and actors

            place_name = location_entry.get('locations')
            if place_name:
                location_args = {'place_name': place_name,
                                 'fun_fact': location_entry.get('fun_facts')}
                try:
                    location = locations.first_or_create(**location_args)
                except Exception as detail:
                    logging.exception(u'location: {}\n{}'.format(location_args, detail))
                    raise Exception("boop")
                if not location in film.locations:
                    films.add_location(film, location)
                    logging.info(u'adding loc {loc} for {title}({year})'.format(
                        loc=location.place_name,
                        title=film.title,
                        year=film.release_year,
                    ))

                geo_loc_q = SFGeoLoc(place_name)
                geo_loc = geo_locs.first(**{'location': geo_loc_q.raw_loc_string})
                if not geo_loc:
                    logging.info(u'geo querying for {}'.format(place_name))
                    geo_loc_q.process()
                    geo_loc_args = geo_loc_q.results_to_dict
                    if geo_loc_args:
                        geo_loc = geo_locs.first_or_create(**geo_loc_args)
                    else:
                        # Something weird happened with the query...
                        geo_loc = None
                if geo_loc:
                    if not geo_loc in location.geo_locs:
                        locations.add_geo_loc(location, geo_loc)
                        logging.info(u'added {geo} for {title}({year}) - {loc}'.format(
                            geo=geo_loc.location,
                            loc=location.place_name,
                            title=film.title,
                            year=film.release_year,
                        ))
                    else:
                        logging.info(u'have {geo} for {title}({year}) - {loc}'.format(
                            geo=geo_loc.location,
                            loc=location.place_name,
                            title=film.title,
                            year=film.release_year,
                        ))
                else:
                    logging.error(u'failed geo query for {geo} while doing {title}({year}) - {loc}'.format(
                        geo=place_name,
                        loc=location.place_name,
                        title=film.title,
                        year=film.release_year,
                    ))


parser = argparse.ArgumentParser()
parser.add_argument('csv_filename', help='Name of the csv file you want to convert to json')
args = parser.parse_args()

if __name__ == '__main__':
    bootstrap_db(args.csv_filename)
