import os
from flask import Flask
from apps.main import main
from apps.users import auth
from apps.tickets_opp import to


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
app.SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL?sslmode=require').replace('postgres://', 'postgresql://')
app.register_blueprint(main)
app.register_blueprint(auth)
app.register_blueprint(to)
