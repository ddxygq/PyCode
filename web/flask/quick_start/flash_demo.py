from flask import Flask, flash, redirect, render_template, \
     request, url_for


app = Flask(__name__)
app.secret_key = 'jlajf*JLFa/.JLafj'


"""
http://docs.jinkan.org/docs/flask/patterns/flashing.html#message-flashing-pattern
"""


@app.route('/')
def index():
    return render_template('flash_demo/index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('flash_demo/login.html', error=error)

if __name__ == "__main__":
    app.run(debug=True)