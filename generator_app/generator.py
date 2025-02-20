import random
import importlib
import unicodedata



class Postac:

    def __init__(self, form):
        self.form = form
        self.race = form.race.data
        self.name=form.name.data
        self.sex=form.sex.data
        self.profession=form.profession.data
        self.level = form.level.data
        self.experience = None
        self.talenty_lista_liczba = None
        self.klasa = None
        self.nazwa_profesji = None
        self.status = None
        self.rozwiniecia_cech = None
        self.slownik_umiejetnosci_oraz_levelu = None
        self.talenty = None
        self.wyp = None
        self.waga = None
        self.talents = []
        self.skills_to_choose = []
        self.tabela_losowych_talentow = {
            1: 'Atrakcyjny', 2: 'Atrakcyjny', 3: 'Atrakcyjny', 4: 'Bardzo Silny', 5: 'Bardzo Silny',
            6: 'Bardzo Silny', 7: 'Błękitna Krew', 8: 'Błękitna Krew', 9: 'Błyskotliwość', 10: 'Błyskotliwość',
            11: 'Błyskotliwość', 12: 'Charyzmatyczny', 13: 'Charyzmatyczny', 14: 'Charyzmatyczny',
            15: 'Chodu!', 16: 'Chodu!', 17: 'Chodu!', 18: 'Czujny', 19: 'Czujny', 20: 'Czujny',
            21: 'Czysta Dusza', 22: 'Czysta Dusza', 23: 'Czysta Dusza', 24: 'Czysta Dusza', 25: 'Czytanie/Pisanie',
            26: 'Czytanie/Pisanie', 27: 'Czytanie/Pisanie', 28: 'Geniusz Arytmetyczny', 29: 'Geniusz Arytmetyczny',
            30: 'Geniusz Arytmetyczny', 31: 'Geniusz Arytmetyczny', 32: 'Naśladowca', 33: 'Naśladowca',
            34: 'Naśladowca', 35: 'Niezwykle Odporny', 36: 'Niezwykle Odporny', 37: 'Niezwykle Odporny',
            38: 'Oburęczność', 39: 'Oburęczność', 40: 'Oburęczność', 41: 'Odporny na (Dowolne Zagrożenie)',
            42: 'Odporny na (Dowolne Zagrożenie)', 43: 'Odporny na (Dowolne Zagrożenie)', 44: 'Poliglota',
            45: 'Poliglota', 46: 'Poliglota', 47: 'Posłuch u Zwierząt', 48: 'Posłuch u Zwierząt',
            49: 'Posłuch u Zwierząt', 50: 'Silne Nogi', 51: 'Silne Nogi', 52: 'Silne Nogi', 53: 'Słuch Absolutny',
            54: 'Słuch Absolutny', 55: 'Słuch Absolutny', 56: 'Strzelec Wyborowy', 57: 'Strzelec Wyborowy',
            58: 'Strzelec Wyborowy', 59: 'Szczęście', 60: 'Szczęście', 61: 'Szczęście', 62: 'Szczęście',
            63: 'Szósty Zmysł', 64: 'Szósty Zmysł', 65: 'Szósty Zmysł', 66: 'Szósty Zmysł', 67: 'Szybki Refleks',
            68: 'Szybki Refleks', 69: 'Szybki Refleks', 70: 'Talent Artystyczny', 71: 'Talent Artystyczny',
            72: 'Talent Artystyczny', 73: 'Tragarz', 74: 'Tragarz', 75: 'Tragarz', 76: 'Twardziel',
            77: 'Twardziel', 78: 'Twardziel', 79: 'Twardziel', 80: 'Urodzony Wojownik', 81: 'Urodzony Wojownik',
            82: 'Urodzony Wojownik', 83: 'Widzenie w Ciemności', 84: 'Widzenie w Ciemności',
            85: 'Widzenie w Ciemności', 86: 'Wyczucie Kierunku', 87: 'Wyczucie Kierunku',
            88: 'Wyczucie Kierunku', 89: 'Wyczulony Zmysł (Dowolny)', 90: 'Wyczulony Zmysł (Dowolny)',
            91: 'Wyczulony Zmysł (Dowolny)', 92: 'Wytwórca (Dowolny)', 93: 'Wytwórca (Dowolny)',
            94: 'Wytwórca (Dowolny)', 95: 'Zimna Krew', 96: 'Zimna Krew', 97: 'Zimna Krew', 98: 'Zręczny',
            99: 'Zręczny', 100: 'Zręczny'
        }


    def generate_race_name_profession(self):
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
            from rasy.wysoki_elf import losowanie_imienia, profesje, talentyx
        if self.race == "Leśny elf":
            from rasy.lesny_elf import losowanie_imienia, profesje, talentyx
        if self.race == "Krasnolud":
            from rasy.khazad import losowanie_imienia, profesje, talentyx
        if self.race == "Niziołek":
            from rasy.hobbit import losowanie_imienia, profesje, talentyx
        if self.race == "Człowiek":
            from rasy.czlowiek import losowanie_imienia, profesje, talentyx

        self.talenty_lista_liczba=talentyx

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
            rand = random.randint(1,100)
            self.profession = profesje[rand]


        #######################################
        ###### określamy doświadczenie ########
        #######################################
    def give_experience(self):
        doswiadczenie = {
            "0": "zielony",
            "1": "początkujący",
            "2": "znający swój fach",
            "3": "doświadczony",
            "4": "mistrzowski"
        }
        self.experience = doswiadczenie[str(self.level)]

    def draw_talents(self):
        if isinstance(self.talenty_lista_liczba[-1], int):
            while True:
                liczba = self.talenty_lista_liczba[-1]
                los = random.sample(range(1, 100), liczba)
                for i in los:
                    self.talents.append(self.tabela_losowych_talentow[i])
                if len(self.talents) == len(set(self.talents)):
                    self.talenty_lista_liczba.pop()
                    break
                else:
                    self.talents = []

            while isinstance(self.talenty_lista_liczba[-1], str):
                self.talents.append(self.talenty_lista_liczba[-1])
                self.talenty_lista_liczba.pop()
                if len(self.talenty_lista_liczba)==0:
                    break


    def get_profession_traits_and_add_to_character(self):
        folder = 'profesje'
        file = self.profession.lower()
        # pozbywam się polskich znaków :/ moduł robiący to automatycznie, jest zjebane dla języka polskiego i usuwa ł, zamiast zamienić na l
        file = file.replace("ł", "l")
        file = file.replace(" ", "_")
        normalized = unicodedata.normalize("NFKD", file)
        file = normalized.encode("ASCII", "ignore").decode("utf-8")
        module_name = f'{folder}.{file}'
        profesja_variables = importlib.import_module(module_name)
        self.klasa=profesja_variables.klasa,
        self.nazwa_profesji=profesja_variables.nazwa_profesji,
        self.status=profesja_variables.status,
        self.rozwiniecia_cech=profesja_variables.rozwiniecia_cech,
        self.slownik_umiejetnosci_oraz_levelu=profesja_variables.slownik_umiejetnosci_oraz_levelu,
        self.talenty=profesja_variables.talenty,
        self.wyp=profesja_variables.wyp,
        self.waga=profesja_variables.waga


    def generate_json_readable_output(self):
        ############################################################################
        ######### tworzę słownik do przekazania do następnego widoku ###############
        ############################################################################
        postac_slownik = {
            "imie": self.name,
            "plec": self.sex,
            "rasa": self.race,
            "profesja": self.profession,
            "poziom": self.level,
            "talenty": self.talents,
            "doswiadczenie": self.experience,
            "klasa": self.klasa,
            "nazwa_profesji": self.nazwa_profesji,
            "status": self.status,
            "rozwiniecia_cech": self.rozwiniecia_cech,
            "slownik_umiejetnosci_oraz_levelu": self.slownik_umiejetnosci_oraz_levelu,
            'talenty_lista_liczba':self.talenty_lista_liczba
        }


        return postac_slownik



class PostacTalentyIUmiejki:
    def __init__(self, postac_slownik):
        self.race = postac_slownik['rasa']
        self.profession = postac_slownik['profesja']
        self.name = postac_slownik['imie']
        self.sex = postac_slownik['plec']
        self.level = postac_slownik['poziom']



    def draw_random_talents(self):
        if isinstance(self.talenty_lista[-1], int):
            while True:
                liczba = self.talenty_lista[-1]
                los = random.sample(range(1, 100), liczba)
                for i in los:
                    self.talents.append(self.tabela_losowych_talentów[i])
                if len(self.talents) == len(set(self.talents)):
                    self.talenty_lista.pop()
                    break
                else:
                    self.talents = []



    # def generate_talenty_i_umiejki(self):
    #     if self.race == "Wysoki elf":
    #         from rasy.wysoki_elf import
    #     if self.race == "Leśny elf":
    #         from rasy.lesny_elf import losowanie_imienia, profesje
    #     if self.race == "Krasnolud":
    #         from rasy.khazad import losowanie_imienia, profesje
    #     if self.race == "Niziołek":
    #         from rasy.hobbit import losowanie_imienia, profesje
    #     if self.race == "Człowiek":
    #         from rasy.czlowiek import losowanie_imienia, profesje
