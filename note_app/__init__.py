from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from note_app.config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


# login_manager = LoginManager(app)
# login_manager.login_view = 'login'


from note_app.routes import *
from note_app.models import *
from note_app.forms import *


with app.app_context():
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
