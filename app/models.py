from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    # ID used by flask-login for tracking current user
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    purchases = db.Column()

class Listing(db.Model):
    productID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(1000))
    brand = db.Column(db.String(100))
    price = db.Column(db.Float)
    image = db.Column(db.String(100))
    stock = db.Column(db.Integer)
class history(db.model):
    id = db.Column(db.Integer,primary_key=True)
    date = db.Column(db.String(10))
    