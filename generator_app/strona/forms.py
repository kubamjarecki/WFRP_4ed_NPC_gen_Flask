from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, RadioField, SelectField, IntegerField, BooleanField, widgets,
                     SelectMultipleField)
from wtforms.validators import NumberRange, ValidationError



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

def validate_choices(form, field):
    if not (len(field.data) == 3):
        raise ValidationError("Musisz wybrać dokładnie 3 opcje.")

class CreationFormDvarf(FlaskForm):
    #cechy
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

    #Talenty
    field_1 = SelectField('Talent 1',
        choices=[("Czytanie/Pisanie","Czytanie/Pisanie"), ("Nieustępliwy","Nieustępliwy")])

    field_2 = SelectField('Talent 2',
                          choices=[("Odporność Psychiczna","Odporność Psychiczna"), ("Nieugięty", "Nieugięty")])
    @property
    def fields(self):
        return [self.field_1, self.field_2]

    #Umiejki
    umiejki = ["Broń Biała (WW) (Podstawowa)",
               "Język (Int) (Khazalid)",
               "Opanowanie (SW)",
               "Mocna Głowa (Wt)",
               "Rzemiosło (Zr) (Dowolne)",
               "Wiedza (Int) (Geologia)",
               "Wiedza (Int) (Krasnoludy)",
               "Wiedza (Int) (Metalurgia)",
               "Wycena (Int)",
               "Występy (Ogd) (Gawędziarstwo)",
               "Zastraszanie (S)"]

    skill_choices = []
    for skill in umiejki:
        tupel = (skill, skill)
        skill_choices.append(tupel)

    pola_umiejek5 = SelectMultipleField('Wybierz opcje:', choices=skill_choices,
                                        option_widget=widgets.CheckboxInput(),
                                        widget=widgets.ListWidget(prefix_label=False),
                                        validators=[validate_choices]
                                        )
    pola_umiejek3 = SelectMultipleField('Wybierz opcje:', choices=skill_choices,
                                        option_widget=widgets.CheckboxInput(),
                                        widget=widgets.ListWidget(prefix_label=False),
                                        validators=[validate_choices]
                                        )

    # guziki


    losuj = BooleanField('Losuj', default=False)

    dalej = SubmitField('Dalej')
    losuj_reszte = SubmitField('Losuj Resztę')





class CreationFormWoodElf(FlaskForm):
    #cechy
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

    #Talenty
    field_1 = SelectField('Talent 1',
        choices= [("Twardziel", "Twardziel"),
                  ("Percepcja Magiczna","Percepcja Magiczna")])

    field_2 = SelectField('Talent 2',
                          choices=[("Czytanie/Pisanie", "Czytanie/Pisanie"),
                                   ("Niezwykle Odporny", "Niezwykle Odporny")])
    @property
    def fields(self):
        return [self.field_1, self.field_2]

    #Umiejki
    umiejki = ["Atletyka (Zw)", "Broń Biała (WW) (Podstawowa)", "Broń Zasięgowa (US) (Łuk)", "Język (Int) (Eltharin)",
               "Odporność (Wt)", "Percepcja (I)", "Skradanie (Zw)", "Sztuka Przetrwania (Int)", "Tropienie (I)",
               "Wspinaczka (S)", "Występy (Ogd) (Śpiewanie)", "Zastraszanie (S)"]

    skill_choices = []
    for skill in umiejki:
        tupel = (skill, skill)
        skill_choices.append(tupel)

    pola_umiejek5 = SelectMultipleField('Wybierz opcje:', choices=skill_choices,
                                        option_widget=widgets.CheckboxInput(),
                                        widget=widgets.ListWidget(prefix_label=False),
                                        validators=[validate_choices]
                                        )
    pola_umiejek3 = SelectMultipleField('Wybierz opcje:', choices=skill_choices,
                                        option_widget=widgets.CheckboxInput(),
                                        widget=widgets.ListWidget(prefix_label=False),
                                        validators=[validate_choices]
                                        )

    #guziki
    losuj = BooleanField('Losuj', default=False)
    dalej = SubmitField('Dalej')
    losuj_reszte = SubmitField('Losuj Resztę')



