import os
from flask import Flask, render_template
from src.apps.users import auth
from src.apps.tickets_opp import to

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
app.SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
app.register_blueprint(auth)
app.register_blueprint(to)


# model = Models()
@app.route('/')
def index():  # put application's code here
    return render_template('index.html')
