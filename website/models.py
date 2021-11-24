from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Reseptit(db.Model):
    __tablename__ = 'reseptit'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000))
    content = db.Column(db.String(1000))
    comment = db.Column(db.String(1000))
    created = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    etunimi = db.Column(db.String(150))
    reseptit = db.relationship('Reseptit')

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    palaute = db.Column(db.Text())