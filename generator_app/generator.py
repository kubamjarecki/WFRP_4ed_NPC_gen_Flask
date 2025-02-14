import random

class Postac:
    def __init__(self, form):
        self.form = form
        self.rasa = form.race.data

    def generate_postac(self):

        if self.rasa == "Losowo":
            K100 = random.randint(1, 100)
            lesny = [100]
            wysoki = [99]
            kras = [98, 97, 96, 95]
            hobbit = [94, 93, 92, 91]
            if K100 in wysoki:
                race = "Wysoki elf"
            if K100 in lesny:
                self.rasa = "Leśny elf"
            if K100 in kras:
                self.rasa = "Krasnolud"
            if K100 in hobbit:
                self.rasa = "Niziołek"
            if K100 < 91:
                self.rasa = "Człowiek"

        return f"Twoja rasa to {self.rasa}"
