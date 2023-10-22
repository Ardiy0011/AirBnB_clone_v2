#!/usr/bin/python3
""" A route to /states_list """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db(exception):
    storage.close()


@app.route('/states_list')
def states_list():
    """retrieve all states in order"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)

    return render_template('7-states_list.html',
                           sorted_states=sorted_states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