class CreationFormHighElf(FlaskForm):
    # cechy
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

    # Talenty
    talenty2 = ["Szósty Zmysł", "Percepcja Magiczna"]
    talenty3 = ["Błyskotliwość", "Zimna Krew"]
    field_1 = SelectField('Talent 1',
                          choices=[("Szósty Zmysł", "Szósty Zmysł"),
                                   ("Percepcja Magiczna", "Percepcja Magiczna")])

    field_2 = SelectField('Talent 2',
                          choices=[("Błyskotliwość", "Błyskotliwość"),
                                   ("Zimna Krew", "Zimna Krew")])

    @property
    def fields(self):
        return [self.field_1, self.field_2]

    # Umiejki
    umiejki = ["Broń Biała (WW) (Podstawowa)", "Broń Zasięgowa (US) (Łuk)", "Dowodzenie (Ogd)",
               "Język (Int) (Eltharin)", "Muzyka (Zr)(Dowolny instrument)", "Nawigacja (I)", "Opanowanie (SW)",
               "Pływanie (S)", "Percepcja (I)", "Wycena (Int)", "Występy (Ogd) (Śpiewanie)", "Żeglarstwo (Zw)"]

    skill_choices = []
    for skill in umiejki:
        tupel = (skill, skill)
        skill_choices.append(tupel)

    pola_umiejek5 = SelectMultipleField('Wybierz opcje:', choices=skill_choices,
                                        option_widget=widgets.CheckboxInput(),
                                        widget=widgets.ListWidget(prefix_label=False),
                                        validators=[validate_choices]
                                        )
    pola_umiejek3 = SelectMultipleField('Wybierz opcje:', choices=skill_choices,
                                        option_widget=widgets.CheckboxInput(),
                                        widget=widgets.ListWidget(prefix_label=False),
                                        validators=[validate_choices]
                                        )

    # guziki
    losuj = BooleanField('Losuj', default=False)
    dalej = SubmitField('Dalej')
    losuj_reszte = SubmitField('Losuj Resztę')


class CreationFormMan(FlaskForm):
    def validate_choices(form, field):
        if not (len(field.data) == 3):
            raise ValidationError("Musisz wybrać dokładnie 3 opcje.")
    # cechy
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

    # Talenty
    field_1 = SelectField('Talent 1',
                          choices=[(" Błyskotliwość", " Błyskotliwość"),
                                   ("Charyzmatyczny", "Charyzmatyczny")])

    @property
    def fields(self):
        return [self.field_1]

    # Umiejki
    umiejki = ["Broń Biała (WW) (Podstawowa)", "Broń Zasięgowa (US) (Łuk)", "Charyzma (Ogd) ", "Dowodzenie (Ogd)",
               "Język (Int) (bretoński)", "Język (Int) (Jałowej Krainy)", "Opanowanie (SW)",
               "Opieka nad Zwierzętami (Int)", "Plotkowanie (Ogd)", "Targowanie (Ogd)", "Wiedza (Int) (Reikland)",
               "Wycena (Int)"]
    skill_choices = []
    for skill in umiejki:
        tupel = (skill, skill)
        skill_choices.append(tupel)

    pola_umiejek5 = SelectMultipleField('Wybierz opcje:', choices=skill_choices,
                                        option_widget=widgets.CheckboxInput(),
                                        widget=widgets.ListWidget(prefix_label=False),
                                        validators=[validate_choices]
    )
    pola_umiejek3 = SelectMultipleField('Wybierz opcje:', choices=skill_choices,
                                       option_widget=widgets.CheckboxInput(),
                                       widget=widgets.ListWidget(prefix_label=False),
                                       validators=[validate_choices]
    )

    #guziki
    losuj = BooleanField('Losuj', default=False)
    dalej = SubmitField('Dalej')
    losuj_reszte = SubmitField('Losuj Resztę')


class CreationFormHalfing(FlaskForm):
    # cechy
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


    @property
    def fields(self):
        return []

    # Umiejki
    umiejki = ["Charyzma (Ogd) ", "Hazard (Int)", "Intuicja (I)", "Język (Int) (Krainy Zgromadzenia)",
               "Mocna Głowa (Wt)", "Percepcja (I)", "Rzemiosło (Zr) (Kucharz)", "Skradanie (Zw) (Dowolne)",
               "Targowanie (Ogd)", "Unik (Zw)", "Wiedza (Int) (Reikland)", "Zwinne Palce (Zr)"]

    skill_choices = []
    for skill in umiejki:
        tupel = (skill, skill)
        skill_choices.append(tupel)

    pola_umiejek5 = SelectMultipleField('Wybierz opcje:', choices=skill_choices,
                                        option_widget=widgets.CheckboxInput(),
                                        widget=widgets.ListWidget(prefix_label=False),
                                        validators=[validate_choices]
    )
    pola_umiejek3 = SelectMultipleField('Wybierz opcje:', choices=skill_choices,
                                       option_widget=widgets.CheckboxInput(),
                                       widget=widgets.ListWidget(prefix_label=False),
                                       validators=[validate_choices]
    )

    #guziki
    losuj = BooleanField('Losuj', default=False)
    dalej = SubmitField('Dalej')
    losuj_reszte = SubmitField('Losuj Resztę')

