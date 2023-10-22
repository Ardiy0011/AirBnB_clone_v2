#!/usr/bin/python3
"""Create a Flask application"""
from flask import Flask, render_template


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


"""Define the route for "/number/<n>" with
strict_slashes=False. only if n is a number"""


@app.route('/number/<n>', strict_slashes=False)
def number_route(n):
    if n.isdigit():
        return f'{n} is a number'
    else:
        return 'Not Found', 404


"""Define the route for "/number_template/<n>" with
strict_slashes=False. only if n is a number render
template"""


@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    if n.isdigit():
        return render_template('5-number.html', n=n)
    else:
        return 'Not Found', 404


"""Define the route for "/number_template/<n>" with
strict_slashes=False. only if n is a number render
template.odd or even"""


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_oddoreven(n):
    return render_template('6-number_odd_or_even',
                           n=n,
                           oe="even" if n % 2 == 0 else "odd")


"""run the Flask app """
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
