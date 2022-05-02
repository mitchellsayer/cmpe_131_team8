from flask import Blueprint, render_template
from flask_login import login_required, current_user
from numpy import product
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
    other_listings = Listing.query.filter(Listing.userID == current_user.id)
    # test_listings = []
    # for i in range(5):
    #     listing = Listing(
    #         productID = i,
    #         userID = current_user.id,
    #         name = f"Test Item {i}",
    #         brand = "Test Brand",
    #         description = "This is a test item description",
    #         price = 10.99,
    #         image = 'images/test_image.jpeg',
    #         stock = 5
    #     )
    #     test_listings.append(listing)
    #     db.session.add(listing)
    # db.session.commit()

    return render_template('listings.html', listings = other_listings)

@main.route('/new_listing')
@login_required
def new_listing():
    return render_template('new_listing.html')

@main.route('/purchase/<productID>')
@login_required
def purchase(productID):
    print(str(productID))
    cur_listing = Listing.query.get(productID)

    tax = round((cur_listing.price * 0.0725), 3)
    total = cur_listing.price + tax

    print(cur_listing)
    return render_template('purchase.html', listing=cur_listing, tax=tax, total=total)

@main.route('/purchase', methods=['POST'])
@login_required
def purchase_post():
    #Before final payment is paid for, an additional sales tax is included
    total_checkout = total_price + (total_price *0.10)
    return redirect(url_for('index.html'))
