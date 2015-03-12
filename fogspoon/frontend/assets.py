# -*- coding: utf-8 -*-

from flask_assets import Environment

css_cdnjs = ('https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.3/leaflet.css',
             'https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css',
             'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.3.0/css/font-awesome.css')

css_vendor = ('css/backbone.autocomplete-1.0.2.css',)

css_main = ('css/fogspoon.css',)

js_cdnjs = ('http://cdnjs.cloudflare.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.8.2/underscore-min.js',
            'http://cdnjs.cloudflare.com/ajax/libs/backbone.js/1.1.2/backbone-min.js',
            'http://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.3/leaflet.js',
            'http://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.min.js',)

js_vendor = ('js/vendor/backbone.autocomplete-1.0.2.js',)

js_main = ('js/main.js',)


def init_app(app):
    webassets = Environment(app)
    webassets.register('css', *(css_cdnjs + css_vendor + css_main))
    webassets.register('js', *(js_cdnjs + js_vendor + js_main))
    webassets.manifest = 'cache' if not app.debug else False
    webassets.cache = not app.debug
    webassets.debug = app.debug
