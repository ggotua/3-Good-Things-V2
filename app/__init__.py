import os
from flask import Flask
from flask_login import LoginManager
from .db import db

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev')
    
    # Database config
    database_url = os.environ.get('DATABASE_URL')
    if database_url and database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
        
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url or 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login' # Note: API auth handles 401 differently often, but good fallback
    
    # Initialize database tables
    with app.app_context():
        # Import models so they are registered with SQLAlchemy
        from . import models 
        db.create_all()
    
    # Register blueprints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app
