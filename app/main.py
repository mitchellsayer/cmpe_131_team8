from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

#Zander
@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, email=current_user.email)

@main.route('/listings')
@login_required
def listings():
    return render_template('listings.html')

#Zander
@main.route('/new_listing')
@login_required
def new_listing():
    return render_template('new_listing.html')

@main.route('/purchase')
@login_required
def purchase():
    return render_template('purchase.html')
