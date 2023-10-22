#!/usr/bin/python3
"""Create a Flask application"""
from flask import Flask, render_template, jsonify
from models import storage
from models.state import State
from models.state import State
from operator import attrgetter
from models.city import City

app = Flask(__name__)


"""run the Flask app """


@app.teardown_appcontext
def close_session(exception):
    """Closes SQLAlchemy session after each request."""
    storage.close()


"""run the Flask app """


@app.route("/states_list", strict_slashes=False)
def states_list():
    """A route to /states_list"""
    data = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template("7-states_list.html", states=data)


@app.route("/cities_by_states", strict_slashes=False)
def citiesInStates():
    """A route to cities in states"""
    data = sorted(storage.all(City.state_id).values())
    return render_template("8-cities_by_states.html", cities=data)
"""run the Flask app """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
