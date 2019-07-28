# -*- coding:utf-8 -*-

import sys
import datetime
import commands
import MySQLdb

sys.path.append('/var/lib/hadoop-hdfs/scripts/python_module2')
import keguang.commons as commons
import keguang.timedef as timedef
import keguang.sql.hiveclient as hive
import keguang.sql.mysqlclient as mysql

def run(days, regx):
	resultTb = 'active_week_install_helper'
	# days = timedef.getDays(starttime,endtime,regx)
	for day in days:
		print '============================%s 今天又是美好的一天========================='%(day)
		print '=========================佛祖保佑， 永无bug，南无阿弥陀佛！==========================='
		hclient = hive.HiveClient()
		# day 2019-05-20
		dayAgo14 =timedef.getExacDay(regx, day, -14) # 2019-05-06
		dayAgo7 = timedef.getExacDay(regx, day, -7) # 2019-05-13
		dayAgo8 = timedef.getExacDay(regx, day, -8) # 2019-05-13
		dayAgo1 = timedef.getExacDay(regx, day, -1) # 2019-05-19

		# 历史总安装设备数 `weekHelperOld`
		sql = '''
		select count(1) from hm2.history_helper where starttime < '%s'
		'''%(dayAgo7)
		print sql
		weekHelperOld = int(hclient.query(sql)[0][0])

		# 当周安装helper设备数
		sql = '''
		select count(1) from (select helper.guid g, history_helper.guid g2 from (select guid from hm2.helper where dt between '%s' and '%s' group by guid) helper left join (select guid from hm2.history_helper where starttime < '%s') history_helper on helper.guid = history_helper.guid) m where m.g2 is null
		'''%(dayAgo7, dayAgo1, dayAgo7)
		print sql
		weekHelperNew = int(hclient.query(sql)[0][0])

		# 本周helper活跃设备数
		sql = '''
		select count(1) from (select guid from hm2.helper where dt between '%s' and '%s' group by guid)m
		'''%(dayAgo7, dayAgo1)
		print sql
		weekHelper = int(hclient.query(sql)[0][0])

		# 上周helper活跃设备数
		sql = '''
		select count(1) from (select guid from hm2.helper where dt between '%s' and '%s' group by guid)m
		'''%(dayAgo14, dayAgo8)
		print sql
		weekLastHelper = int(hclient.query(sql)[0][0])

		# 本周回流老用户
		sql = '''
		select count(1) from (select c.guid from (select guid from hm2.helper where dt >= '%s' and dt <= '%s'  group by guid) c left join (select guid from hm2.history_helper where starttime < '%s') d on c.guid = d.guid where d.guid is not null ) e left join  (select a.guid from (select guid from hm2.helper where dt >= '%s' and dt <= '%s'  group by guid) a left join (select guid from hm2.history_helper where starttime < '%s') b on a.guid = b.guid where b.guid is not null ) f on e.guid = f.guid where f.guid is null
		'''%(dayAgo7, dayAgo1, dayAgo14, dayAgo14, dayAgo8, dayAgo14)
		print sql
		backWeekHelper = int(hclient.query(sql)[0][0])

		# 上周老用户本周流失
		sql = '''
		select count(1) from (select c.guid from (select guid from hm2.helper where dt >= '%s' and dt <= '%s'  group by guid) c left join (select guid from hm2.history_helper where starttime < '%s') d on c.guid = d.guid where d.guid is not null ) e left join  (select a.guid from (select guid from hm2.helper where dt >= '%s' and dt <= '%s'  group by guid) a left join (select guid from hm2.history_helper where starttime < '%s') b on a.guid = b.guid where b.guid is not null ) f on e.guid = f.guid where f.guid is null
		'''%(dayAgo14, dayAgo8, dayAgo14, dayAgo7, dayAgo1, dayAgo14)
		print sql
		offWeekHelper = int(hclient.query(sql)[0][0])

		# 上周新用户本周流失
		sql = '''
		select count(1) from (select history_helper.guid as g,helper.guid as g2 from (select guid from hm2.history_helper where starttime between '%s' and '%s')history_helper left join (select guid from hm2.helper where dt between '%s' and '%s' group by guid) helper on history_helper.guid = helper.guid)m where m.g2 is null
		'''%(dayAgo14, dayAgo8, dayAgo7, dayAgo1)
		print sql
		offNewHelper = int(hclient.query(sql)[0][0])

		weekcircRatio = (weekHelperNew + backWeekHelper - offWeekHelper) / float(weekLastHelper) * 100

		# 结果保存到数据库
		mclient = getConn()
		sql = '''
		insert into %s(weekTime,weekHelperOld,weekHelperNew,weekHelper,weekLastHelper,backWeekHelper,offWeekHelper,offNewHelper,weekcircRatio) values('%s', %d, %d, %d, %d, %d, %d, %d, %f)
		'''%(resultTb, day, weekHelperOld,weekHelperNew,weekHelper,weekLastHelper,backWeekHelper,offWeekHelper,offNewHelper, weekcircRatio)
		print sql

		mclient.insert(sql)
		mclient.close()

# 返回mysql 连接
def getConn():
	return mysql.MysqlClient(host = '10.1.254.89', user = 'statistic', passwd = 'P55VsPPBs2', db= 'statistic')

if __name__ == '__main__':
	regx = '%Y-%m-%d'
	yesday = timedef.getYes(regx, -1)
	# starttime = '2019-05-25'
	# endtime = '2019-06-20'
	days = [timedef.getYes(regx, 0)]
	run(days, regx)
