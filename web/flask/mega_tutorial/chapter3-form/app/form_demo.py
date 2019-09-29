from flask import render_template,Flask,flash,redirect,url_for
from forms import LoginForm


app = Flask(__name__)
app.secret_key = 'fjaofoahfo39rowjho'


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))

        # 等效于 return redirect('/index')
        return redirect(url_for('index'))
    return render_template('login.html', title = 'Sign In', form = form)


if __name__ == '__main__':
    app.run(debug=True)
