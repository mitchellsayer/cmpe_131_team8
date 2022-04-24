from app import app 
from flask import render_template
from flask import flash
from flask import redirect
from app.forms import LoginForm


@app.route('/home')
def home():
    return "HOME PG"


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.user_name.data == 'admin' and form.password.data == 'admin':
            flash('login Successful')
            return redirect('/home')
    return render_template('form.html', form=form)
