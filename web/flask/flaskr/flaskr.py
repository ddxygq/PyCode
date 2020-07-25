import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__, instance_path=os.path.abspath(__file__))
app.config['USERNAME'] = 'name'
app.config['PASSWORD'] = 'password'
app.secret_key = 'ajflafoo8qm.mgaj'

# DATABASE = 'D:/我的文件/Codes/PyCode/web/flask/flaskr/entries.db'
DATABASE = os.path.join(os.getcwd(), 'entries.db')


def init_table():
    """first run create table"""
    db = get_db()
    result = db.cursor().execute(
        "SELECT count(*) FROM sqlite_master WHERE type = 'table' AND name = 'entries'").fetchall()
    table_exists = result[0][0] == 1

    # 不存在，则创建表
    if not table_exists:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
    else:
        print('entries already exists .')

    db.close()


def get_db():
    """connect to special database"""
    return sqlite3.connect(DATABASE)


"""
@app.before_request
def get_connection():
    db = getattr(g, 'db', None)
    if db is None:
        db = g.db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
"""


@app.before_request
def before_request():
    g.db = get_db()


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()


@app.route('/')
def show_entries():
    """显示条目"""
    sql = 'select title, text from entries order by id desc'
    cursor = g.db.cursor()
    entries = [dict(title = row[0], text = row[1]) for row in cursor.execute(sql).fetchall()]
    cursor.close()
    return render_template('show_entries.html', entries = entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    sql = 'insert into entries(title, text) values(?, ?)'
    g.db.execute(sql, [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """登陆函数"""
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error = error)


@app.route('/logout')
def logout():
    """注销函数"""
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    # 第一次执行，需要初始化数据库，和表
    init_table()

    app.run(debug=True)