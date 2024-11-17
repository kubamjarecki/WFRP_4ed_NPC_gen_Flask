from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired


class BasicCharacterForm(FlaskForm):
    race = None
    klass = None


