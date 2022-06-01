import flask


app = flask.Flask(__name__)
data = {'dateTo': None,
        'dateFrom': None,
        'to': None,
        'from': None,
        'amount': 0}
        

@app.route('/', methods=['GET', 'POST'])
def index():
    global data
    if flask.request.method == 'POST':
        try:
            data = {'dateTo': flask.request.form.get('dateTo'),
                    'dateFrom': flask.request.form.get('dateFrom'),
                    'to': flask.request.form.get('to'),
                    'from': flask.request.form.get('from'),
                    'amount': int(flask.request.form.get('amount'))}
        except:
            pass
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

    data['amount'] = 14 + data['amount']
    if data['amount'] >= 22:
        data['amount'] = 100
    elif 22 > data['amount'] >= 11:
        data['amount'] = 50
    elif 11 > data['amount'] >= 6:
        data['amount'] = 25
    elif data['amount'] < 6:
        data['amount'] = 0

    if flask.request.method == 'POST':
        return flask.redirect('/booking')

    return flask.render_template('search.html', to=data['to'], _from=data['from'],
                                 dateTo=data['dateTo'], dateFrom=data['dateFrom'],
                                 amount=data['amount'])


@app.route('/booking', methods=['GET', 'POST'])
def booking():
    global data
    
    if flask.request.method == 'POST':
        return flask.redirect('/booking_management')

    return flask.render_template('booking.html', to=data['to'], _from=data['from'],
                                 dateTo=data['dateTo'], dateFrom=data['dateFrom'])


@app.route('/booking_management', methods=['GET', 'POST'])
def booking_management():
    global data
    
    if flask.request.method == 'POST':
        return flask.redirect('/seat')

    return flask.render_template('booking_management.html', to=data['to'], _from=data['from'],
                                 dateTo=data['dateTo'], dateFrom=data['dateFrom'],
                                 amount=data['amount'])


@app.route('/seat')
def seat():
    return flask.render_template('seat.html')


@app.route('/return')
def back():
    return flask.redirect('/')


@app.route('/news')
def news():
    return flask.redirect('/')


@app.route('/contact')
def contact():
    return flask.redirect('/')


@app.route('/feedback')
def feedback():
    return flask.redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)