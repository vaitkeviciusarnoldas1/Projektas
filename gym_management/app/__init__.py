from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the Flask application
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a more secure secret key
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://postgres:Nojus123456!@localhost:5432/Projektas')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy and Migrate extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import routes and models after initializing the extensions
from app import routes, models
