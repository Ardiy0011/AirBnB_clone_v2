#!/usr/bin/python3
"""Create a Flask application"""
from flask import Flask, render_template, jsonify
from models import storage
from models.state import State
from operator import attrgetter


app = Flask(__name__)


@app.route('/api/data', methods=['GET'])
def get_data():
    """retireve all objects from db"""
    data = storage.all()
    return jsonify(data)


@app.teardown_appcontext
def close_session(exception):
    """Closes SQLAlchemy session after each request."""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """retrieve all states in order"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=attrgetter('name'))

    return render_template('7-states_list.html',
                           sorted_states=sorted_states)


"""run the Flask app """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
