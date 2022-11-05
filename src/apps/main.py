from flask import render_template, Blueprint

main = Blueprint('main', __name__)


@main.route('/')
def index():  # put application's code here
    return render_template('index.html')
