#!/usr/bin/python3
"""Create a Flask application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def dispose(exception):
    """ Remove current session """
    storage.close()


@app.route('/states/')
@app.route('/states/<id>')
def states_and_state(id=None):
    """ Display list of all the states """
    if id:
        id = 'State.{}'.format(id)
    return render_template('9-states.html', states=storage.all(State), id=id)


"""run the Flask app """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
