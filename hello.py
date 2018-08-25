from flask import Flask
from flask import request
from flask import make_response, redirect, abort

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.header.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)

# a more traditional way to set up the application routes
# def index():
#   return '<h1>Hello World!</h1>'

# app.add_url('/', 'index', index)

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)


@app.route('/reponse')
def reponse_1():
    return '<h1>Bad Request</h1>', 400


@app.route('/make_response')
def make_response_eg():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '43')
    return response

@app.route('/redirect')
def redirect_eg():
    return redirect('http://www.baidu.com')


@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, {}</h1>'.format(user.name)

