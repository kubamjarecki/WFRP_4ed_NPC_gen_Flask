from flask import Flask, render_template, url_for, redirect, request
from strona.forms import CreationForm
from generator import Postac

app = Flask(__name__)
app.config['SECRET_KEY'] ='dugsnaga'

@app.route('/', methods=['GET', 'POST'])
def formularz():
    form = CreationForm()
    if form.validate_on_submit():
        postac = Postac(form)
        postac_ = postac.generate_postac()
        print(postac_)
        return redirect(url_for('wyniki', postac_=postac_))

    return render_template('form.html', form=form)

@app.route('/result', methods=['GET'])
def wyniki():
    postac_ = request.args.get('postac_')
    return render_template('result.html', postac_=postac_)


if __name__ == '__main__':
    app.run(debug=True)


