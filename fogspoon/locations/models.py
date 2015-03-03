# -*- coding: utf-8 -*-

from ..core import db
from ..helpers import JsonSerializer


class Location(JsonSerializer, db.Model):
    __tablename__ = 'locations'
    __json_hidden__ = ['films']

    id = db.Column(db.Integer(), primary_key=True)
    place_name = db.Column(db.String(255, convert_unicode=True))
    fun_fact = db.Column(db.String(255, convert_unicode=True))
