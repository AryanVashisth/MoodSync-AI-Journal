from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '0000'  # Set your secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Use SQLite for simplicity

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from your_app import routes  # Import your routes after defining the app, db, bcrypt, and login_manager
