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


@app.route("/states_list", strict_slashes=False)
def states_list():
    """A route to /states_list"""
    data = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template("7-states_list.html", states=data)


"""run the Flask app """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
