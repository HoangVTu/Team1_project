from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
db = SQLAlchemy(app)

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

if __name__ == '__main__':
    app.run(debug=True)
