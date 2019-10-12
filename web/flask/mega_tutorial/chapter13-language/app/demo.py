from flask import render_template, Flask, flash, redirect, url_for, request, g
from forms import LoginForm, RegistrationForm, EditProfileForm, PostForm, ResetPasswordRequestForm, ResetPasswordForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from datetime import datetime
from flask_babel import _

import sys

sys.path.append('../')
from app.models import User, Post
from app import app, db
from app.emails import send_password_reset_email


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.before_request:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)


@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('login'))
    return render_template('reset_password_request.html',
                           title='Reset Password', form=form)


@app.route('/explore')
@login_required
def explore():
    flash(_('Your post is now live!'))
    page = request.args.get('page', 1, type=int)
    posts = current_user.followed_posts().paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('index', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('index', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('index.html', posts=posts.items, next_url=next_url,
                           prev_url=prev_url)


@app.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))

    if user == current_user:
        flash("you can't follow yourself.")
        return redirect(url_for('user_home', username=username))

    current_user.follow(user)
    db.session.commit()
    flash('you are following {}.'.format(username))
    return redirect(url_for('user_home', username=username))


@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    """
    取消follow
    :param username:
    :return:
    """
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash("you can't unfollow yourself.")
        return redirect(url_for('user_home', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('you are not following {}.'.format(username))
    return redirect(url_for('user_home', username=username))


def get_post():
    # return Post.query.filter_by(user_id=current_user.id)
    return Post.query.order_by(Post.timestamp.desc()).all()


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('index'))
    # posts = current_user.followed_posts().all()

    # 分页
    page = request.args.get('page', 1, type=int)
    posts = current_user.followed_posts().paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('index', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('index', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('index.html'
                           , current_user=current_user
                           , posts=posts.items
                           , form=form
                           , next_url=next_url
                           , prev_url=prev_url
                           )


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
    # posts_ = Post.query.filter_by(user_id=user.id)
    # posts = [{'author': user, 'body': post.body} for post in posts_]
    page = request.args.get('page', 1, type=int)
    posts = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('user_home', username=user.username, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('user_home', username=user.username, page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('user.html'
                           , current_user=current_user
                           , user=user
                           , posts=posts.items
                           , next_url=next_url
                           , prev_url=prev_url)


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
