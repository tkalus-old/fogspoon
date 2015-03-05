# -*- coding: utf-8 -*-

from flask_assets import Environment, Bundle


#: css bundle
css_all = Bundle("css/leaflet-0.7.css",
                 "css/fogspoon.css",
                 filters="cssmin", output="css/fogspoon.min.css")

#: vendor js bundle
js_vendor = Bundle("js/vendor/leaflet-0.7.js",
                   filters="jsmin", output="js/vendor.min.js")

#: application js bundle
#js_main = Bundle("coffee/*.coffee", filters="coffeescript", output="js/main.js")
js_main = Bundle("js/main.js", filters="jsmin", output="js/main.min.js")


def init_app(app):
    webassets = Environment(app)
    webassets.register('css_all', css_all)
    webassets.register('js_vendor', js_vendor)
    webassets.register('js_main', js_main)
    webassets.manifest = 'cache' if not app.debug else False
    webassets.cache = not app.debug
    webassets.debug = app.debug
