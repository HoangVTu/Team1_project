from flask import Flask, render_template, jsonify, request, redirect, url_for, session, Response
from note_app import app, db
from note_app.models import Note, User,Folder
from note_app.forms import NoteForm, RegistrationForm, LoginForm, PasswordResetForm,FolderForm
from datetime import datetime
from deep_translator import GoogleTranslator


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/notes', methods=['GET', 'POST'])
def handle_notes():
    if 'username' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    user = User.query.filter_by(username=session['username']).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404
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
            new_note.user_id = user.id
            db.session.add(new_note)
            db.session.commit()
            return jsonify({'message': 'Note added', 'id': new_note.id}), 201
        else:
            return jsonify({'errors': form.errors}), 400
    notes = Note.query.filter_by(user_id=user.id).order_by(Note.created_at.desc()).all()
    return jsonify([
        {'id': note.id, 'title': note.title, 'content': note.content,
         'created_at': note.created_at.isoformat(), 'is_starred': note.is_starred, 'highlights': note.highlights}
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




        new_user = User(username=username, email=email, password=password, security_answer=form.security_answer.data)  
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


@app.route('/log_out')
def log_out():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        user = User.query.filter_by(username=session['username']).first()
        if user:
            user_notes = Note.query.filter_by(user_id=user.id).order_by(Note.created_at.desc()).all()
            return render_template('dashboard.html', username=session['username'], notes=user_notes)
    else:
        return redirect(url_for('login'))




@app.route('/create_note', methods=['GET', 'POST'])
def create_note():
    if 'username' not in session:
        return redirect(url_for('login'))


    user = User.query.filter_by(username=session['username']).first()
    if not user:
        return redirect(url_for('login'))
   
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


        new_note = Note(title=title, content=content, highlighted_text=highlights, reminder=reminder, user_id=user.id)
        db.session.add(new_note)
        db.session.commit()


        return redirect(url_for('dashboard'))


    return render_template('create_note.html')

@app.route('/api/folders',methods = ['GET', 'POST'])
def handle_folders():
    print("handle_folders called")
    if request.method == "POST":
        folderData = request.json
        print("Receieved data:", folderData)
        form = FolderForm(meta = {'csrf':False})
        if form.validate_on_submit():
            new_folder = Folder(name = form.name.data)
            db.session.add(new_folder)
            db.session.commit()
            return jsonify({'message': 'folder added', 'id': new_folder.id}),201
        else:
            return jsonify({'errors': form.errors}), 400
    folders = Folder.query.order_by(Folder.folder_id.desc()).all()
    folder_list =[]
    for folder in folders:
        folderData = {'id':folder.folder_id, 'name':folder.name, 'notes': []}
        for note in folder.notes:
            note_data = {'id': note.id, 'title': note.title, 'content': note.content}
            folderData['notes'].append(note_data)
        folder_list.append(folderData)
    return jsonify(folder_list)

@app.route('/api/folders/<int:folderid>/notes', methods=['GET', 'POST'])
def handle_notes_in_folders(folderid):
    print(f"Handling notes for folder {folderid}")
    notes = Note.query.filter_by(folder_id = folderid).all()
    note_list = []
    for note in notes:
        noteData = {'id': note.id, 'title': note.title, 'content': note.content}
        note_list.append(noteData)
    return jsonify(note_list)



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
        print(f"Note {note_id} starred")
        return jsonify({'message': 'Note starred'}), 200
    return jsonify({'message': 'Note not found'}), 404


@app.route('/unstar_note/<int:note_id>', methods=['POST'])
def unstar_note(note_id):
    note = Note.query.get(note_id)
    if note:
        note.is_starred = False
        db.session.commit()
        print(f"Note {note_id} unstarred")
        return jsonify({'message': 'Note unstarred'}), 200
    return jsonify({'message': 'Note not found'}), 404


@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    form = PasswordResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.security_answer == form.security_answer.data:
            user.password = form.new_password.data  
            db.session.commit()
            return redirect(url_for('login'))
        else:
            return "Invalid email or security answer."
    return render_template('password_reset.html', form=form)


@app.route('/api/starred_notes', methods=['GET'])
def get_starred_notes():
    if 'username' not in session:
        return jsonify({'error': 'Unauthorized'}), 401


    user = User.query.filter_by(username=session['username']).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404


    starred_notes = Note.query.filter_by(user_id=user.id, is_starred=True).all()
    return jsonify([
        {'id': note.id, 'title': note.title, 'content': note.content}
        for note in starred_notes
    ])


@app.route('/edit_note/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    note = Note.query.get_or_404(note_id)


    if request.method == 'POST':
        note.title = request.form['title']
        note.content = request.form['content']
        db.session.commit()
        return redirect('/dashboard')


    return render_template('edit_note.html', note=note)


@app.route('/update_note/<int:note_id>', methods=['POST'])
def update_note(note_id):
    note = Note.query.get_or_404(note_id)
    note.title = request.form['title']
    note.content = request.form['content']
    db.session.commit()
    return redirect('/dashboard')




@app.route('/search', methods = ['GET', 'POST'])
def search():
    if request.method =="POST":
        searched_term =  request.form['search']
        note_results = Note.query.filter(Note.title.contains(searched_term)).all()
        if note_results:
            for note in note_results:
                return render_template('search.html',searched=searched_term, note_results=note.content)
        else:
            return "The note was note found. Please try again."
        return render_template('search.html', searched=searched_term)

@app.route('/translate/<searched>/<note_results>', methods = ['GET','POST'])
def translate(searched,note_results):
    result1 =""
    result2 =""
    if request.method == "POST":
        yetTo_TranslateTitle = searched
        yetTo_TranslateContent = note_results
        selected_language = request.form['language']
        # lang = detectlanguage.batch_detect(yetTo_TranslateTitle,yetTo_TranslateContent)
        # if lang:
        translatedTitle = GoogleTranslator(source='auto',target= selected_language).translate(yetTo_TranslateTitle)
        translatedContent = GoogleTranslator(source='auto',target= selected_language).translate(yetTo_TranslateContent)
        # Note.title = result1
        # Note.content = result2
        # print (Note.title, Note.content)
        return render_template('translate.html',result1=translatedTitle, result2 =translatedContent)
    else:
        return jsonify({'note_exists':False})

@app.route('/createFolder', methods = ['GET','POST'])
def create_folder():
    form = FolderForm()
    if form.validate_on_submit():
        folderName = Folder(name = form.name.data)
        db.session.add(folderName)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('createFolder.html',form = form)


@app.route('/chooseFolder/<note_id>', methods = ['GET', 'POST'])
def chooseFolder(note_id):
    form = FolderForm()
    if request.method =="POST":
        folderName = request.form.get('name')
        folderResults = Folder.query.filter(Folder.name == folderName).first()
        return render_template('chooseFolder.html',form=form, folderResults=folderResults, note_id=note_id)
    return render_template('chooseFolder.html', form=form, note_id=note_id)
    #     print("new code is here")
    # return redirect(url_for('add_to_folder',note_id=note_id))


@app.route('/addToFolder/<note_id>', methods = ['GET', 'POST'])
def add_to_folder(note_id):
    form = FolderForm()
    print("code is here")
    if request.method == "POST":
        print("im here")
        folderName = form.name.data
        folderResults = Folder.query.filter(Folder.name == folderName).first()
        note = Note.query.get(note_id)
        if folderResults:
            print("code is in the if statement")
            note = Note.query.get(note_id)
            if note:
                if note not in folderResults.notes:
                    folderResults.notes.append(note)
                    db.session.commit()
                    print('Note added to folder successfully!', 'success')
                else:
                    print('Note already exists in the folder.')
            else:
                print("Note not found")
        else:
            print("Creating a new folder.")
            new_folder = Folder(name=folderName)
            note = Note.query.get(note_id)
            if note:
                new_folder.notes.append(note)
                db.session.add(new_folder)
                db.session.commit()
                print('Folder and note added successfully!', 'success')
            else:
                print('Note not found.')
        return redirect(url_for('dashboard', note_id = note_id))
    return render_template('addToFolder.html', form=form)



@app.route('/user_question', methods=['GET', 'POST'])
def user_question():
    if request.method == 'POST':
        securityAnswer = request.form['security_answer']
        user = User.query.filter_by(security_answer=securityAnswer).first()
        if user:
              #Redirect to the edit_user_profile route, passing user ID as an argument
            return redirect(url_for('edit_user_profile', user_id=user.id))
        else:
            return jsonify({'answer': False})
    
    return render_template('displayUserQuestion.html')



@app.route('/userProfile', methods=['GET', 'POST'])
def edit_user_profile():
    if request.method == "POST":
        past_user = User.query.filter_by(username=session['username']).first()

        new_username = request.form['username']
        new_password = request.form['password']
        confirm_new_password = request.form['confirm_password']
        new_email = request.form['email']

        if past_user:
            if past_user.username != new_username:
                past_user.username = new_username
            else:
                return "Past and Current Username cannot be the same. Please try again."
            if new_password and new_password == confirm_new_password:
                past_user.password = new_password
            else:
                return "Past and current password cannot be the same. Please try again."
            if past_user.email != new_email:
                past_user.email = new_email
            else:
                return "Past and current email cannot be the same. Please try again."
            db.session.commit()
            return redirect(url_for('edit_user_profile'))
        else:
            return "Did not work. Please try again."
    return render_template('editUserProfile.html')  




with app.app_context():
    db.drop_all()  
    db.create_all()




if __name__ == '__main__':
    app.run (debug = True)