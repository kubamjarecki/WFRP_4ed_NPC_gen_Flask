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
        self.wyp = None
        self.waga = None
        self.talents = []
        self.skills = {}
        self.cechy = {}
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
        self.slownik_talentow_i_level = {}
        self.equipment = []
        #print(self.cechy)

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
            from rasy.wysoki_elf import losowanie_imienia, profesje, talentyx, cechy
        if self.race == "Leśny elf":
            from rasy.lesny_elf import losowanie_imienia, profesje, talentyx, cechy
        if self.race == "Krasnolud":
            from rasy.khazad import losowanie_imienia, profesje, talentyx, cechy
        if self.race == "Niziołek":
            from rasy.hobbit import losowanie_imienia, profesje, talentyx, cechy
        if self.race == "Człowiek":
            from rasy.czlowiek import losowanie_imienia, profesje, talentyx, cechy

        self.cechy = cechy

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
        for element in self.talenty_lista_liczba:
            if isinstance(element, str):
                self.talents.append(element)
        if isinstance(self.talenty_lista_liczba[-1], int):
            liczba = self.talenty_lista_liczba[-1]
            while liczba > 0:
                los = random.randint(1, 100)
                if self.tabela_losowych_talentow[los] not in self.talents:
                    self.talents.append(self.tabela_losowych_talentow[los])
                    liczba -= 1
                else:
                    continue



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
        self.klasa=profesja_variables.klasa
        self.nazwa_profesji=profesja_variables.nazwa_profesji
        self.status=profesja_variables.status
        self.rozwiniecia_cech=profesja_variables.rozwiniecia_cech
        self.slownik_umiejetnosci_oraz_levelu=profesja_variables.slownik_umiejetnosci_oraz_levelu
        self.slownik_talentow_i_level = profesja_variables.talenty
        self.wyp=profesja_variables.wyp
        self.waga=profesja_variables.waga

    def unpack_profession_talents(self):
        for key, value in self.slownik_talentow_i_level.items():
            if (value + self.level) > 0:
                self.talents.append(key)


    def unpack_profession_skills(self):
        for key, value in self.slownik_umiejetnosci_oraz_levelu.items():
            #print(key, value)
            val = value + self.level
            if val > 0:
                v=5*val
                self.skills[key]=v

    def unpack_equipment(self):
        count = self.level
        for element in self.wyp[0]:
            self.equipment.append(element)

        for element in self.wyp[1]:
            self.equipment.append(element)
        if self.level >= 2:
            for element in self.wyp[2]:
                self.equipment.append(element)
        if self.level >= 3:
            for element in self.wyp[3]:
                self.equipment.append(element)
                self.equipment.append(element)
        if self.level == 4:
            for element in self.wyp[4]:
                self.equipment.append(element)
    def create_gold_str_and_append_to_character_equipment(self):
        status = self.status[self.level]
        if status == "Złoto":
            majatek = "1 ZK"
        if status == "Srebro":
            a = random.randint(1, 10)
            majatek = f"{a} SS"
        if status == "Brąz":
            a = random.randint(2, 20)
            majatek = f"{a} BP"
        self.equipment.append(majatek)

    def generate_json_readable_output(self):
        ############################################################################
        ######### tworzę słownik do przekazania do następnego widoku ###############
        ############################################################################
        postac_slownik = {
        }

        for attr, value in vars(self).items():
            if attr != "form":
                #print(f"{attr}: {value}")
                postac_slownik[attr] = value

        return postac_slownik

