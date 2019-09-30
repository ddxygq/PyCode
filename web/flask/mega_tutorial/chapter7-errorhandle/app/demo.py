from flask import render_template, Flask, flash, redirect, url_for, request
from forms import LoginForm, RegistrationForm, EditProfileForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from datetime import datetime

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


@app.route('/user/<username>')
@login_required
def user_home(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts_ = Post.query.filter_by(user_id=user.id)
    posts = [{'author': user, 'body': post.body} for post in posts_]

    return render_template('user.html', current_user=current_user, user=user, posts=posts)


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        """
        最后一步是提交数据库会话，以便将上面所做的更改写入数据库。如果你想知道为什么在提交之前没有db.session.add()，
        考虑在引用current_user时，Flask-Login将调用用户加载函数，该函数将运行一个数据库查询并将目标用户添加到数据库会话中。
        所以你可以在这个函数中再次添加用户，但是这不是必须的，因为它已经在那里了。
        """
        db.session.commit()


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile', form=form)


@app.errorhandler(404)
def not_found_error(error):
    app.logger.error('404 error')
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(eror):
    print('handle 500')
    db.session.rollback()
    return render_template('500.html'), 500


if __name__ == '__main__':
    # init_db()
    app.run(debug=True)