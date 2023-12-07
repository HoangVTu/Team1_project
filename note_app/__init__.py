# Import necessary modules and classes from Flask and its extensions
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

# Import configuration settings from the 'Config' class in the 'config' module
from note_app.config import Config

# Create a Flask web application instance
app = Flask(__name__)

# Configure the Flask application using settings from the 'Config' class
app.config.from_object(Config)

# Initialize a SQLAlchemy database instance with the Flask application
db = SQLAlchemy(app)

# Initialize a Bootstrap extension with the Flask application
bootstrap = Bootstrap(app)

# Import routes, models, and forms from respective modules
from note_app.routes import *
from note_app.models import *
from note_app.forms import *

# Create database tables based on the defined models
with app.app_context():
    db.drop_all()  # Drop existing tables (if any)
    db.create_all()  # Create new tables based on the models

# Run the Flask application in debug mode if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
