# -*- coding: utf-8 -*-

import bottle
import os


bottle.BaseRequest.MEMFILE_MAX = 1024 * 1024
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static').replace('\\', '/')

myapp = bottle.Bottle()

@myapp.route('/')
def home():
    return 'Hello, world!'


@myapp.error(403)
def mistake403(code):
    return 'There is a mistake in your url!'


@myapp.error(405)
def mistake405(code):
    return 'There is a mistake in your url!'


@myapp.error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'


if __name__ == '__main__':
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static').replace('\\', '/')
    HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '9999'))
    except ValueError:
        PORT = 9999

    myapp.run(reloader=True, host=HOST, port=PORT)
