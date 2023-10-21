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


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Handles /python/<text> route"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Handles /number/<n> route"""
=======
# Author: MikiasHailu
""" This will Add fourth view function that displays var only if is integer """

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
    """ This will replace text with variable. """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """ This will replace more text with another variable. """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def number_text(n):
    """ This will replace with int only if given int. """
    n = str(n)
>>>>>>> 73a4f5def11930c5bfe7beada05b368a94622a85
    return '{} is a number'.format(n)


if __name__ == '__main__':
<<<<<<< HEAD
    app.run("0.0.0.0", 5000)
=======
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 73a4f5def11930c5bfe7beada05b368a94622a85
