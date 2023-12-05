from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class NoteForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    highlights = HiddenField()

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')
    security_question = StringField('Security Question', validators=[DataRequired()])
    security_answer = StringField('Answer to Security Question', validators=[DataRequired()])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class SecurityQuestionForm(FlaskForm):
    # Your form fields here, e.g., username, security_question, security_answer
    username = StringField('Username')
    security_question = StringField('Security Question')
    security_answer = StringField('Security Answer')
    submit = SubmitField('Submit')

class NewPasswordForm(FlaskForm):
    # Your form fields here, e.g., new_password
    new_password = PasswordField('New Password')
    submit = SubmitField('Submit')