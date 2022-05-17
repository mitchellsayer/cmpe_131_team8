from ast import Break
import os
import re
import datetime as dt
import random
import string

from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from flask_mail import Message
from werkzeug.utils import secure_filename

from .models import Listing
from . import db, mail, ALLOWED_EXTENSIONS, UPLOAD_FOLDER

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

def compute_purchase_totals(quantity, price):
    subtotal = round(quantity * price, 2)
    tax = round(subtotal * 0.0725, 2)
    total = round(subtotal + tax, 2)

    totals = {
        'subtotal': subtotal,
        'tax':      tax,
        'total':    total,
        'quantity': quantity
    }

    return totals

def validate_card(card_number_str):
    isOdd=True
    processCardNumber=[]
    digit_char_list = list(card_number_str)
    for x in reversed(digit_char_list):
        x=int(x)
        if (isOdd):
            doubleVariable=2*x
            if (doubleVariable > 9):
                doubleVariable = doubleVariable//(10) + doubleVariable%(10)
            processCardNumber.append(doubleVariable)    
        else:
            processCardNumber.append(x)
        isOdd=not isOdd
    card_sum = sum(processCardNumber)
    return (card_sum % 10 == 0)

def get_email_confirmation_number(length):   
    get_char = lambda x: random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase)
    rnd_list = [get_char(x) for x in range(length)]
    return ''.join(rnd_list)

def build_totals_str(totals_dict):
    msg = f'''
    \tQuantity: {totals_dict['quantity']}
    \tSubtotal: ${totals_dict['subtotal']}
    \tTax: ${totals_dict['tax']}
    \tTotal: ${totals_dict['total']}
    '''
    return msg

def build_email_body(quantity, cur_listing):
    current_time = dt.datetime.now()
    confirmation_number = get_email_confirmation_number(current_app.config['CONFIRMATION_NUMBER_LEN'])
    totals = compute_purchase_totals(quantity, cur_listing.price)

    msg = f"""\
    Purchase Comfirmation of {cur_listing.name}\n
    {build_totals_str(totals)}\n
    Confirmation number: {confirmation_number}
    Purchase time: {current_time}
    """
    return msg
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

@main.route('/listings', methods=['POST','GET'])
@login_required
def listings():
    flash_id = request.args.get('id')
    all_listings = Listing.query.all()
    if request.method == "POST":
        search_entry = request.form.get('search-txt')
        price_filter = request.form.get('price_filter')
        if (search_entry == None or search_entry==''):
            if price_filter=='high2low':
                print("high2low")
                all_listings = Listing.query.order_by(Listing.price.desc()).all()
                print(all_listings)
            elif price_filter=='low2high':
                print("low2high")
                all_listings = Listing.query.order_by(Listing.price.asc()).all()
                print(all_listings)
            else:
                all_listings = Listing.query.all()

        else:
            if price_filter=='high2low':
                all_listings = Listing.query.filter_by(name = search_entry).order_by(Listing.price.desc()).all()
            elif price_filter=='low2high':
                all_listings = Listing.query.filter_by(name = search_entry).order_by(Listing.price.asc()).all()
            else:
                all_listings = Listing.query.filter(Listing.name == search_entry)
        
    return render_template('listings.html', listings = all_listings, id=flash_id)

@main.route('/new_listing')
@login_required
def new_listing():
    return render_template('new_listing.html')

@main.route('/new_listing', methods=['POST'])
@login_required
def new_listing_post():
    # Parse form
    title = request.form.get('title')
    brand = request.form.get('brand')
    description = request.form.get('description')
    stock = request.form.get('stock')
    price = request.form.get('price')
    
    # Validate File
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    
    if (not (file and file.filename == '' and allowed_file(file.filename))):
        flash('File not allowed')
        return redirect(request.url)

    # Save File
    filename = secure_filename(file.filename)
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    print(f'uploaded: {filename}')

    # Update Listing Table
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

@main.route('/purchase/<productID>', methods=['GET'])
@login_required
def purchase(productID):
    cur_listing = Listing.query.get(productID)
    quantity = int(request.args.get('quantity'))

    if (quantity > cur_listing.stock):
        flash('Selected quantity is greater than item stock.')
        return redirect(url_for('main.listings', id=productID))
    if (quantity <= 0 ):
        flash('Selected quantity must be greater than 0.')
        return redirect(url_for('main.listings', id=productID))

    totals = compute_purchase_totals(quantity, cur_listing.price)

    return render_template('purchase.html', 
                           listing=cur_listing,  
                           totals=totals)

@main.route('/purchase/<productID>', methods=['POST'])
@login_required
def purchase_post(productID):
    cur_listing = Listing.query.get(productID)

    # Parse Form
    cardNumber = request.form.get('cardNumber')
    paymentType = request.form.get('paymentType')
    cardOwner = request.form.get('cardOwner')
    expirationDate = request.form.get('expirationDate')
    quantity = int(request.form.get('quantity'))

    if (not cardOwner or not expirationDate or not cardNumber):
        flash("Please fill out all fields")
        return redirect(url_for('main.purchase', productID=productID) + f'?quantity={quantity}')

    # Validate Card
    validation = validate_card(cardNumber)
    if (not validation):
        flash("Please enter a valid card!")
        return redirect(url_for('main.purchase', productID=productID) + f'?quantity={quantity}')

    # Update Listing table
    cur_listing.stock -= quantity
    if (cur_listing.stock <= 0):
        db.session.delete(cur_listing)
    db.session.commit()

    # TODO: Update Purchase table

    # Send Confirmation Email
    sender_email = current_app.config['MAIL_USERNAME']
    msg = Message('Purchase Confirmation', 
                  sender=sender_email, 
                  recipients = [current_user.email])
    msg.body = build_email_body(quantity, cur_listing)

    try:
        print(f'Sending email from {sender_email} to {current_user.email}')
        mail.send(msg)
    except Exception as e:
        print('Sending email failed.')
        print(e)
    # TODO: add flash msg to profile page
    flash("Confirmation Email Sent")

    return redirect(url_for('main.profile'))

   
