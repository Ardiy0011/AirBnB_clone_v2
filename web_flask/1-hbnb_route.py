#!/usr/bin/python3
"""Create a Flask application"""
from flask import Flask


app = Flask(__name__)

"""Define the route for the root URL ("/")
with strict_slashes=False"""


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


"""Define the route for the root URL ("/hbnb")
with strict_slashes=False"""


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


"""run the Flask app """
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
