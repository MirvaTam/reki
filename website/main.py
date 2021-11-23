from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . import db
from .models import Users, Reseptit

main = Blueprint('main', __name__)
# defines that this file is a blueprint

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        resepti = request.form.get('resepti')

        new_resepti = Reseptit(data=resepti, user_id=current_user.id)
        db.session.add(new_resepti)
        db.session.commit()
        flash('Resepti lisätty')
   
    return render_template('profile.html', user=current_user, name=current_user.etunimi)

@main.route('/feedback', methods=['POST'])
def palaute():
    if request.method == 'POST':
        email = request.form['email']
        palaute = request.form['palaute']
        if email == '' or palaute == '':
            return render_template('index.html', message='Täytä vaadittavat kentät')
        
        #db.session.query(Feedback): #tarviiko, miten avataan tietokantayhteys??
        #data = Feedback(email, palaute) #tietokantayhteys??
        #db.session.add(data)
        #db.session.commit()            
        #todo send_mail(email, palaute)
        flash('Kiitos palautteestasi!')
        return render_template('index.html')