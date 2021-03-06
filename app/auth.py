from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import db
import re

# Use blueprints to group auth routes together
auth = Blueprint('auth', __name__)

def validate_email_adress(email):
    validation_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    if(re.fullmatch(validation_regex, email)):
        print("Valid Email")
        return True

    print("Invalid Email")
    return False

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = request.form.get('remember')

    # Check if user exists
    user = User.query.filter_by(email=email).first()

    # Check supplied password against hash in db
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    # User login successful
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    # Parse form
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # Query will return None if user doesnt exist
    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    if(not validate_email_adress(email)):
        flash('Invalid email address format')
        return redirect(url_for('auth.signup'))

    # Use SHA 256 to hash password & avoid storing in plaintext
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # Save new user in db
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    # Logout user and return to homepage
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/delete')
@login_required
def delete():#pass current user into delete function
    #User clicks "Delete Account" option which signs them out and redirects them to homepage
    userId=current_user.id
    user = User.query.get(userId) #getting row which has primary key of user (user id) from database
    logout_user()
    print(user)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('main.index'))
    