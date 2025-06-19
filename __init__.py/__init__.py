from flask import Flask
from .config import Config
from .database import init_db

def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
        app.config.from_object(config_class)
            app.config.from_pyfile('config.py', silent=True)

                with app.app_context():
                        init_db(app)

                            return create_app