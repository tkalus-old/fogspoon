# -*- coding: utf-8 -*-

from ..core import db
from ..helpers import JsonSerializer


class Film(JsonSerializer, db.Model):
    __tablename__ = 'films'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255, convert_unicode=True))
    release_year = db.Column(db.Integer())