class PostacTalentyIUmiejki:
    def __init__(self, postac_slownik, form=None):
        self.race = postac_slownik['race']
        self.profession = postac_slownik['profession']
        self.name = postac_slownik['name']
        self.sex = postac_slownik['sex']
        self.level = postac_slownik['level']
        self.talents = postac_slownik['talents']
        self.skills = postac_slownik['skills']
        self.form = form
        self.cechy = postac_slownik['cechy']
        self.waga = postac_slownik['waga']
        self.traits_dev = postac_slownik['rozwiniecia_cech']
        self.cechy_rozwiniecia = {}
        self.cechy_rozwiniete = {}
        self.equipment = postac_slownik['equipment']
        self.klasa = postac_slownik['klasa']
        self.nazwa_profesji = postac_slownik['nazwa_profesji']
        self.talenty_lista_liczba = postac_slownik['talenty_lista_liczba']
        #print(f'Init {self.skills}')

    def add_talents(self):
        for field in self.form.fields:
            self.talents.append(field.data)


    def add_choosable_talents_randomly(self):
        for element in self.talenty_lista_liczba:
            if isinstance(element, list):
                losowy = random.choice(element)
                self.talents.append(losowy)


    def add_skills(self):
        for skill in self.form.pola_umiejek5.data:
            if skill in self.skills:
                self.skills[skill] += 5
            else:
                self.skills[skill]=5
        for skill in self.form.pola_umiejek3.data:
            if skill in self.skills:
                self.skills[skill] += 3
            else:
                self.skills[skill]=3

    def add_skills_randomly(self):
        if self.race == "Wysoki elf":
            from rasy.wysoki_elf import umiejki
        if self.race == "Leśny elf":
            from rasy.lesny_elf import umiejki
        if self.race == "Krasnolud":
            from rasy.khazad import umiejki
        if self.race == "Niziołek":
            from rasy.hobbit import umiejki
        if self.race == "Człowiek":
            from rasy.czlowiek import umiejki


        #umiejki 5
        a=3
        while a >= 0:
            skill = random.choice(umiejki)
            umiejki.remove(skill)

            if skill in self.skills:
                self.skills[skill] += 5
            else:
                self.skills[skill]=5
            a -= 1

        #umiejki 3
        while a >= 0:
            rand = random.randint(0, len(umiejki))
            skill = umiejki.pop(rand)
            if skill in self.skill:
                self.skills[skill] += 5
            else:
                self.skills[skill]=5
            a -= 1



    def random_traits(self):
        rzuty = []
        a = 10
        while a > 0:
            b = random.randint(1, 10) + random.randint(1, 10)
            rzuty.append(b)
            a = a - 1


        rzuty.sort()
        rzuty.reverse()



        for cecha in self.waga:
            rzut = rzuty.pop(0)
            self.cechy[cecha] += rzut

        #print(f'Random traits: {self.cechy}')



    def wrote_traits(self):
        for cecha in self.form.cechy:
            atrybut = cecha.label.text
            rzut = cecha.data
            self.cechy[atrybut] += rzut
            #print(f'wrote traits: {self.cechy}')

    def add_cechy(self):
        random = False

        for cecha in self.form.cechy:
            if cecha.data == None:
                random = True

        if random:
            self.random_traits()
        else:
            self.wrote_traits()


    def modify_traits_from_talents(self):
        if "Urodzony Wojownik" in self.talents:
            self.cechy["WW"] = self.cechy["WW"] + 5
        if "Charyzmatyczny" in self.talents:
            self.cechy["Ogd"] = self.cechy["Ogd"] + 5
        if "Błyskotliwość" in self.talents:
            self.cechy["Int"] = self.cechy["Int"] + 5
        if "Bardzo silny" in self.talents:
            self.cechy["S"] = self.cechy["S"] + 5
        if "Niezwykle Odporny" in self.talents:
            self.cechy["Wt"] = self.cechy["Wt"] + 5
        if "Strzelec Wyborowy" in self.talents:
            self.cechy["US"] = self.cechy["US"] + 5
        if "Szybki Refleks" in self.talents:
            self.cechy["Zw"] = self.cechy["Zw"] + 5
        if "Zimna Krew" in self.talents:
            self.cechy["SW"] = self.cechy["SW"] + 5
        if "Zręczny" in self.talents:
            self.cechy["Zr"] = self.cechy["Zr"] + 5
        if "Czujny" in self.talents:
            self.cechy["I"] = self.cechy["I"] + 5

        #print(f'talnety {self.cechy}')

    def develop_traits(self):
        for key, value in self.cechy.items():
            self.cechy_rozwiniete[key] = value

        for trait, level in self.traits_dev.items():
            level += self.level
            if level > 0:
                wart = level*5
                self.cechy_rozwiniecia[trait] = wart
                self.cechy_rozwiniete[trait] = self.cechy[trait] + wart

        #print(f'develop traits{self.cechy} rozwinięcia {self.cechy_rozwiniecia}')

    def generate_json_readable_output(self):
        postac_slownik = {}
        for attr, value in vars(self).items():
            if attr != "form":
                #print(f"{attr}: {value}")
                postac_slownik[attr] = value

        return postac_slownik


