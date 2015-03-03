# -*- coding: utf-8 -*-
"""
bootstrap_db.py

This file takes the CSV file detailing filming locations in SF and loads it
into SQLAlchemy
"""

from __future__ import print_function

import argparse
import csv
import logging

from fogspoon.api import create_app
from fogspoon.core import db
from fogspoon.services import films

LOGGING_FORMAT = u'\033[1;36m%(levelname)s:\033[0;37m %(message)s'
logging.basicConfig(format=LOGGING_FORMAT,
                    level=logging.DEBUG)


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
            #self.data = [row for row in csvInstance]
            self.data = [dict((k, unicode(v, 'utf-8')) for k, v in row.iteritems()) for row in csvInstance]


def bootstrap_db(bootstrap_csv_file):
    app = create_app()
    with app.app_context():
        db.create_all()

        location_entries = CSVToDict(bootstrap_csv_file).data
        for location_entry in location_entries:
            film_args = {'title': location_entry.get('title'),
                         'release_year': location_entry.get('release_year')}
            films.first_or_create(**film_args)
            # TODO Add director, writer, producer and actors


parser = argparse.ArgumentParser()
parser.add_argument('csv_filename', help='Name of the csv file you want to convert to json')
args = parser.parse_args()

if __name__ == '__main__':
    bootstrap_db(args.csv_filename)
