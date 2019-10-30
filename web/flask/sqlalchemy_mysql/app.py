from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/test?charset=utf8'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    accountNumber = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(20), unique=True)

    __tablename__ = 'sqlalchemy_mysql_test'

    def __init__(self, account_number=None, password=None, name="admin"):
        self.accountNumber = account_number
        self.password = password
        self.name = name

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % self.name


if __name__ == '__main__':
    db.create_all()
    test_user = User('3', 'root3', 'keguang3')
    db.session.add(test_user)
    db.session.commit()
    print(db.session.query(User).all())
