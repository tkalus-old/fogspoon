# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

from . import route

bp = Blueprint('map', __name__)


@route(bp, '/')
def index():
    """Returns the map interface."""
    return render_template('map.html')

@route(bp, '/fogspoon')
def fogspoon():
    """
    Base API call that returns name of service.

    @param None
    @return: pre-wrapped string containing ascii-art-esque name of service
    """
    return '''<pre>
    ____
   / __/___  ____ __________  ____  ____  ____
  / /_/ __ \/ __ `/ ___/ __ \/ __ \/ __ \/ __ \\
 / __/ /_/ / /_/ (__  ) /_/ / /_/ / /_/ / / / /
/_/  \____/\__, /____/ .___/\____/\____/_/ /_/
          /____/    /_/`
</pre>
'''
