import pymysql as MySQLdb


class MysqlClient:
	def __init__(self, db, host="10.1.0.20", port=3306, user="hm2", passwd="asdlk$gawHke", charset='utf8'):
		self.conn = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)

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
		self.conn.close()