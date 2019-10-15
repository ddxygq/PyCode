from flask import render_template, flash, redirect, url_for, request, current_app
from flask_login import current_user, login_required
from datetime import datetime
from flask_babel import _

import sys
sys.path.append('../..')
from app.models import User, Post
from app import db
from app.main import bp
from app.main.forms import EditProfileForm, PostForm


@bp.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))

    if user == current_user:
        flash("you can't follow yourself.")
        return redirect(url_for('main.user_home', username=username))

    current_user.follow(user)
    db.session.commit()
    flash('you are following {}.'.format(username))
    return redirect(url_for('main.user_home', username=username))


@bp.route('/unfollow/<username>')
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
        return redirect(url_for('main.user_home', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('you are not following {}.'.format(username))
    return redirect(url_for('main.user_home', username=username))


@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('main.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile', form=form)


@bp.route('/user/<username>')
@login_required
def user_home(username):
    user = User.query.filter_by(username=username).first_or_404()
    # posts_ = Post.query.filter_by(user_id=user.id)
    # posts = [{'author': user, 'body': post.body} for post in posts_]
    page = request.args.get('page', 1, type=int)
    posts = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.user_home', username=user.username, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.user_home', username=user.username, page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('user.html'
                           , current_user=current_user
                           , user=user
                           , posts=posts.items
                           , next_url=next_url
                           , prev_url=prev_url)


@bp.route('/explore')
@login_required
def explore():
    flash(_('Your post is now live!'))
    page = request.args.get('page', 1, type=int)
    posts = current_user.followed_posts().paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.index', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.index', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('index.html', posts=posts.items, next_url=next_url,
                           prev_url=prev_url)


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    if current_user.is_anonymous:
        return redirect(url_for('auth.login'))
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('main.index'))
    # posts = current_user.followed_posts().all()

    # 分页
    page = request.args.get('page', 1, type=int)
    posts = current_user.followed_posts().paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.index', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.index', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('index.html'
                           , current_user=current_user
                           , posts=posts.items
                           , form=form
                           , next_url=next_url
                           , prev_url=prev_url
                           )


@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        """
        最后一步是提交数据库会话，以便将上面所做的更改写入数据库。如果你想知道为什么在提交之前没有db.session.add()，
        考虑在引用current_user时，Flask-Login将调用用户加载函数，该函数将运行一个数据库查询并将目标用户添加到数据库会话中。
        所以你可以在这个函数中再次添加用户，但是这不是必须的，因为它已经在那里了。
        """
        db.session.commit()