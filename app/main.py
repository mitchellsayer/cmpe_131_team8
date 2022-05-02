from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Listing
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
    # other_listings = Listing.query.filter(Listing.userID != current_user.id)
    test_listings = []
    for i in range(5):
        listing = Listing(
            productID = i,
            userID = current_user.id,
            name = "Test Item",
            description = "This is a test item description",
            price = 10.99,
            image = 'static/images/test_image.jpeg',
            stock = 5
        )
        test_listings.append(listing)

    return render_template('listings.html', listings = test_listings)

@main.route('/new_listing')
@login_required
def new_listing():
    return render_template('new_listing.html')

@main.route('/purchase/<productID>')
@login_required
def purchase(productID):
    print(str(productID))
    return render_template('purchase.html')