class PostacFinito:
    def __init__(self, postac_dict2):
        self.race = postac_dict2['race']
        self.profession = postac_dict2['profession']
        self.name = postac_dict2['name']
        self.sex = postac_dict2['sex']
        self.level = postac_dict2['level']
        self.talents = postac_dict2['talents']
        self.skills = postac_dict2['skills']
        self.cechy = postac_dict2['cechy']
        self.cechy_rozwiniecia = postac_dict2['cechy_rozwiniecia']
        self.cechy_rozwiniete = postac_dict2['cechy_rozwiniete']
        self.equipment = postac_dict2['equipment']
        self.nazwa_profesji = postac_dict2['nazwa_profesji']
        self.klasa = postac_dict2['klasa']
        self.wzrost = None
        self.wiek = None
        self.wlosy = None
        self.oczy = None
        self.HP=None
        self.skills_output = {}


    def get_eyes_hair_age_height(self, form):
        if form.oczy.data:
            self.oczy = form.oczy.data
        if form.wzrost.data:
            self.wzrost = form.wzrost.data
        if form.wlosy.data:
            self.wlosy = form.wlosy.data
        if form.wiek.data:
            self.wiek = form.wiek.data

    def random_eyes_hair_age_height(self):
        # Importowanie danych w zależności od rasy
        if self.race == "Wysoki elf":
            from rasy.wysoki_elf import wlosy, oczy, wzrost
        elif self.race == "Leśny elf":
            from rasy.lesny_elf import wlosy, oczy, wzrost
        elif self.race == "Krasnolud":
            from rasy.khazad import wlosy, oczy, wzrost
        elif self.race == "Niziołek":
            from rasy.hobbit import wlosy, oczy, wzrost
        elif self.race == "Człowiek":
            from rasy.czlowiek import wlosy, oczy, wzrost
        if self.oczy == None:
            oczy_rand = random.randint(1, 19)
            self.oczy = oczy[oczy_rand]
        if self.wlosy == None:
            wlosy_rand = random.randint(1, 19)
            self.wlosy = wlosy[wlosy_rand]
        if self.wzrost == None:
            a = wzrost[1]
            random_wzrost = wzrost[0]
            while a > 0:
                random_wzrost += random.randint(1, 10)
                a -= 1
            self.wzrost = random_wzrost

        if self.wiek == None:
            if self.race == 'Człowiek':
                a = random.randint(1, 10)
                self.wiek = 15 + a
            if self.race == 'Niziołek':
                a=0
                for i in range(5):
                    a += random.randint(1, 10)
                self.wiek = 15 + a
            if self.race == 'Krasnolud':
                a=0
                for i in range(10):
                    a += random.randint(1, 10)
                self.wiek = 15 + a
            if self.race == 'Leśny elf' or self.race =="Wysoki elf":
                a = 0
                for i in range(10):
                    a += random.randint(1, 10)
                self.wiek = 30 + a


    def unpack_profesji(self):
        self.nazwa_profesji = {int(k): v for k, v in self.nazwa_profesji.items()}

        self.nazwa_profesji = self.nazwa_profesji[self.level]

    def rany(self):
        if 'S' in self.cechy_rozwiniete:
            b_sily = int(self.cechy_rozwiniete['S'] / 10)
        else:
            b_sily=int(self.cechy['S']/10)
        if 'Wt' in self.cechy_rozwiniete:
            b_wt = int(self.cechy_rozwiniete['Wt'] / 10)
        else:
            b_wt=int(self.cechy['Wt']/10)
        if 'SW' in self.cechy_rozwiniete:
            b_sw = int(self.cechy_rozwiniete['SW'] / 10)
        else:
            b_sw = int(self.cechy['SW'] / 10)

        self.HP = b_sily+(2*b_wt)+b_sw
        if self.race == "Niziołek":
            self.HP = self.HP - b_sily
        if 'Twardziel' in self.talents:
            self.HP = self.HP + b_wt
    
    def modify_skill_output(self):
        for umiejetnosc, wartosc in self.skills.items():
            if "(Zw)" in umiejetnosc:
                self.skills_output[umiejetnosc] =f'{wartosc} ({wartosc + self.cechy_rozwiniete["Zw"]})'
            if "(WW)" in umiejetnosc:
                self.skills_output[umiejetnosc] = f'{wartosc} ({wartosc + self.cechy_rozwiniete["WW"]})'
            if "(Ogd)" in umiejetnosc:
                self.skills_output[umiejetnosc] = f'{wartosc} ({wartosc + self.cechy_rozwiniete["Ogd"]})'
            if "(Int)" in umiejetnosc:
                self.skills_output[umiejetnosc] = f'{wartosc} ({wartosc + self.cechy_rozwiniete["Int"]})'
            if "(S)" in umiejetnosc:
                self.skills_output[umiejetnosc] = f'{wartosc} ({wartosc + self.cechy_rozwiniete["S"]})'
            if "(Wt)" in umiejetnosc:
                self.skills_output[umiejetnosc] = f'{wartosc} ({wartosc + self.cechy_rozwiniete["Wt"]})'
            if "(US)" in umiejetnosc:
                self.skills_output[umiejetnosc] = f'{wartosc} ({wartosc + self.cechy_rozwiniete["US"]})'
            if "(SW)" in umiejetnosc:
                self.skills_output[umiejetnosc] = f'{wartosc} ({wartosc + self.cechy_rozwiniete["SW"]})'
            if "(Zr)" in umiejetnosc:
                self.skills_output[umiejetnosc] = f'{wartosc} ({wartosc + self.cechy_rozwiniete["Zr"]})'
            if "(I)" in umiejetnosc:
                self.skills_output[umiejetnosc] = f'{wartosc} ({wartosc + self.cechy_rozwiniete["I"]})'
            




    def generate_output(self):
        slownik={}
        slownik['Oczy'] = self.oczy
        slownik['Wzrost'] = self.wzrost
        slownik['Włosy'] = self.wlosy
        slownik['Wiek'] = self.wiek
        slownik['Rasa']= self.race
        slownik['Ścieżka Kariery'] = self.profession
        slownik['Imię'] = self.name
        slownik['Płeć'] = self.sex
        slownik['Talenty'] = self.talents
        slownik['Umiejętności'] = self.skills_output
        slownik['Cechy'] = self.cechy
        slownik['Cechy rozwinięcia'] = self.cechy_rozwiniecia
        slownik['Cechy aktualne'] = self.cechy_rozwiniete
        slownik['Wyposażenie'] = self.equipment
        slownik['Klasa'] = self.klasa
        slownik['Profesja'] = self.nazwa_profesji
        slownik['Żywotność'] = self.HP
        return slownik



