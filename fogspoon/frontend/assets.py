# -*- coding: utf-8 -*-

from flask_assets import Environment

css_cdnjs = ('https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.3/leaflet.css',
             'https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css',
             'https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.11.2/jquery-ui.min.css',
             'https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.11.2/jquery-ui.structure.min.css',
             'https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.11.2/jquery-ui.theme.min.css',
             'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.3.0/css/font-awesome.css')

css_main = ('css/fogspoon.css',)

js_cdnjs = ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.11.2/jquery-ui.js',
            'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.3/leaflet.js',
            'https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.min.js',)

js_main = ('js/main.js',)


def init_app(app):
    webassets = Environment(app)
    webassets.register('css', *(css_cdnjs + css_main))
    webassets.register('js', *(js_cdnjs + js_main))
    webassets.manifest = 'cache' if not app.debug else False
    webassets.cache = not app.debug
    webassets.debug = app.debug
