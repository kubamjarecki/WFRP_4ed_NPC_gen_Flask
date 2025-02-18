from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, SelectField, IntegerField, BooleanField
from wtforms.validators import NumberRange



class CreationFormOne(FlaskForm):

    #########################
    ### buduje listę ras ####
    #########################
    tabela_ras = {1: "Leśny elf", 2: "Wysoki elf", 3: "Krasnolud", 4: "Niziołek", 5: "Człowiek"}
    race_choices = []
    for race_id, race_name in tabela_ras.items():
        tupel = (race_name, race_name)
        race_choices.append(tupel)
    losowo = ('Losowo', 'Losowo')
    race_choices.append(losowo)
    #####################################
    ###### buduje liste profesji#########
    #####################################

    tabela_wszystkich_profesji = {
    0: 'Agitator', 1: 'Aptekarz', 2: 'Artysta', 3: 'Banita', 4: 'Biczownik', 5: 'Chłop', 6: 'Czarodziej',
    7: 'Czarownica', 8: 'Doker', 9: 'Domokrążca', 10: 'Doradca', 11: 'Flisak', 12: 'Gladiator', 13: 'Guślarz',
    14: 'Górnik', 15: 'Hiena Cmentarna', 16: 'Inżynier', 17: 'Kapłan', 18: 'Kapłan Bitewny', 19: 'Kawalerzysta',
    20: 'Kuglarz', 21: 'Kupiec', 22: 'Medyk', 23: 'Mieszczanin', 24: 'Mistyk', 25: 'Mnich', 26: 'Namiestnik',
    27: 'Ochroniarz', 28: 'Oprych', 29: 'Paser', 30: 'Pilot Rzeczny', 31: 'Pirat Rzeczny', 32: 'Poseł',
    33: 'Posłaniec', 34: 'Prawnik', 35: 'Przemytnik', 36: 'Przewoźnik', 37: 'Rajfur', 38: 'Rekietier',
    39: 'Rycerz', 40: 'Rzemieślnik', 41: 'Strażnik', 42: 'Strażnik Dróg', 43: 'Strażnik Rzeczny', 44: 'Szarlatan',
    45: 'Szczurołap', 46: 'Szlachcic', 47: 'Szpieg', 48: 'Służący', 49: 'Uczony', 50: 'Woźnica', 51: 'Zabójca',
    52: 'Zarządca', 53: 'Zielarz', 54: 'Zwadźca', 55: 'Zwiadowca', 56: 'Złodziej', 57: 'Łowca',
    58: 'Łowca Czarownic', 59: 'Łowca Nagród', 60: 'Śledczy', 61: 'Żebrak', 62: 'Żeglarz', 63: 'Żołnierz'}
    profession_choices = [('Losowo', 'Losowo')]
    for prof_id, prof_name in tabela_wszystkich_profesji.items():
        tupel = (prof_name, prof_name)
        profession_choices.append(tupel)

    #########################
    ## pola wyboru ##########
    #########################
    race = RadioField('Wybierz rasę',
                      choices= race_choices,
                      default= 'Losowo')
    name = StringField('Imię')
    sex = RadioField('Wybierz płeć',
                     choices=[('Mężczyzna', 'Mężczyzna'), ('Kobieta', 'Kobieta')],
                     default='Mężczyzna')

    profession = RadioField('Wybierz profesję',
                             choices=profession_choices,
                             default='Losowo')

    level = SelectField(f'Wybierz poziom postaci.(Nr oznacza ukończoną profesję):',
                        choices=[(0,0),('1',1),(2,2),(3,3),(4,4)],
                        default='0', coerce=int)
    #########################
    #### przyciski ##########
    #########################
    dalej = SubmitField('Dalej') #render_kw= {"class": "btn btn-primary mr-3"})
    losuj_reszte = SubmitField('Losuj Resztę') #render_kw={"class": "btn btn-primary"})


class CreationFormTwo(FlaskForm):
    class Meta:
        csrf = False  # Wyłącz CSRF dla testów

    def __init__(self, dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dict = dict
        self.choosable_talent_list = dict['talenty_lista_liczba']
        self.count = len(self.choosable_talent_list)

        # Debugowanie: sprawdzenie ile mamy talentów
        print(f"Liczba talentów: {self.count}")

        # Dynamiczne tworzenie dropdownów
        for i in range(self.count):
            options = self.choosable_talent_list[i]
            talent_field_name = f'talent_{i+1}'
            field = SelectField(
                f'Talent {i+1}',
                choices=[(option, option) for option in options],
                #render_kw={'id': f'talent_{i+1}'}  # Ustawienie ID ręcznie
            )
            # Dodanie pola do formularza przy użyciu _fields
            field.id = talent_field_name
            field_name = f'talent_{i+1}'
            self._fields[field_name] = field


    WW = IntegerField('WW', validators=[NumberRange(min=2, max=20)])
    US = IntegerField('US', validators=[NumberRange(min=2, max=20)])
    S = IntegerField('S', validators=[NumberRange(min=2, max=20)])
    Wt = IntegerField('Wt', validators=[NumberRange(min=2, max=20)])
    I = IntegerField('I', validators=[NumberRange(min=2, max=20)])
    Zw = IntegerField('Zw', validators=[NumberRange(min=2, max=20)])
    Zr = IntegerField('Zr', validators=[NumberRange(min=2, max=20)])
    Int = IntegerField('Int', validators=[NumberRange(min=2, max=20)])
    SW = IntegerField('SW', validators=[NumberRange(min=2, max=20)])
    Ogd = IntegerField('Ogd', validators=[NumberRange(min=2, max=20)])

    losuj = BooleanField('Losuj', default=False)

    dalej = SubmitField('Dalej')
    losuj_reszte = SubmitField('Losuj Resztę')



