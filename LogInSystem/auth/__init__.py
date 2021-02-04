from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'JonasIstGut'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://db.swlite'

    db.init_app(app)

    from .auth import auth as authblueprint
    app.register_blueprint(authblueprint)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app