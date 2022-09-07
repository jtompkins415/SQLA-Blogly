"""Models for Blogly."""

import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

default_iamge = 'https://cdn.pixabay.com/photo/2013/07/13/12/07/avatar-159236__340.png'

class User(db.Model):
    '''User Class'''

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    first_name = db.Column(db.Text, nullable = False)
    last_name = db.Column(db.Text, nullable = False)
    image_url = db.Column(db.Text, nullable = False, default = default_iamge)

    posts =  db.relationship('Post', backref = 'users')

    @property
    def full_name(self):
        '''Show full name'''

        return f'{self.first_name} {self.last_name}'


class Post(db.Model):
    '''Post Class'''

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.Text, nullable = False)
    content = db.Column(db.Text, nullable = False)
    created_at = db.Column(db.DateTime, nullable = False, default =datetime.datetime.now)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)

    @property
    def friendly_date(self):
        '''Return well-formated date'''

        return self.created_at.strftime('%a %b %-d %Y, %-I:%M %p')

def  connect_db(app):
    '''Connect to a DB'''
    db.app = app
    db.init_app(app)

