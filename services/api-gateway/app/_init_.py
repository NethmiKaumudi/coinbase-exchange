# /api-gateway/app/__init__.py

from flask import Flask
from .routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG_FILE', silent=True)
    
    register_routes(app)
    
    return app
