# Initialize app
# Set up flask
# Register route blueprints
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os

db = SQLAlchemy()

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///packd.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    CORS(app)

    # Import after db is initialized
    from . import models 

    from .routes import auth, groups, notes, home
    app.register_blueprint(auth.bp)
    app.register_blueprint(home.bp)
    # app.register_blueprint(groups.bp) # No need to register now
    # app.register_blueprint(notes.bp)

    return app

