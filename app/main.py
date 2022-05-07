import os
import random

from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from .models import Listing
from . import db, ALLOWED_EXTENSIONS, UPLOAD_FOLDER

main = Blueprint('main', __name__)

# --------- Helper Functions ---------
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def unique_id():
    seed = random.getrandbits(32)
    while True:
       yield seed
       seed += 1

# -------------- Routes --------------
@main.route('/')
def index():
    all_listings = Listing.query.all()
    images = [l.image for l in all_listings]
    return render_template('index.html', images=images)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, email=current_user.email)

@main.route('/listings')
@login_required
def listings():
    flash_id = request.args.get('id')
    # other_listings = Listing.query.filter(Listing.userID != current_user.id)
    all_listings = Listing.query.all()

    return render_template('listings.html', listings = all_listings, id=flash_id)

@main.route('/new_listing')
@login_required
def new_listing():
    return render_template('new_listing.html')

@main.route('/new_listing', methods=['POST'])
@login_required
def new_listing_post():
    title = request.form.get('title')
    brand = request.form.get('brand')
    description = request.form.get('description')
    stock = request.form.get('stock')
    price = request.form.get('price')
    
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if not file or not allowed_file(file.filename):
        flash('File not allowed')
        return redirect(request.url)

    filename = secure_filename(file.filename)
    file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
    print(f'uploaded: {filename}')

    listing = Listing(
            productID = next(unique_id()),
            userID = current_user.id,
            name = title,
            brand = brand,
            description = description,
            price = float(price),
            image = filename,
            stock = int(stock))

    print(listing)
    db.session.add(listing)
    db.session.commit()

    return redirect(url_for('main.listings'))

@main.route('/purchase/<productID>')
@login_required
def purchase(productID):
    cur_listing = Listing.query.get(productID)
    quantity = int(request.args['quantity'])

    subtotal = round(quantity * cur_listing.price, 2)
    tax = round(subtotal * 0.0725, 2)
    total = round(subtotal + tax, 2)
    totals = {
        'subtotal': subtotal,
        'tax':      tax,
        'total':    total,
        'quantity': quantity
    }

    if (quantity > cur_listing.stock):
        flash('Selected quantity is greater than item stock.')
        return redirect(url_for('main.listings', id=productID))

    if (quantity == 0 ):
        flash('Selected quantity must be greater than 0.')
        return redirect(url_for('main.listings', id=productID))

    return render_template('purchase.html', 
                           listing=cur_listing,  
                           totals=totals)

@main.route('/purchase/<productID>', methods=['POST'])
@login_required
def purchase_post(productID):
    quantity = int(request.args['quantity'])
    cur_listing = Listing.query.get(productID)
    
    #reduce stock of item 
    return redirect(url_for('main.index'))
