from orator import DatabaseManager
from orator import Model

config = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'test',
        'user': 'root',
        'password': 'root',
        'prefix': ''
    }
}

config3 = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'ry',
        'user': 'root',
        'password': 'root',
        'prefix': ''
    }
}


class User(Model):
    __table__ = 'test'


db = DatabaseManager(config)
User.set_connection_resolver(db)


class User3(Model):
    __table__ = 'test3'
    __timestamps__ = False

    __primary_key__ = 'id'
    __guarded__ = []

db3 = DatabaseManager(config3)
User3.set_connection_resolver(db3)


# user = User.find(1)
#
# data = user.get_attributes()
#
#
# User3.update_or_create({'id':data.get('id')},data)

users = db.table('test').get()
for user in users:
    print(user.get('id'))
    User3.update_or_create({'id': user.get('id')}, user)
