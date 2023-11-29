from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMix
from app import app, login, db
from time import time
import jwt

class User(db.Model, UserMix):
    # User's ID:
    id = db.Column(db.Integer, primary_key = True)
    # Username:
    username = db.Column(db.String(40), nullable = False)
    # User's password:
    password = db.Column(db.String(40), nullable = False)
    # User's email:
    email = db.Column(db.String(100), nullable = False, unique = True)

    # Set up relationship with class Post:
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    # Function which generates password hash for user's password --> more protected!
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # Function which checks the hash of password given by user and the password in Database:
    def check_password(self, password):
        return check_password_hash(self.password, password)

    # Function which generates a reset password token for the user:
    # The token will expire after 900 seconds (15 mins)
    def get_reset_password_token(self, expires_in = 900):
        # Generates token by using the encode() method of PyJWT package: 
        return jwt.encode(
            # The dictionary below contains the data which will be encoded
            # with our Flask app's secret key to sign the token
            # and hashing algorithm 'HS256' for that token signature:
            {'reset_password': self.id, 'exp': time() + expires_in},
            myapp_obj.config['SECRET_KEY'], algorithm = 'HS256')

    # This static method verifies 1 reset password token then returns corresponding user:
    @staticmethod
    def verify_reset_password_token(token):
        try:
            # Decoding token by decode() method in PyJWT package:
            id = jwt.decode(token, myapp_obj.config['SECRET_KEY'], algorithms=['HS256'])['reset_password']
        except:
            # If the token is invalid (or has been already expired) --> None:
            return
        # If the token is valid --> the user object corresponding to the user id in the token.
        return User.query.get(id)

    # Function that returns 1 string every time creating 1 new row (user): 
    def __repr__(self):
        return f'<User {self.id}: {self.username}>'


# This is a callback function used by Flask-Login to load a user from a user ID.
# The 'id' argument is the user ID as a string, 
# which we convert to an integer before querying the database for the user:
@login.user_loader
# The function returns a User object or None if no user is found with the given ID.
def load_user(id):
    return User.query.get(int(id))