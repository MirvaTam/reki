from sqlite3.dbapi2 import connect
from flask import Blueprint, render_template, request, flash
from flask.helpers import url_for
from flask_login import login_required, current_user
from . import db
from .models import Users, Reseptit, Feedback
import sqlite3

main = Blueprint('main', __name__)
# defines that this file is a blueprint

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')

        new_resepti = Reseptit(title=title, content=content, user_id=current_user.id)
        db.session.add(new_resepti)
        db.session.commit()
        flash('Resepti lisätty')
   
    return render_template('reseptit.html', user=current_user, name=current_user.etunimi)

@main.route('/reseptit', methods=['GET', 'POST'])
@login_required
def reseptit():

    resepti = Reseptit.query.all()

    return render_template('reseptit.html', resepti=resepti, user=current_user, name=current_user.etunimi)

@main.route('/feedback', methods=['POST'])
def feedback():
    if request.method == 'POST':
        email = request.form['email']
        palaute = request.form['palaute']
        if email == '' or palaute == '':
            return render_template('index.html', message='Täytä vaadittavat kentät')
        
        data = Feedback(email=email, palaute=palaute) 
        db.session.add(data)
        db.session.commit()            
        #todo send_mail(email, palaute)
        flash('Kiitos palautteestasi!')
        return render_template('index.html')