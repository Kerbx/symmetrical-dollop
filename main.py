import flask


app = flask.Flask(__name__)
        

@app.route('/', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'POST':
        return flask.redirect('/search')

    return flask.render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return flask.render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    return flask.render_template('register.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return flask.render_template('profile.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if flask.request.method == 'POST':
        return flask.redirect('/booking')

    return flask.render_template('search.html')


@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if flask.request.method == 'POST':
        return flask.redirect('/booking_management')

    return flask.render_template('booking.html')


@app.route('/booking_management', methods=['GET', 'POST'])
def booking_management():
    if flask.request.method == 'POST':
        return flask.redirect('/seat')

    return flask.render_template('booking_management.html')


@app.route('/seat', methods=['GET', 'POST'])
def seat():
    return flask.render_template('seat.html')


@app.route('/return', methods=['GET', 'POST'])
def back():
    return flask.redirect('/')


@app.route('/news', methods=['GET', 'POST'])
def news():
    return flask.redirect('/')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return flask.redirect('/')


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    return flask.redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)