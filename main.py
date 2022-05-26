import flask


app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/login')
def login():
    return flask.render_template('login.html')


@app.route('/register')
def register():
    return flask.render_template('register.html')


@app.route('/profile')
def profile():
    return flask.render_template('profile.html')


@app.route('/search')
def search():
    return flask.render_template('search.html')


@app.route('/booking')
def booking():
    return flask.render_template('booking.html')


@app.route('/booking_management')
def booking_management():
    return flask.render_template('booking_management.html')


@app.route('/seat')
def route():
    return flask.render_template('seat.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)