from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////users.sqlte3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)
class users(db.Model):
    _id=db.Column("id", db.Integer, primary_key=True)
    name=db.Column("name", db.String(100))
    email=db.Column("email", db.String(100))

    def __init__(self, name, email):
        self.name =name
        self.email=email
db.create_all()