import os

# Configuration class for Flask application
class Config:
    # Secret key for protecting against CSRF attacks
    SECRET_KEY = 'your-secret-key'

    # Database URI for SQLAlchemy, using SQLite in this example
    SQLALCHEMY_DATABASE_URI = 'sqlite:///notes.db'

    # Disable Flask-SQLAlchemy modification tracking for improved performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Add other configuration options as needed
    # For example, you might add configurations for file uploads, email settings, etc.
