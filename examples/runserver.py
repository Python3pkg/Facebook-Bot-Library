"""
This script runs the FlaskFBBot application using a development server.
"""

from os import environ
import flask_app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    flask_app.app.run(HOST, PORT)
