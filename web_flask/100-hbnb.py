#!/usr/bin/python3
"""Create a Flask application"""
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.place import Place
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def dispose(exception):
    """ Exit SQLAlchemy session """
    storage.close()


@app.route('/hbnb')
def hbnb_filters():
    """route to filters"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    data = {
        'states': list(states.values()),
        'amenities': list(amenities.values()),
        'places': list(places.values())
    }
    return render_template('100-hbnb.html', **data)


"""run the Flask app """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
