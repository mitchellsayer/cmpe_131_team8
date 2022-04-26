from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    # ID used by flask-login for tracking current user
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
