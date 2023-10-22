from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def teardown_session(exception):
    storage.close()

@app.route('/cities_by_states')
def cities_by_states():
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('cities_by_states.html', states=sorted_states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
