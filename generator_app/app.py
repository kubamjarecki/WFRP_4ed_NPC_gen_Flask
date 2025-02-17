from flask import Flask, render_template, url_for, redirect, request, session
from strona.forms import CreationFormOne, CreationFormTwo
from generator import Postac, PostacTalentyIUmiejki

app = Flask(__name__)
app.config['SECRET_KEY'] ='dugsnaga'

@app.route('/one', methods=['GET', 'POST'])
def formularz():
    form = CreationFormOne()

    if form.validate_on_submit():
        postac = Postac(form)
        postac_dict = postac.generate_postac()

        if form.dalej.data:
            session['postac_dict'] = postac_dict
            return redirect(url_for('two'))
        if form.losuj_reszte.data:
            print(postac_dict)
            session['postac_dict'] = postac_dict
            return redirect(url_for('wyniki'))

    return render_template('form_one.html', form=form)

@app.route('/two', methods=['GET', 'POST'])
def two():
    postac_dict = session.get('postac_dict')
    postac = PostacTalentyIUmiejki(postac_dict)
    form = CreationFormTwo()
    if form.validate_on_submit():
        if form.dalej.data:
            if form.losuj.data:
                #logika losowania TBC
                return redirect(url_for('three'))
            else:
                #przekazujemy wpisane wartości do strony trzeciej TBC
                return redirect(url_for('three'))
        if form.losuj_reszte.data:
            if form.losuj.data:
                #logika losowania reszty TBC
                return redirect(url_for('wyniki'))
            else:
                # przekazujemy wpisane wartości do strony wyników TBC
                return redirect(url_for('wyniki'))

    return render_template('form_two.html',
                           postac_dict=postac_dict, form=form)

@app.route('/result', methods=['GET'])
def wyniki():
    postac_dict = session.get('postac_dict')
    imie = postac_dict['imie']
    rasa = postac_dict['rasa']


    return render_template('result.html', postac_dict=postac_dict)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


