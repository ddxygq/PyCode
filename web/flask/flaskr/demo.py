import sqlite3
DATABASE = 'D:/我的文件/Codes/PyCode/web/flask/flaskr/entries.db'
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()
sql = '''
    select * from entries
    '''
result = cursor.execute(sql).fetchall()
for i in result:
    print(i)