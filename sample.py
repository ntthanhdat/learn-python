from flask import Flask, url_for, render_template, request, redirect, session
from markupsafe import escape
from jinja2 import Template
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
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

    

app = Flask(__name__)
app.secret_key = "hell"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite://users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False
app.permanent_session_lifetime=timedelta(hours=12)

db=SQLAlchemy(app)
class users(db.Model):
    _id=db.Column("id", db.Integer, primary_key=True)
    name=db.Column("name", db.String(100))
    email=db.Column("email", db.String(100))

    def __init__(self, name, email):
        self.name =name
        self.email=email

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
        username=request.form['name']
        session.permanent=True
        session["user"]=username
        return redirect(url_for("user"))
    else:
        content =None
        return render_template("login.html", content="login") #render ra trang login.html, dua tren trang base.html

@app.route('/logout')
def logout():
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))

@app.route('/user', methods=["POST","GET"])
def user():
    email=None
    if "user" in session:
        username = session["user"]
        if request.method=="POST":
            mail=request.form['email']
            session["email"]=email
        else:
            if "email" in session:
             session["email"]=email
        return render_template("user.html") 
        
    else:
        return redirect(url_for("login"))

if __name__=="__main__":
    app.run()