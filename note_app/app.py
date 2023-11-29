from flask import Flask, render_template, jsonify, request, redirect, url_for, session, Response
from flask_socketio import SocketIO, join_room, leave_room, send, emit
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
db = SQLAlchemy(app)
socketio = SocketIO(app)

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
    highlighted_text = db.Column(db.String(1000))
    reminder = db.Column(db.DateTime, nullable=True)
    
    def __repr__(self):
        return f"Note('{self.id}')"

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        note_content = request.form.get('content')
        note = Note.query.first()
        
        if note:
            note.content = note_content
        else:
            new_note = Note(content=note_content)
            db.session.add(new_note)
        
        db.session.commit()
        
        return redirect(url_for('index'))
    
    note = Note.query.first()
    return render_template('index.html', note=note)

if __name__ == '__main__':
    app.run(debug=True)
    
current_note_content = ""

@app.route('/', methods=['GET', 'POST'])
def home():
    global current_note_content
    if request.method == 'POST':
        # Update the note content when the form is submitted.
        current_note_content = request.form['content']
    
    return render_template('index.html', note={'content': current_note_content})

@app.route('/export')
def export_note():
    global current_note_content
    # Make sure there is content to export.
    if not current_note_content.strip():
        return "No content to export", 404

    # Set the headers and filename for the download prompt.
    headers = {
        'Content-Disposition': 'attachment; filename=note.txt',
        'Content-Type': 'text/plain'
    }
    
    # Return the note as a downloadable text file.
    return Response(current_note_content, headers=headers)

if __name__ == '__main__':
    app.run(debug=True)
    
# Dictionary to store the contents of the notes
notes_content = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def on_connect():
    print('User connected')

@socketio.on('disconnect')
def on_disconnect():
    print('User disconnected')

@socketio.on('join')
def on_join(data):
    room = data['room']
    join_room(room)
    # Send existing note content when user joins the room
    if room in notes_content:
        emit('note content', {'content': notes_content[room]}, room=room)

@socketio.on('leave')
def on_leave(data):
    room = data['room']
    leave_room(room)

@socketio.on('edit note')
def handle_edit_note_event(data):
    room = data['room']
    content = data['content']
    # Update the note content in the dictionary
    notes_content[room] = content
    # Broadcast the updated content to all users in the room
    emit('note content', {'content': content}, room=room, include_self=False)

if __name__ == '__main__':
    socketio.run(app, debug=True)

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
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

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

@app.route('/register_acc', methods=['POST', 'GET'])
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
        return redirect(url_for('/dashboard'))  

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