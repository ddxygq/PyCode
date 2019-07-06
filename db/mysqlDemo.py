# -*- coding:utf-8 -*-

import sys

# ('bb', 'bb123456', 'bb@126.com')

def demo():
	import mysql.MySQLdbClient as mysqldb
	conn = mysqldb.MysqlClient(host = 'localhost', user = 'root', passwd = 'root', db= 'test')
	# 查询
	print('===============查询结果=============')
	sql = 'select user_name,pass_word,email from user'
	users = conn.query(sql)
	print(users)
	
	# 删除
	sql = 'delete from user where user_name ="bb"'
	conn.execute(sql)

	# 查询删除后
	print('================删除后结果============')
	sql = 'select user_name,pass_word,email from user'
	users = conn.query(sql)
	print(users)

	# 插入
	sql = '''
	insert into user(user_name, pass_word, email, nick_name, reg_time) values('bb', 'bb123456', 'bb@126.com', 'bb2', '2019年6月24日 下午11时26分57秒')
	'''
	conn.insert(sql)

	# 查询插入后
	print('==============插入后结果==============')
	sql = 'select user_name,pass_word,email from user'
	users = conn.query(sql)
	print(users)



def demo2():
	import mysql.mysqlclint as mysqlclint
	conn = mysqlclint.MysqlClient(host = 'localhost', user = 'root', passwd = 'root', db= 'test')
	# 查询
	print('===============查询结果=============')
	sql = 'select user_name,pass_word,email from user'
	users = conn.query(sql)
	print(users)
	
	# 删除
	sql = 'delete from user where user_name ="bb"'
	conn.execute(sql)

	# 查询删除后
	print('================删除后结果============')
	sql = 'select user_name,pass_word,email from user'
	users = conn.query(sql)
	print(users)

	# 插入
	sql = '''
	insert into user(user_name, pass_word, email, nick_name, reg_time) values('bb', 'bb123456', 'bb@126.com', 'bb2', '2019年6月24日 下午11时26分57秒')
	'''
	conn.insert(sql)

	# 查询插入后
	print('==============插入后结果==============')
	sql = 'select user_name,pass_word,email from user'
	users = conn.query(sql)
	print(users)

def demo3():
	import mysql.PyMSQLClient as pymysql
	conn = pymysql.MysqlClient(host = 'localhost', user = 'root', passwd = 'root', db= 'test')
	# 查询
	print('===============查询结果=============')
	sql = 'select user_name,pass_word,email from user'
	users = conn.query(sql)
	print(users)
	
	# 删除
	sql = 'delete from user where user_name ="bb"'
	conn.execute(sql)

	# 查询删除后
	print('================删除后结果============')
	sql = 'select user_name,pass_word,email from user'
	users = conn.query(sql)
	print(users)

	# 插入
	sql = '''
	insert into user(user_name, pass_word, email, nick_name, reg_time) values('bb', 'bb123456', 'bb@126.com', 'bb2', '2019年6月24日 下午11时26分57秒')
	'''
	conn.insert(sql)

	# 查询插入后
	print('==============插入后结果==============')
	sql = 'select user_name,pass_word,email from user'
	users = conn.query(sql)
	print(users)

if __name__ == '__main__':
	print('**********   demo() => ')
	demo()
	print('**********   demo2() => ')
	demo2()
	print('**********   demo3() => ')
	demo3()