-- 创建数据库
create database wx_test;

-- 显示数据库
show databases;

-- 指定操作的数据库
use wx_test; 

-- 显示表
show tables; 

-- 建表命令
create table if not exists user(
id bigint(10) not null auto_increment primary key,
user_name varchar(50) not null default 'null',
age int not null default 0
)engine=Innodb charset=utf8mb4;

-- 显示建表语句
show create table user; 
/*
+-------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                                                                                                                            |
+-------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| user  | CREATE TABLE `user` (
  `id` bigint(10) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) NOT NULL DEFAULT 'null',
  `age` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 |
+-------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
*/

-- 查看表的字段信息
desc user; 
/*
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| id        | bigint(10)  | NO   | PRI | NULL    | auto_increment |
| user_name | varchar(50) | NO   |     | null    |                |
| age       | int(11)     | NO   |     | 0       |                |
+-----------+-------------+------+-----+---------+----------------+
*/

-- =====注释=============
-- 我是单行注释，
/*
我是多行注释
*/

-- 插入数据
insert into user(user_name, age) values
('ikeguang.com', 23),
('cj318.cn', 24),
('数据分析挖掘与算法', 36);

-- 查询数据
select * from user;
/*
+----+--------------------+-----+
| id | user_name          | age |
+----+--------------------+-----+
|  1 | ikeguang.com       |  23 |
|  2 | cj318.cn           |  24 |
|  3 | 数据分析挖掘与算法 |  36 |
+----+--------------------+-----+
3 rows in set (0.14 sec)
*/

-- 更新数据
update user set age = 25 where id = 3;

-- 删除数据
delete from user where age = 24;
select * from user;
/*
+----+--------------------+-----+
| id | user_name          | age |
+----+--------------------+-----+
|  1 | ikeguang.com       |  23 |
|  3 | 数据分析挖掘与算法 |  25 |
+----+--------------------+-----+
2 rows in set (0.00 sec)
*/

-- 将一个文本文件导入mysql表中
load data local infile 'D:/我的文件/公众号文章材料/数据分析挖掘与算法/mysql知识/user.txt' into table user fields terminated by '\t';

/*
Query OK, 1 row affected (0.07 sec)
Records: 1  Deleted: 0  Skipped: 0  Warnings: 0
*/

-- select * from user;
/*
+----+--------------------+-----+
| id | user_name          | age |
+----+--------------------+-----+
|  1 | ikeguang.com       |  23 |
|  3 | 数据分析挖掘与算法 |  25 |
|  4 | 学习使我快乐       |  18 |
+----+--------------------+-----+
*/

-- 显示当前用户和正在操作的数据库
 select database();
 /*
 +------------+
| database() |
+------------+
| wx_test    |
+------------+
 */
select user();
/*
+----------------+
| user()         |
+----------------+
| root@localhost |
+----------------+
*/

-- 匹配，user_name 含有ke这个子串
select * from user where user_name like '%ke%';
/*
+----+--------------+-----+
| id | user_name    | age |
+----+--------------+-----+
|  1 | ikeguang.com |  23 |
+----+--------------+-----+
*/

-- 正则匹配 user_name 以k开头，k出现0次或者多次
select * from user where user_name rlike '^k*';
/*
+----+--------------------+-----+
| id | user_name          | age |
+----+--------------------+-----+
|  1 | ikeguang.com       |  23 |
|  3 | 数据分析挖掘与算法 |  25 |
|  4 | 学习使我快乐       |  18 |
+----+--------------------+-----+
3 rows in set (0.00 sec)
*/

-- 正则匹配 user_name 以k开头，k出现一次以上
select * from user where user_name rlike '^k+';
-- Empty set (0.00 sec)

-- 正则匹配 user_name 以i开头，k出现一次及以上
select * from user where user_name rlike '^ik+';
/*
+----+--------------+-----+
| id | user_name    | age |
+----+--------------+-----+
|  1 | ikeguang.com |  23 |
+----+--------------+-----+
1 row in set (0.00 sec)
*/

/*
常用mysql状态命令
*/

-- 显示最大连接数
show global status like 'Max_used_connections';
+----------------------+-------+
| Variable_name        | Value |
+----------------------+-------+
| Max_used_connections | 2     |
+----------------------+-------+

-- 查看进程的连接
show full processlist;
/*
+----+------+-----------------+---------+---------+------+----------+-----------------------+
| Id | User | Host            | db      | Command | Time | State    | Info                  |
+----+------+-----------------+---------+---------+------+----------+-----------------------+
|  8 | root | localhost:49608 | wx_test | Query   |    0 | starting | show full processlist |
+----+------+-----------------+---------+---------+------+----------+-----------------------+
*/

-- SQL执行计划
explain select * from user;
/*
+----+-------------+-------+------------+------+---------------+------+---------+------+------+----------+-------+
| id | select_type | table | partitions | type | possible_keys | key  | key_len | ref  | rows | filtered | Extra |
+----+-------------+-------+------------+------+---------------+------+---------+------+------+----------+-------+
|  1 | SIMPLE      | user  | NULL       | ALL  | NULL          | NULL | NULL    | NULL |    3 |   100.00 | NULL  |
+----+-------------+-------+------------+------+---------------+------+---------+------+------+----------+-------+
*/

