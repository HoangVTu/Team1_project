import os

class Config:
    SECRET_KEY = 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///notes.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Add other configuration options as needed
