from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

base_dir = os.path.abspath(os.path.dirname(__file__))

myapp = Flask(__name__)

myapp.config.from_mapping(
	SECRET_KEY = "PICK ONE",
	SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(base_dir,
					 "app.db")
	)

db = SQLAlchemy(myapp)
login = LoginManager(myapp)
login.login_view = "Login"

from app import route
