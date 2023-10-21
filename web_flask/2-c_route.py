#!/usr/bin/python3
<<<<<<< HEAD
"""Module - script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Handles the root url"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Handles hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Handles /c/<text> route"""
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
=======
# Author: MikiasHailu
""" This will Script to start a flask web application with 3 view functions """

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """ Returns some text. """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello():
    """ Return other text. """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """ This replace text with variable. """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 73a4f5def11930c5bfe7beada05b368a94622a85
