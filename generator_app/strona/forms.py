from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, RadioField
from wtforms.validators import DataRequired



class CreationForm(FlaskForm):
    tabela_ras = {
        1: "Leśny elf", 2: "Wysoki elf", 3: "Krasnolud", 4: "Niziołek", 5: "Człowiek"
    }
    race_choices = []
    for race_id, race_name in tabela_ras.items():
        tupel = (race_name, race_name)
        race_choices.append(tupel)
    losowo = ('Losowo', 'Losowo')
    race_choices.append(losowo)
    race = RadioField('Wybierz rasę',
                      choices= race_choices,
                      default= 'Losowo')
    name = StringField('Imię')
    sex = RadioField('Wybierz płeć',
                     choices=[('Mężczyzna', 'Mężczyzna'), ('Kobieta', 'Kobieta')],
                     default='M')



