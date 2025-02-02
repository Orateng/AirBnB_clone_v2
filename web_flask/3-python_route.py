#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB!'."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """Displays 'C' followed by the value of <text>."""
    formatted_text = text.replace('_', ' ')
    return "C {}".format(formatted_text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text):
    """
    Displays 'Python' followed by the value of <text>.
    Replaces any underscores in <text> with slashes.
    """
    formatted_text = text.replace('_', ' ')
    return "Python {}".format(formatted_text)


if __name__ == "__main__":
    """Start the Flask development server"""
    app.run(host='0.0.0.0', port=5000)
