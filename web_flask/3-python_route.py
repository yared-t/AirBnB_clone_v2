#!/usr/bin/python3
<<<<<<< HEAD
"""Module - script that starts a Flask web application"""
=======
# Author: MikiasHailu
""" This Sript that starts a Flask web application  """
>>>>>>> 73a4f5def11930c5bfe7beada05b368a94622a85
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
<<<<<<< HEAD
def hello_hbnb():
    """Handles the root url"""
    return 'Hello HBNB!'
=======
def hello_hbn():
    """ This function will return Hello HBNB! """
    return "Hello HBNB!"
>>>>>>> 73a4f5def11930c5bfe7beada05b368a94622a85


@app.route('/hbnb', strict_slashes=False)
def hbnb():
<<<<<<< HEAD
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


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
=======
    """ This function will return HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text_var(text):
    """ This function will display text variable passed in """
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def text_var_python(text="is cool"):
    """ This will function to display text variable, with default "is cool" """
    return "Python {}".format(text.replace("_", " "))
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
>>>>>>> 73a4f5def11930c5bfe7beada05b368a94622a85
