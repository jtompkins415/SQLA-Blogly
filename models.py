"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

default_iamge = 'https://cdn.pixabay.com/photo/2013/07/13/12/07/avatar-159236__340.png'

class User(db.Model):
    '''User Class'''

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True, auto_increment = True)
    first_name = db.Column(db.Text, nullable = False)
    last_name = db.Column(db.Text, nullable = False)
    image_url = db.Column(db.Text, nullable = False, default = default_iamge)

    @property
    def full_name(self):
        '''Show full name'''

        return f'{self.first_name} {self.last_name}'

def  connect_db(app):
    '''Connect to a DB'''
    db.app = app
    db.init_app(app)

