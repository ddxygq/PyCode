import sqlite3

def run():
    DATABASE = 'D:/我的文件/Codes/PyCode/Python基础语法/数据库/test.db'
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    """
    sql = '''
    create table user (
    id integer primary key autoincrement,
    name string not null,
    age integer not null
    )
    '''
    """
    sql = '''
    insert into user(name, age) values('柯广的博客', 2)
    '''
    cursor.execute(sql)
    conn.commit()

    sql = '''
    select count(1) from user
    '''
    result = cursor.execute(sql).fetchall()
    print(result)
    cursor.close()
    conn.close()



if __name__ == '__main__':
    run()