#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Closes the storage on teardown."""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with the states listed in alphabetical order."""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    """Start the Flask development server"""
    app.run(host="0.0.0.0", port=5000)
