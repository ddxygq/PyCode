import sys

sys.path.append('../')
from app.models import User, Post
from app import app, db


def run():
    db.create_all()
    user = User(username='cj318.cn', email='hbzegkg@126.com')
    user.set_password('123456')
    db.session.add(user)
    db.session.commit()

    users = User.query.all()
    for u in users:
        print(u.id, u.username)

    u = User.query.get(1)
    # post有一个动态属性，post.author，将返回发出动态的user
    for i in range(5):
        body = '%s post %s' % (u.username, str(i))
        print(body)
        p = Post(body=body, author=u)
        db.session.add(p)
        db.session.commit()

    posts = Post.query.all()
    for post in posts:
        print(post.id, post.body, post.timestamp, post.user_id, post.author)


if __name__ == '__main__':
    run()
