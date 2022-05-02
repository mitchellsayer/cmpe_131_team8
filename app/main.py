from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/listings')
@login_required
def listings():
    return render_template('listings.html')

@main.route('/new_listing')
@login_required
def new_listing():
    return render_template('new_listing.html')

@main.route('/purchase')
@login_required
def purchase():
    #compute initial sales tax here
    #pass into render template
    return render_template('purchase.html')

@main.route('/purchase', methods=['POST'])
@login_required
def purchase_post():
    product_ID= request.form.get('product_ID')
    return render_template()
