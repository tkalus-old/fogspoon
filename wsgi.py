# -*- coding: utf-8 -*-

from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from fogspoon import api, frontend

LISTEN_PORT = 8080

application = DispatcherMiddleware(frontend.create_app(), {
    '/api': api.create_app()
})

if __name__ == '__main__':
    run_simple('127.0.0.1', LISTEN_PORT, application, use_reloader=True, use_debugger=True)
