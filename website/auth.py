from flask import Blueprint, render_template, request, flash
from . import db

auth = Blueprint('auth', __name__)
# defines that this file is a blueprint

@auth.route('/login') #, methods=['GET', 'POST'])
def login():
    #data = request.form # tuo lomakkeelle syötetyt tiedot
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return 'Logout'

@auth.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

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
