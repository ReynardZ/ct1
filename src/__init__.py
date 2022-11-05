import os
from flask import Flask
from .apps.main import main
from .apps.users import auth
from .apps.tickets_opp import to


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
app.SQLALCHEMY_DATABASE_URI = 'postgresql://clrszdrdunindu:b288f70cd2caeeb05a4535803df42a30831de20ad32be2ca7da5fa4b98fdde49@ec2-44-199-22-207.compute-1.amazonaws.com:5432/d48rt1aso8gj3h'
app.register_blueprint(main)
app.register_blueprint(auth)
app.register_blueprint(to)
