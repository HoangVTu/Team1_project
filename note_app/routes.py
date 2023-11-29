from .forms import LoginForm, RegistrationForm, NoteForm
from app import app, db, Note
from flask import render_template, redirect, flash, request, url_for
from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import current_user, login_user, logout_user, login_required
from .models import User
from datetime import datetime
import json 


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
            return json({'message': 'Note added', 'id': new_note.id}), 201
        else:
            return json({'errors': form.errors}), 400

    notes = Note.query.order_by(Note.created_at.desc()).all()
    return json([
        {'id': note.id, 'title': note.title, 'content': note.content, 
         'created_at': note.created_at.isoformat(), 'highlights': note.highlights}
        for note in notes
    ])

@app.route('/test')
def test():
    return 'Test successful!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    # If the user is already logged in (authenticated), redirect the user to the home page:
    if current_user.is_authenticated:
        return redirect(url_for('index'))

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
        return redirect(url_for('index'))

    # Render the login.html template with the LoginForm instance:
    return render_template('login.html', title = 'Sign In For Memomate', form = form)


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
                f'Congratulations, {form.username.data} are now a Memomate user now!')
            return redirect(url_for('login'))
        else:
            # If 1 user with the same username already exists, flash an error message and redirect to the login page:
            flash(f'Sorry, {form.username.data} is already an Memomate user!')
            return redirect(url_for('login'))

    # Render the register.html template with the RegistrationForm instance:
    return render_template('register.html', title='User Register for Memomate', form=form)

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