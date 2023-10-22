#!/usr/bin/python3
"""Create a Flask application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_session(exception):
    """ fixing the  erro around all"""
    storage.close()


@app.route('/cities_by_states')
def cities_by_states():
    """fixing the error areound all"""
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('cities_by_states.html', states=sorted_states)


"""pycode starting at rect"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
