# fog-spoon

[![Build Status](https://drone.io/bitbucket.org/tkalus/fog-spoon/status.png)](https://drone.io/bitbucket.org/tkalus/fog-spoon/latest)

Queryable Service that shows on a map where movies have been filmed in San Francisco.

## The Impetus

After being solicited for samples of Python code that I’ve worked on, I found that I didn’t have much in the way I could show as nearly all the code I’d worked on was proprietary.

- Show my strengths in Backend/API
- Illustrate my moderate understanding of Frontend
- Produce something fun and useful.

## How to Install or Deploy

#### Linux Server

```
$ git clone https://bitbucket.org/tkalus/fog-spoon.git
$ cd fog-spoon
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
