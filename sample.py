from flask import Flask, url_for, render_template, request, redirect
from markupsafe import escape
from jinja2 import Template

# app = Flask("web1")
# @app.route('/')
# def index():
#     return  render_template('login.html')

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)

    
# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)


app = Flask(__name__)

@app.route('/')
def home():
    return "<h1> hello</h1>"
@app.route('/hello/')
@app.route('/hello/<name>')

def hello(name=None):
    return render_template("hello.html", name=name, r=3)

@app.route('/admin/')
def admin():
    return redirect(url_for("home"))

@app.route('/login/', methods=["POST", "GET"])
def login():
    if request.method=="POST":
        user=request.form['name']
        return redirect(url_for("hello", name=user))
    else:
        content =None
        return render_template("login.html", content="login") #render ra trang login.html, dua tren trang base.html

@app.route('/<usr>')
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__=="__main__":
    app.run()