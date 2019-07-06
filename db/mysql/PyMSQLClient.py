# -*- coding:utf-8 -*-

# pip3 install PyMySQL

import pymysql

class MysqlClient:
	def __init__(self, db, host = "localhost", user = "root", passwd = "root", charset='utf8'):
		self.conn = pymysql.connect (host = host, user = user, passwd = passwd, db= db, charset=charset)

	def insert(self, sql): 
		cursor = self.conn.cursor()
		cursor.execute(sql)
		cursor.close()
		self.conn.commit()

	def query(self, sql):
		cursor = self.conn.cursor()
		cursor.execute(sql)
		result = cursor.fetchall()
		cursor.close()
		return result

	# 执行删除表，清空表操作
	def execute(self, sql):
		cursor = self.conn.cursor()
		cursor.execute(sql)
		cursor.close()
		self.conn.commit()

	def close(self):
		self.conn.close ()