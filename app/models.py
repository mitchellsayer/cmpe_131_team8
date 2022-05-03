from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    # ID used by flask-login for tracking current user
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    listings=db.relationship('Listing', backref='seller', lazy='dynamic')

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    #image?
    stock = db.Column(db.Integer)
    desc = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

