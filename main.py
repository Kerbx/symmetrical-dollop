import flask


app = flask.Flask(__name__)
data = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    global data
    if flask.request.method == 'POST':
        data = {'dateTo': flask.request.form.get('dateTo'),
                'dateFrom': flask.request.form.get('dateFrom'),
                'to': flask.request.form.get('to'),
                'from': flask.request.form.get('from'),
                'amount': int(flask.request.form.get('amount'))}
        return flask.redirect('/search')
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


@app.route('/search', methods=['GET', 'POST'])
def search():
    global data

    amount = 14 + data['amount']
    if data['amount'] >= 22:
        amount = 100
    if 22 > data['amount'] >= 11:
        amount = 50
    if 11 > data['amount'] >= 6:
        amount = 25
    if data['amount'] < 6:
        amount = 0

    if flask.request.method == 'POST':
        return flask.redirect('/booking')

    return flask.render_template('search.html', to=data['to'], _from=data['from'],
                                 dateTo=data['dateTo'], dateFrom=data['dateFrom'],
                                 amount=amount)


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