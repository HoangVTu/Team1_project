from flask import render_template, jsonify, request, redirect, url_for, session, flash
from note_app import app, db
from note_app.forms import SecurityQuestionForm, NewPasswordForm
from flask_login import login_user, current_user
from note_app.models import Note, User
from note_app.forms import NoteForm, RegistrationForm, LoginForm
from datetime import datetime

@app.route('/')
def home():
    return render_template('home.html')

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
def register_acc():
    form = RegistrationForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return "Username or email already exists. Please choose different credentials."


        new_user = User(username=username, email=email, password=password)  
        # print(new_user)
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

@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    form = SecurityQuestionForm()

    if form.validate_on_submit():
        username_or_email = form.username.data
        user = User.query.filter_by(username=username_or_email).first() or User.query.filter_by(email=username_or_email).first()

        if user:
            flash('Answer correct! You can now reset your password.', 'success')
            # Redirect to the reset password page with the username as a parameter
            return redirect(url_for('reset_password', username=user.username))

        flash('Incorrect answer to the security question. Please try again.', 'error')

    return render_template('reset_password_request.html', form=form)

@app.route('/reset_password/<username>', methods=['GET', 'POST'])
def reset_password(username):
    form = NewPasswordForm()
    user = User.query.filter_by(username=username).first()

    if form.validate_on_submit():
        # update user's password
        user.set_password(form.new_password.data)
        db.session.commit()

        flash('Your password has been reset.', 'success')
        return redirect(url_for('login'))

    return render_template('reset_password.html', username=username, form=form)

@app.route('/log_out')
def log_out():
    session.pop('username', None)
    return redirect(url_for('login'))

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

@app.route('/delete_note/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    note = Note.query.get(note_id)
    if note:
        db.session.delete(note)
        db.session.commit()
        return jsonify({'message': 'Note deleted'}), 200
    return jsonify({'message': 'Note not found'}), 404

@app.route('/star_note/<int:note_id>', methods=['POST'])
def star_note(note_id):
    note = Note.query.get(note_id)
    if note:
        note.is_starred = True
        db.session.commit()
        return jsonify({'message': 'Note starred'}), 200
    return jsonify({'message': 'Note not found'}), 404

@app.route('/unstar_note/<int:note_id>', methods=['POST'])
def unstar_note(note_id):
    note = Note.query.get(note_id)
    if note:
        note.is_starred = False
        db.session.commit()
        return jsonify({'message': 'Note unstarred'}), 200
    return jsonify({'message': 'Note not found'}), 404

with app.app_context():
    db.drop_all()  
    db.create_all() 


if __name__ == '__main__':
    app.run (debug = True)


