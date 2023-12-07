from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField, PasswordField, SubmitField
from wtforms.validators import DataRequired

# Form for creating and editing notes
class NoteForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    highlights = HiddenField()  # Hidden field for storing highlights, if needed


# Form for user registration
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    security_answer = StringField('Answer to Security Question: What was the name of your elementary school?', validators=[DataRequired()])
    submit = SubmitField('Register')


# Form for user login
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# Form for resetting user password
class PasswordResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    security_answer = StringField('Answer to Security Question', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired()])
    submit = SubmitField('Reset Password')


# Form for creating folders
class FolderForm(FlaskForm):
    name = StringField('Folder Name')
    submit = SubmitField('Create Folder')
    enter = SubmitField('Enter')  # It's not clear what 'enter' does; you might want to add a comment explaining its purpose
