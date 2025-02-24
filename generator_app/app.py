from flask import Flask, render_template, url_for, redirect, request, session, send_file
from strona.forms import (CreationFormOne, CreationFormDvarf, CreationFormMan, CreationFormHighElf,
                          CreationFormWoodElf, CreationFormHalfing, AppearanceForm, )
from generator import Postac, PostacTalentyIUmiejki, PostacFinito, FileCreation


app = Flask(__name__)

app.config['SECRET_KEY'] ='dugsnaga'
app.config["SESSION_PERMANENT"] = False

@app.route('/one', methods=['GET', 'POST'])
def formularz():
    #print(globals())
    #czyszczenie zmiennych
    #print(globals()['session'])

    form = CreationFormOne()
    if form.validate_on_submit():
        postac = Postac(form)


        postac.generate_race_name_profession()
        postac.give_experience()
        postac.draw_talents()
        postac.get_profession_traits_and_add_to_character()
        postac.unpack_profession_talents()
        postac.unpack_profession_skills()
        postac.unpack_equipment()
        postac.create_gold_str_and_append_to_character_equipment()


        postac_dict = postac.generate_json_readable_output()


        if form.dalej.data:
            session['postac_dict'] = postac_dict
            return redirect(url_for('two'))
        if form.losuj_reszte.data:
            #print(postac_dict)
            postac2=PostacTalentyIUmiejki(postac_dict)
            postac2.add_choosable_talents_randomly()
            postac2.add_skills_randomly()
            postac2.random_traits()
            postac2.modify_traits_from_talents()
            postac2.develop_traits()
            postac_dict2=postac2.generate_json_readable_output()
            postac3 = PostacFinito(postac_dict2)
            postac3.random_eyes_hair_age_height()
            postac3.unpack_profesji()
            postac3.rany()
            postac3.modify_skill_output()
            postac_dict3 = postac3.generate_output()
            session['postac_dict3'] = postac_dict3
            return redirect(url_for('wyniki'))

    return render_template('form_one.html', form=form)

@app.route('/two', methods=['GET', 'POST'])
def two():
    postac_dict = session.get('postac_dict')
    #wybór formularza
    if postac_dict['race'] == 'Krasnolud':
        form = CreationFormDvarf()
    if postac_dict['race'] == 'Człowiek':
        form = CreationFormMan()
    if postac_dict['race'] == 'Wysoki elf':
        form=CreationFormHighElf()
    if postac_dict['race'] == 'Leśny elf':
        form = CreationFormWoodElf()
    if postac_dict['race'] == 'Niziołek':
        form= CreationFormHalfing()

    postac = PostacTalentyIUmiejki(postac_dict, form)

    ## po kliknięciu
    if form.validate_on_submit():
        # Sprawdzamy, czy wybrane umiejętności w obu polach są te same
        selected_5 = set(form.pola_umiejek5.data)  # Zbieramy dane z pola pola_umiejek5
        selected_3 = set(form.pola_umiejek3.data)  # Zbieramy dane z pola pola_umiejek3

        # Sprawdzamy, czy nie ma wspólnych umiejętności
        if not selected_5.isdisjoint(selected_3):
            form.pola_umiejek5.errors.append('Nie możesz wybrać tych samych umiejętności w obu polach!')
            form.pola_umiejek3.errors.append('Nie możesz wybrać tych samych umiejętności w obu polach!')
            return render_template('form_two.html', postac_dict=postac_dict, form=form)

        ## wywołujemy funkcje generatora
        postac.add_talents()
        postac.add_skills()
        postac.add_cechy()
        postac.modify_traits_from_talents()
        postac.develop_traits()
        postac_dict2 = postac.generate_json_readable_output()
        print(postac_dict2)

        if form.dalej.data:
            #przekazujemy wpisane wartości do strony trzeciej TBC
            session['postac_dict2'] = postac_dict2
            return redirect(url_for('three'))
        if form.losuj_reszte.data:
            # przekazujemy wpisane wartości do strony wyników TBC
            postac3 = PostacFinito(postac_dict2)
            postac3.random_eyes_hair_age_height()
            postac3.unpack_profesji()
            postac3.modify_skill_output()
            postac_dict3 = postac3.generate_output()
            session['postac_dict3'] = postac_dict3

            return redirect(url_for('wyniki'))

    return render_template('form_two.html',
                           postac_dict=postac_dict, form=form)


@app.route('/three', methods=['GET', 'POST'])
def three():
    postac_dict2 = session.get('postac_dict2')
    form = AppearanceForm(postac_dict2)
    postac = PostacFinito(postac_dict2)

    if form.validate_on_submit():
        postac.get_eyes_hair_age_height(form)
        postac.random_eyes_hair_age_height()
        postac.unpack_profesji()
        postac.rany()

        postac.modify_skill_output()

        output = postac.generate_output()

        session['postac_dict3'] = output

        return redirect(url_for('wyniki'))

    return render_template('form_three.html', form=form)

@app.route('/result', methods=['GET'])
def wyniki():
    postac_dict3 = session.get('postac_dict3')
    #print(postac_dict3)


    return render_template('result.html', postac=postac_dict3)


@app.route('/download', methods=['GET'])
def download_file():
    postac_dict = session.get('postac_dict3')  # Pobieramy słownik z sesji
    if not postac_dict:
        return "Brak danych do pobrania", 404
    # Nazwa pliku do pobrania
    plik = FileCreation(postac_dict)
    plik.format_output()
    plik.output_to_file()
    file_path = plik.nazwa_pliku

    # Wysyłamy plik do pobrania
    return send_file(file_path, as_attachment=True)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


