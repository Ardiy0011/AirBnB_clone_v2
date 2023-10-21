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


"""Define the route for "/c/<text>" with 
strict_slashes=False"""


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text = text.replace('_', ' ')
    return f'C {text}'


"""Define the route for "/python/<text>" with 
strict_slashes=False. if no text is passed default 
text of is cool is returned"""


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    text = text.replace('_', ' ')
    return f'Python {text}'


"""run the Flask app """
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
