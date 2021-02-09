from flask import Flask, url_for, render_template
from markupsafe import escape

app = Flask("web1")

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

