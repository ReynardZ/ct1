import os
from flask import Flask
from src.apps.users import auth
from src.apps.tickets_opp import to
from src.apps.main import main

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
app.SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
app.register_blueprint(main)
app.register_blueprint(auth)
app.register_blueprint(to)
