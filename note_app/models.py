from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from note_app import db


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    highlights = db.Column(db.String(1000))  
    reminder = db.Column(db.DateTime)
    highlighted_text = db.Column(db.String(1000))
    reminder = db.Column(db.DateTime, nullable=True)
    is_starred = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    folder_id = db.Column(db.Integer, db.ForeignKey('folder.folder_id'))
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    security_answer = db.Column(db.String(150), nullable=False)

class Folder(db.Model):
    folder_id = db.Column(db.Integer, primary_key = True)
    name =db.Column(db.String(255), nullable = False)
    notes = db.relationship('Note', backref = 'folder', lazy = True)
    