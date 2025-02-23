from flask import Flask, render_template
from form import NameForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

@app.route('/form', methods=['GET','POST'])
def form():
    form = NameForm()
    if form.validate_on_submit():
        return f"Hello,{form.name.data}!"
    return render_template('form.html', form=form)

@app.errorhandler(404)
def not_found(error):
    return "Internal Server Error", 500

if __name__== 'main_':
    app.run(debug=True)