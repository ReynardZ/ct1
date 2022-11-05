import os
from flask import Flask, render_template
from src.apps.users import auth
from src.apps.tickets_opp import to
from src.apps.main import main
from src.db_init import init_database
from src.models import Models


def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY")
    app.SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(to)
    models = Models()
    models.initialize()
    init_database('src/data.sql', models)
    return app


# model = Models()

