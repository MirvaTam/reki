from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import Users
from . import db

auth = Blueprint('auth', __name__)
# defines that this file is a blueprint

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = Users.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@auth.route('/sign_up', methods=['POST'])
def sign_up_post():
    email = request.form.get('email')
    etunimi = request.form.get('etunimi')
    password = request.form.get('pass2')

    user = Users.query.filter_by(email=email).first()

    if user: # if a user is found, we want to redirect to login /or sigup/
        flash('Email on jo olemassa. Kirjaudu tästä sisään.')
        return redirect(url_for('auth.login'))
        
    # create a new user with the form data
    new_user = Users(email=email, etunimi=etunimi, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))
    

#@auth.route('/sign_up', methods=['GET', 'POST'])
#def sign_up():
#    if request.method == 'POST':
#        email = request.form.get('email')
#        etunimi = request.form.get('etunimi')
#        password1 = request.form.get('pass1')
#        password2 = request.form.get('pass2')
#
#        if len(email) < 4:
#            flash ('Email-osoitteen pitää olla enemmän kuin 3 merkkiä', category='error')
#        elif len(etunimi) < 2:
#            flash ('Etunimi pitää olla enemmän kuin 1 merkkiä', category='error')
#        elif password1 != password2:
#            flash ('Salasanat eivät mätsää', category='error')
#        elif len(password1) < 4:
#            flash ('Salasanan pitää olla vähintään 3 merkkiä', category='error')
#        else:
#            #add user to database
#            flash ('Tili luotu onnistuneesti', category='success')
#
#    return render_template('sign_up.html')
