# /services/account-management/app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')

    db.init_app(app)

    with app.app_context():
        # Import routes and models
        from . import views, models
        # Create tables
        db.create_all()
    
    return app
