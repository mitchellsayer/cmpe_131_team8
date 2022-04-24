from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms import BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
	user_name = StringField('UserName', validators = [DataRequired()])
	password = PasswordField('Password', validators = [DataRequired()])
	# remember = BooleanField("Stay Logged In")
	submit = SubmitField('Log In')
