import os
from flask import Flask
from .apps.main import main
from .apps.users import auth
from .apps.tickets_opp import to


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
app.SQLALCHEMY_DATABASE_URI = 'postgres://sfgfsntzceuzfr:2308dd0efa4e1ef829c8ed17b481707285d8a0ee81a92a020cda7339c51a751a@ec2-35-170-21-76.compute-1.amazonaws.com:5432/dek4ggasgftq1t'
app.register_blueprint(main)
app.register_blueprint(auth)
app.register_blueprint(to)
