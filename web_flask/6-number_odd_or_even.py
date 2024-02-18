#!/usr/bin/python3
'''Module containing script that starts a Flask web application.'''
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''Displays 'Hello HBNB!'. '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Displays "HBNB".'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''Displays C followed by the value of text.'''
    r_text = text.replace('_', ' ')
    return f'C {r_text}'


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    '''Displays python followed by the value of text.'''
    r_text = text.replace('_', ' ')
    return f'Python {r_text}'


@app.route('/number/<int:n>/', strict_slashes=False)
def is_number(n):
    ''' Display number if n is a number '''
    return f'{n} is a number'


@app.route('/number_template/<int:n>/', strict_slashes=False)
def is_number_template(n):
    ''' Display number in an html file if n is a number '''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>/', strict_slashes=False)
def is_number_odd_or_even(n):
    ''' Display number in an html file if n is an even or number '''
    val = 'even' if (n % 2 == 0) else 'odd'
    return render_template('6-number_odd_or_even.html', num=n, value=val)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
