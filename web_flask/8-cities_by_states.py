#!/usr/bin/python3
"""Create a Flask application"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


"""run the Flask app """


@app.teardown_appcontext
def close_session(exception):
    """Closes SQLAlchemy session after each request."""
    storage.close()


"""run the Flask app """


@app.route("/cities_by_states", strict_slashes=False)
def cities_in_states():
    """A route to /states_list"""
    data = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template("8-cities_by_states.html", states=data)


"""run the Flask app """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
