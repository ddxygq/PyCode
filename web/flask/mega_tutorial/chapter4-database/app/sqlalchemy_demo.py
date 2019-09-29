import sys

sys.path.append("../")
from app import db
from app.models import User, Post


if __name__ == '__main__':
    db.create_all()
    user = User(username = 'ikeguang.com', email = 'ikeguang@126.com', password_hash = '123456')
    user2 = User(username='cj318.cn', email='hbzegkg@126.com')
    db.session.add(user)
    db.session.add(user2)
    db.session.commit()
    users = User.query.all()
    for u in users:
        print(u.id, u.username)

    u = User.query.get(1)
    p = Post(body='my first post!', author=u)
    db.session.add(p)
    db.session.commit()
