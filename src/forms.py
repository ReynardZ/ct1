import wtforms
from wtforms.validators import length, email, DataRequired


class SignInForm(wtforms.Form):
    email = wtforms.EmailField(validators=[length(min=5, max=30), email()])
    password = wtforms.PasswordField(validators=[length(min=4, max=20)])


class RegisterForm(wtforms.Form):
    email = wtforms.EmailField(validators=[length(min=5, max=30), email()])
    password = wtforms.PasswordField(validators=[length(min=4, max=20)])
    area = wtforms.StringField()
    age = wtforms.IntegerField()


class SearchForm(wtforms.Form):
    concert = wtforms.StringField('concert')
    artist = wtforms.StringField('artist')
    venue = wtforms.StringField('venue')
    min = wtforms.StringField('min')
    max = wtforms.StringField('max')
    month = wtforms.StringField('month')
    day = wtforms.StringField('day')
    year = wtforms.StringField('year')


class ConcertForm(wtforms.Form):
    id = wtforms.StringField('id', validators=[length(min=8, max=8)])
    name = wtforms.StringField('name', validators=[DataRequired()])
    genre = wtforms.StringField('genre', validators=[DataRequired()])
    artist = wtforms.StringField('artist', validators=[DataRequired()])
