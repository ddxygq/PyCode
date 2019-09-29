from flask import render_template, Flask, flash, redirect, url_for, request
from forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

import sys

sys.path.append('../')
from app.models import User, Post
from app import app, db


def get_post():
    return Post.query.filter_by(user_id = current_user.id)


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    return render_template('login.html', current_user=current_user, posts = get_post())


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/vip')
@login_required
def vip():
    # login_manager.login_message = '无权登录'，闪现消息可以配置
    return 'vip page'


@app.route('/register', methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


def init_db():
    db.create_all()
    user = User.query.get(1)
    db.session.delete(user)
    db.session.commit()
    user = User(username='ikeguang.com', email='ikeguang@126.com')
    user.set_password('123456')
    db.session.add(user)
    db.session.commit()
    users = User.query.all()
    for u in users:
        print(u.id, u.username, u.password_hash)


if __name__ == '__main__':
    # init_db()
    app.run(debug=True)
