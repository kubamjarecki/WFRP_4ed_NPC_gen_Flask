from flask import Flask, render_template, url_for, redirect, request, session
from strona.forms import (CreationFormOne, CreationFormDvarf, CreationFormMan, CreationFormHighElf,
                          CreationFormWoodElf, CreationFormHalfing, AppearanceForm)
from generator import Postac, PostacTalentyIUmiejki

app = Flask(__name__)
app.config['SECRET_KEY'] ='dugsnaga'

@app.route('/one', methods=['GET', 'POST'])
def formularz():
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
            session['postac_dict'] = postac_dict
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

        if form.dalej.data:
            #przekazujemy wpisane wartości do strony trzeciej TBC
            session['postac_dict2'] = postac_dict2
            return redirect(url_for('three'))
        if form.losuj_reszte.data:
            # przekazujemy wpisane wartości do strony wyników TBC
            session['postac_dict2'] = postac_dict2
            return redirect(url_for('wyniki'))

    return render_template('form_two.html',
                           postac_dict=postac_dict, form=form)


@app.route('/three', methods=['GET', 'POST'])
def three():
    postac_dict2 = session.get('postac_dict2')
    form = AppearanceForm(postac_dict2)

    return render_template('form_three.html', form=form)

@app.route('/result', methods=['GET'])
def wyniki():


    return render_template('result.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


