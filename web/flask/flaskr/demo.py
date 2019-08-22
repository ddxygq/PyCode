import sqlite3
DATABASE = 'D:/我的文件/Codes/PyCode/web/flask/flaskr/entries.db'
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()
sql = '''
    delete from entries
    '''
result = cursor.execute(sql).rowcount
print(result)

cursor.close()
conn.close()