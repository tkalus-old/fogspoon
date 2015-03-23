# fogspoon

[![Build Status](https://travis-ci.org/tkalus/fogspoon.svg)](https://travis-ci.org/tkalus/fogspoon)

[fogspoon.com](http://fogspoon.com)

Queryable Service that shows on a map where movies have been filmed in San Francisco.

## The Impetus

After being solicited for samples of Python code that I’ve worked on, I found that I didn’t have much in the way I could show as nearly all the code I’d worked on was proprietary.

- Show my strengths in Backend/API
- Illustrate my moderate understanding of Frontend
- Produce something fun and useful.

## ToDo

- Leverage Google’s [Geocoding](https://developers.google.com/maps/documentation/geocoding/) and [Places](https://developers.google.com/places/documentation/) APIs to get better accuracy.
  - E.G. Blue Jasmine’s Marina Blvd from Leguna to Baker is a straight line and Ocean Beach at Lincoln is resolving to the City-Center
- Make the FE prettier... and less hackish.
- Do something with cookies so the map is only pre-populated on the “first visit”.

## How to Install or Deploy

#### Linux Server

```
$ git clone https://github.com/tkalus/fogspoon.git
$ cd fogspoon
$ pip install -r requirements.txt
$ python wsgi.py
```

## Implementation thoughts

- Start with a base Flask app from github (https://github.com/mattupstate/overholt)
  - Why reinvent the wheel
  - Should really cookiecutter that repo
- Don’t bother with an external database machine
  - Data set is very small and can likely be accessed via SQLAlchemy’s SQLite engine
  - Preprocess and checkin to git a SQLite database. Dataset doesn’t change often, so...
- Leverage wsgi, Flask, SQLAchemy.
  - Flask is pretty awesome
  - Haven’t used SQLAlchemy much, but shouldn’t be too bad.
- Leverage a geolocation module to translate address to lat/lon
