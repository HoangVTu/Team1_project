from flask import Flask, render_template, jsonify, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import current_user, login_user, logout_user, login_required, UserMixin
from flask_wtf import FlaskForm
from wtforms.validators import ValidationError, EqualTo
from wtforms import StringField, TextAreaField, HiddenField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
db = SQLAlchemy(app)

users = [
    {'username': 'user1', 'email': 'user1@example.com', 'password': 'password1'},
    {'username': 'user2', 'email': 'user2@example.com', 'password': 'password2'}
]

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    highlights = db.Column(db.String(1000))  
    reminder = db.Column(db.DateTime)

class NoteForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    highlights = HiddenField()  
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    # Custom validation method for username uniqueness:
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    # Custom validation method for email uniqueness:
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

# Login form for registered users:
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

# Checking password form:
class CheckPasswordForm(FlaskForm):
    password = StringField('Password Checker')
    submit = SubmitField('Submit')
    
class User(db.Model, UserMixin):
    # User's ID:
    id = db.Column(db.Integer, primary_key=True)
    # Username:
    username = db.Column(db.String(32), nullable=False)
    # User's password:
    password = db.Column(db.String(32), nullable=False)
    # User's email:
    email = db.Column(db.String(100), nullable=False, unique=True)

    # Set up relationship with class Post:
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    # Function which generates password hash for user's password --> more protected!
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # Function which checks the hash of password given by user and the password in Database:
    def check_password(self, password):
        return check_password_hash(self.password, password)

    # Function that returns 1 string every time creating 1 new row (user): 
    def __repr__(self):
        return f'<User {self.id}: {self.username}>'

# Set up the table Post with different columns in Database:
class Post(db.Model):
    # Post ID:
    id = db.Column(db.Integer, primary_key=True)
    # Post Body:
    body = db.Column(db.String(256))
    # Post timestamp:
    timestamp = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)

    # Set up relationship with class User:
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Function that returns 1 string every time creating 1 new Post element in Database:
    def __repr__(self):
        return f'<Post {self.id}: {self.body}>'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/test')
def test():
    return 'Test successful!'

@app.route('/register_acc', methods=['GET', 'POST'])
def register_acc():
    # If the user is already authenticated (logged in), redirect the user to the home page:
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    # Create an instance of the RegistrationForm:
    form = RegistrationForm()

    # If the form has been submitted and all fields are valid, attempt to create 1 new user:
    if form.validate_on_submit():
        # Check if 1 user with the same username already exists in the database:
        if db.session.query(User).filter_by(username=form.username.data).count() < 1:
            # Create 1 new User object with the form data and add it to the database:
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            # Flash a success message and redirect to the login page:
            flash(
                f'Congratulations, you are now {form.username.data} a Memomate user now!')
            return redirect(url_for('login'))
        else:
            # If 1 user with the same username already exists, flash an error message and redirect to the login page:
            flash(f'Sorry, {form.username.data} is already an Memomate user!')
            return redirect(url_for('login'))

    # Render the register.html template with the RegistrationForm instance:
    return render_template('register.html', title='Register for Memomate', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # If the user is already logged in (authenticated), redirect the user to the home page:
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    # Create an instance of the LoginForm:
    form = LoginForm()

    # If the form has been submitted and all fields are valid, attempt to log the user in:
    if form.validate_on_submit():
        # Query the User table for a user with the specified username:
        user = User.query.filter_by(username=form.username.data).first()

        # If the user doesn't exist, flash an error message and redirect to the login page:
        if user is None:
            flash('Invalid Username')
            return redirect(url_for('login'))
        # If the entered password is incorrect, flash an error message and redirect to the login page:
        if not user.check_password(form.password.data):
            flash('Invalid Password')
            return redirect(url_for('login'))

        # If the user exists and the entered password is correct, log the user in and redirect the user to the home page:
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('home'))

    # Render the login.html template with the LoginForm instance:
    return render_template('login.html', title='Sign In for Memomate', form=form)

@app.route('/logout')
def logout():
    #  Log the user out and redirect to the login page:
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f"Welcome, {session['username']}! This is your dashboard. <a href='/logout'>Logout</a>"
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run (debug = True)