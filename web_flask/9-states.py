#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown_app_context(exception):
    """Closes the storage on teardown."""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """Displays an HTML page with a list of all States."""
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", states=states)
    return render_template("9-states.html")


if __name__ == "__main__":
    """Start the Flask development server"""
    app.run(host="0.0.0.0", port=5000)