-- 查看数据库字符集
show create database wx_test;
/*
+----------+------------------------------------------------------------------+
| Database | Create Database                                                  |
+----------+------------------------------------------------------------------+
| wx_test  | CREATE DATABASE `wx_test` /*!40100 DEFAULT CHARACTER SET utf8 */ |
+----------+------------------------------------------------------------------+
1 row in set (0.00 sec)
*/

-- 修改数据库字符集
alter database test default character set utf8mb4;

-- 查看表的字符集，显示建表语句
show create table user;
/*
+-------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                                                                                                                            |
+-------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| user  | CREATE TABLE `user` (
  `id` bigint(10) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) NOT NULL DEFAULT 'null',
  `age` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 |
+-------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
*/

-- 修改表的字符集
alter table user default character set utf8mb4;

-- 查看mysql版本
status;
/*
--------------
mysql  Ver 14.14 Distrib 5.7.17, for Win64 (x86_64)

Connection id:          8
Current database:       wx_test
Current user:           root@localhost
SSL:                    Not in use
Using delimiter:        ;
Server version:         5.7.17-log MySQL Community Server (GPL)
Protocol version:       10
Connection:             localhost via TCP/IP
Server characterset:    utf8
Db     characterset:    utf8
Client characterset:    gbk
Conn.  characterset:    gbk
TCP port:               3306
Uptime:                 5 days 23 hours 41 min 4 sec

Threads: 1  Questions: 85  Slow queries: 0  Opens: 114  Flush tables: 1  Open tables: 107  Queries per second avg: 0.000
*/

-- 启动mysql服务命令
/etc/init.d/mysqld start
-- 停止mysql服务命令
/etc/inint.d/mysqld stop
-- 重启mysql服务命令
/etc/init.d/mysqld restart

-- 复制表as 与 like
CREATE TABLE IF NOT EXISTS `test` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `label_id` varchar(180) NOT NULL DEFAULT 'null',
  `cou` bigint(20) NOT NULL DEFAULT '0',
  `date` date NOT NULL,
  `hour` int not null DEFAULT '0',
  UNIQUE KEY `date_hour_label_id`(`date`, `hour`, `label_id`),
  PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
insert into test(`label_id`,cou, `date`, hour) values('1', 1314, '2019-07-16', 22);
create table test2 as select * from test;
create table test3 like test;
select * from test2;
/*
+----+----------+------+------------+------+
| id | label_id | cou  | date       | hour |
+----+----------+------+------------+------+
|  1 | 1        | 1314 | 2019-07-16 |   22 |
+----+----------+------+------------+------+
*/
show create table test2;
/*
+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                                                                                                                                                                                 |
+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| test2 | CREATE TABLE `test2` (
  `id` bigint(20) unsigned NOT NULL DEFAULT '0',
  `label_id` varchar(180) CHARACTER SET utf8mb4 NOT NULL DEFAULT 'null',
  `cou` bigint(20) NOT NULL DEFAULT '0',
  `date` date NOT NULL,
  `hour` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 |
+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
*/

show create table test3;
/*
+-------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                                                                                                                                                                                                                                                     |
+-------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| test3 | CREATE TABLE `test3` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `label_id` varchar(180) NOT NULL DEFAULT 'null',
  `cou` bigint(20) NOT NULL DEFAULT '0',
  `date` date NOT NULL,
  `hour` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `date_hour_label_id` (`date`,`hour`,`label_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 |
+-------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)
*/
select * from test3;
/*
Empty set (0.00 sec)
*/

-- as用来创建相同表结构并复制源表数据
-- like用来创建完整表结构和全部索引

-- 存储引擎
/*
MyISAM:这个是默认类型,它是基于传统的ISAM类型,ISAM是Indexed Sequential Access Method (有索引的顺序访问方法) 的缩写,它是存储记录和文件的标准方法.与其他存储引擎比较,MyISAM具有检查和修复表格的大多数工具. MyISAM表格可以被压缩,而且它们支持全文搜索.它们不是事务安全的,而且也不支持外键。如果事物回滚将造成不完全回滚，不具有原子性。如果执行大量的SELECT，MyISAM是更好的选择。


InnoDB:这种类型是事务安全的.它与BDB类型具有相同的特性,它们还支持外键.InnoDB表格速度很快.具有比BDB还丰富的特性,因此如果需要一个事务安全的存储引擎,建议使用它.如果你的数据执行大量的INSERT或UPDATE,出于性能方面的考虑，应该使用InnoDB表


mysql的事务支持与存储引擎有关，MyISAM不支持事务，INNODB支持事务，更新时采用的是行级锁。行级锁并不是直接锁记录，而是锁索引，如果一条SQL语句用到了主键索引，mysql会锁住主键索引；如果一条语句操作了非主键索引，mysql会先锁住非主键索引，再锁定主键索引。

update语句会执行以下步骤：

1、由于用到了非主键索引，首先需要获取非主键列上的行级锁
2、紧接着根据主键进行更新，所以需要获取主键上的行级锁；
3、更新完毕后，提交，并释放所有锁。
*/