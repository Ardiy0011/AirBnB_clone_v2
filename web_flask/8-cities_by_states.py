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


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('cities_by_states.html', states=sorted_states)


"""run the Flask app """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
