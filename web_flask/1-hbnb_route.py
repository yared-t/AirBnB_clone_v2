#!/usr/bin/python3
<<<<<<< HEAD
"""Module - script that starts a Flask web application"""
from flask import Flask
=======
# Author: MikiasHailu
""" This will to start a Flask web application with 2 commands """

from flask import Flask


>>>>>>> 73a4f5def11930c5bfe7beada05b368a94622a85
app = Flask(__name__)


@app.route('/', strict_slashes=False)
<<<<<<< HEAD
def hello_hbnb():
    """Handles the root url"""
=======
def hello_world():
    """ Returns some text. """
>>>>>>> 73a4f5def11930c5bfe7beada05b368a94622a85
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
<<<<<<< HEAD
def hbnb():
    """Handles hbnb route"""
    return 'HBNB'


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
=======
def hello():
    """ Return other text. """
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 73a4f5def11930c5bfe7beada05b368a94622a85
