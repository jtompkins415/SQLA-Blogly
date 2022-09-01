"""Blogly application."""

from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, User, connect_db

app = Flask(__name__)

app.config['SECRET_KEY'] = 'this-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def redirect_to_users():
    '''Redirect to list of users'''
    # users = User.query.all()
    return redirect('/users', code = 200)


@app.route('/users')
def list_users():
    '''Show all users'''
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('list.html', users=users)

@app.route('/users/new', methods=['GET'])
def show_user_form():
    '''Show an add form for users'''
    return render_template('user_form.html')

@app.route('/users/new', methods=['POST'])
def create_user():
   
    new_user = User(first_name=request.form['first_name'], last_name=request.form['last_name'], image_url=request.form['image_url'] or None)
    
    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>')
def show_user(user_id):
    '''Show details about a single user'''
    user = User.query.get_or_404(user_id)
    return render_template('details.html', user=user)


@app.route('/users/<int:user_id>/edit', methods=['GET'])
def show_edit_form(user_id):
    '''Show user edit form'''
    
    user=User.query.get_or_404(user_id)
    return render_template('edit_form.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def update_user(user_id):
    '''Update user information'''

    user=User.query.get_or_404(user_id)

    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    '''Delete user from DB'''

    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()

    return redirect('/users')

# @app.route('/species/<species_id>')
# def show_pets_by_species(species_id):
#     pets = Pet.get_by_species(species_id)
#     return render_template('species.html', pets=pets, species=species_id)


