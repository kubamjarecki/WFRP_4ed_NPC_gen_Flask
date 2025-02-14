import random
from classes import RaceTraits
class Postac:
    def __init__(self, form):
        self.form = form
        self.race = form.race.data
        self.name=form.name.data
        self.sex=form.sex.data

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
            from rasy.wysoki_elf import cechy, szybkosc, punkty_bohatera0, punkty_przeznaczenia0, \
                punkty_wolne, profesje, umiejki, talentyx, wzrost, imiex_m, imiex_z, wlosy, oczy
            nazwa = self.race
        if self.race == "Leśny elf":
            from rasy.lesny_elf import cechy, szybkosc, punkty_bohatera0, punkty_przeznaczenia0, \
                punkty_wolne, profesje, umiejki, talentyx, wzrost, imiex_m, imiex_z, wlosy, oczy
            nazwa = self.race
        if self.race == "Krasnolud":
            from rasy.khazad import cechy, szybkosc, punkty_bohatera0, punkty_przeznaczenia0, \
                punkty_wolne, profesje, umiejki, talentyx, wzrost, imiex_m, imiex_z, wlosy, oczy
            nazwa = self.race
        if self.race == "Niziołek":
            from rasy.hobbit import cechy, szybkosc, punkty_bohatera0, punkty_przeznaczenia0, \
                punkty_wolne, profesje, umiejki, talentyx, wzrost, imiex_m, imiex_z, wlosy, oczy
            nazwa = self.race
        if self.race == "Człowiek":
            from rasy.czlowiek import cechy, szybkosc, punkty_bohatera0, punkty_przeznaczenia0, \
                punkty_wolne, profesje, umiejki, talentyx, wzrost, imiex_m, imiex_z, wlosy, oczy
            nazwa = self.race
        #self.race_traits =RaceTraits(nazwa = nazwa, cechy = cechy, sz = szybkosc, pb = punkty_bohatera0, pp = punkty_przeznaczenia0, p0 = punkty_wolne, profesje = profesje, umiejki = umiejki, talenty=talentyx, wzrost=wzrost, imiex_m=imiex_m, imiex_z=imiex_z, wlosy = wlosy, oczy=oczy )
        ################################
        ## losujemy imię ###############
        ################################

        if self.name == "":
            if self.sex == "Kobieta":
                self.name = imiex_z
            if self.sex == "Mężczyzna":
                self.name = imiex_m
            

        return f"Twoja {self.sex} to {self.race}, a imię {self.name}"
