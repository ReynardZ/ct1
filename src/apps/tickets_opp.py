from flask import (request,
                   render_template,
                   Blueprint, flash,
                   session,
                   url_for, redirect,
                   )
from src.forms import SearchForm, ConcertForm
from src.apps.advanced_search import format_sql
from src.models import Models
import logging

models = Models()
to = Blueprint('tickets', __name__)


@to.route('/tickets')
def tickets():
    if session.get('status'):
        concerts = models.get_concerts_data()
        return render_template('tickets.html', concerts=concerts)
    else:
        return redirect(url_for('users.sign_in'))


@to.route('/data_add', methods=['GET', 'POST'])
def data_add():
    if request.method == "GET":
        return render_template('data_add.html')
    else:
        form = ConcertForm(request.form)
        if form.validate():
            models.add_concert({'id': form.id.data,
                                'name': form.name.data,
                                'genre': form.genre.data,
                                'artist': form.artist.data})
            flash("Data with ID({})has already inserted into concert_dimension.".format(form.id.data))
        else:
            flash("All data should be input. Length for Concert ID should be 8.")
        return render_template('data_add.html')


@to.route('/search', methods=["GET", "POST"])
def search_page():
    if request.method == "GET":
        return render_template('search.html')
    else:
        form = SearchForm(request.form)
        statement = format_sql(form)
        logging.info(statement)
        num, results = models.advanced_search(statement)
        flash("There are total {} results found".format(num))
        return render_template('search.html', results=results)


@to.route('/modify/<c_id>/<concert_name>/<genre>/<artist_name>')
def modify(c_id, concert_name, genre, artist_name):
    return render_template('modify.html',
                           c_id=c_id,
                           concert_name=concert_name,
                           genre=genre,
                           artist_name=artist_name)


@to.route('/delete/<c_id>')
def delete_data(c_id):
    models.delete_data(c_id)
    return redirect(url_for('tickets.tickets'))


@to.route('/update', methods=['GET', 'POST'])
def update_data():
    form = ConcertForm(request.form)
    print('{}|{}|{}|{}'.format(form.id.data, form.name.data, form.genre.data, form.artist.data))
    if form.validate():
        models.update_data(form.id.data, form.name.data, form.genre.data, form.artist.data)
        flash("Data with ID({})has already modified".format(form.id.data))
        return redirect(url_for('tickets.tickets'))
    else:
        flash("All data should be input.")
        return redirect(url_for('tickets.tickets'))

