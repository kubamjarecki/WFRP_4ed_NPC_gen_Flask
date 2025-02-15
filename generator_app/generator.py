import random
from classes import RaceTraits
class Postac:
    def __init__(self, form):
        self.form = form
        self.race = form.race.data
        self.name=form.name.data
        self.sex=form.sex.data
        self.profession=form.profession.data

    def generate_postac(self):


        if self.race == "Losowo":
            K100 = random.randint(1, 100)
            lesny = [100]
            wysoki = [99]
            kras = [98, 97, 96, 95]
            hobbit = [94, 93, 92, 91]
            if K100 in wysoki:
                race = "Wysoki elf"
            if K100 in lesny:
                self.race = "Leśny elf"
            if K100 in kras:
                self.race = "Krasnolud"
            if K100 in hobbit:
                self.race = "Niziołek"
            if K100 < 91:
                self.race = "Człowiek"
        ###########################################
        ### pobieramy rzeczy zależne od rasy ######
        ###########################################
        if self.race == "Wysoki elf":
            from rasy.wysoki_elf import losowanie_imienia, profesje
            nazwa = self.race
        if self.race == "Leśny elf":
            from rasy.lesny_elf import losowanie_imienia, profesje
        if self.race == "Krasnolud":
            from rasy.khazad import losowanie_imienia, profesje
            nazwa = self.race
        if self.race == "Niziołek":
            from rasy.hobbit import losowanie_imienia, profesje
            nazwa = self.race
        if self.race == "Człowiek":
            from rasy.czlowiek import losowanie_imienia, profesje
            nazwa = self.race

        ################################
        ## losujemy imię ###############
        ################################

        if self.name == "":
            self.name = losowanie_imienia(self.sex)

        #print(self.name, self.sex, self.race)

        ######################################
        ##### losujemy profesję ###############
        ######################################
        if self.profession == "Losowo":
            rand = random.randint(0,100)
            self.profession = profesje[rand]


        #print(self.profession)
        #print(self.race)
        #print(self.sex)
        #print(self.name)
        #print(self.wzrost)

        ############################################################################
        ######### tworzę słownik do przekazania do następnego widoku ###############
        ############################################################################
        postac_slownik = {
            "imie": self.name,
            "plec": self.sex,
            "rasa": self.race,
            "profesja": self.profession,
        }

        return postac_slownik

