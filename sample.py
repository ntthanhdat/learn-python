from flask import Flask, url_for, render_template, request
from markupsafe import escape
from jinja2 import Template

app = Flask("web1")

@app.route('/')
def index():
    return 'index'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

