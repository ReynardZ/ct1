from flask import (request,
                   render_template,
                   redirect,
                   Blueprint,
                   url_for,
                   session,
                   flash)
from src.forms import RegisterForm, SignInForm
from src.models import Models

auth = Blueprint('users', __name__)
models = Models()


@auth.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'GET':
        if session.get('status'):
            return redirect(url_for('tickets.tickets'))
        else:
            return render_template('login.html')
    else:
        form = SignInForm(request.form)
        if form.validate():
            if models.get_user_password(form.email.data) == form.password.data:
                session['user'] = form.email.data
                session['status'] = True
                return redirect(url_for('tickets.tickets'))
            else:
                flash("Email does not match with the password.")
                return redirect(url_for('users.sign_in'))
        else:
            flash("Formatting of the email or password is wrong")
            return redirect(url_for('users.sign_in'))


@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        session.clear()
        return render_template('register.html')
    else:
        form = RegisterForm(request.form)
        if form.validate():
            models.create_user({'email': form.email.data,
                                'password': form.password.data,
                                'area': form.area.data,
                                'age': form.age.data}
                               )
            flash("User {} created successfully".format(form.email.data))
            return redirect(url_for('users.sign_in'))
        else:
            flash("Formatting of the email or password is wrong")
            return redirect(url_for('users.sign_up'))


@auth.route('/sign_out', methods=['GET', 'POST'])
def sign_out():
    session.clear()
    return redirect(url_for('main.index'))
