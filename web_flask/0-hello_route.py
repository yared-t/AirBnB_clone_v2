#!/usr/bin/python3
<<<<<<< HEAD
"""Module - script that starts a Flask web application"""
from flask import Flask
=======
# Author: mikiasHailu
"""This module will Script a flask app"""

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


if __name__ == '__main__':
<<<<<<< HEAD
    app.run("0.0.0.0", 5000)
=======
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 73a4f5def11930c5bfe7beada05b368a94622a85
