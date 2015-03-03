# -*- coding: utf-8 -*-

from flask import Blueprint

from . import route

bp = Blueprint('front', __name__)

@route(bp, '/')
def index():
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
