# /wallet/app/__init__.py

from flask import Flask
from .views import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG_FILE', silent=True)
    
    # Initialize SQLAlchemy here if needed
    from flask_sqlalchemy import SQLAlchemy
    db = SQLAlchemy(app)
    
    # Register routes
    register_routes(app)
    
    return app
