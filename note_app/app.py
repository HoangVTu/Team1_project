from flask import Flask, render_template, jsonify, request, redirect, url_for, session, Response
from flask_socketio import SocketIO, join_room, leave_room, emit
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from flask_login import LoginManager
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config.from_mapping(
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'Memomate',
    SQLALCHEMY_DATABASE_URI=os.environ.get(
        'DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'
socketio = SocketIO(app)
migrate = Migrate(app, db)

# Define the Note model
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    highlights = db.Column(db.String(1000))
    reminder = db.Column(db.DateTime)
    highlighted_text = db.Column(db.String(1000))
    
class NoteForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    highlights = HiddenField()

# Define the User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# Create tables before the first request
# @app.before_first_request
# def create_tables():
#     db.create_all()

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/notes', methods=['GET', 'POST'])
def handle_notes():
    print("handle_notes function called")
    notes = Note.query.order_by(Note.created_at.desc()).all()
    print("Notes to send:", notes) 
    if request.method == 'POST':
        data = request.json
        print("Received data:", data)
        form = NoteForm(meta={'csrf': False})
        if form.validate_on_submit():
            new_note = Note(
                title=form.title.data, 
                content=form.content.data,
                highlights=form.highlights.data,
                reminder=data.get('reminder')
            )
            db.session.add(new_note)
            db.session.commit()
            return jsonify({'message': 'Note added', 'id': new_note.id}), 201
        else:
            return jsonify({'errors': form.errors}), 400

    notes = Note.query.order_by(Note.created_at.desc()).all()
    return jsonify([
        {'id': note.id, 'title': note.title, 'content': note.content, 
         'created_at': note.created_at.isoformat(), 'highlights': note.highlights}
        for note in notes
    ])

@app.route('/test')
def test():
    return 'Test successful!'

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return "Username or email already exists. Please choose different credentials."

        new_user = User(username=username, email=email, password=password)  
        db.session.add(new_user)
        db.session.commit()

        session['username'] = username  
        return redirect(url_for('dashboard'))  

    return render_template('register.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username, password=password).first()

        if user:
            session['username'] = username
            return redirect(url_for('dashboard'))

        return "Invalid login credentials. Please try again."

    return render_template('login.html', form=form)

@app.route('/log_out')
def log_out():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/create_note', methods=['GET', 'POST'])
def create_note():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        highlights = request.form.get('highlights')
        reminder_str = request.form.get('reminder')

        reminder = None
        if reminder_str:
            try:
                reminder = datetime.strptime(reminder_str, '%Y-%m-%dT%H:%M')
            except ValueError:
                pass  

        new_note = Note(title=title, content=content, highlighted_text=highlights, reminder=reminder)
        db.session.add(new_note)
        db.session.commit()

        return redirect(url_for('dashboard'))

    return render_template('create_note.html')


with app.app_context():
    db.drop_all()  
    db.create_all() 



if __name__ == '__main__':
    app.run (debug = True)