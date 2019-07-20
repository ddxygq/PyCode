# -*- coding:utf-8 -*-

import numpy as np
import random as rd
import matplotlib.pyplot as plt
import math

def printLine():
   print '----------------------------------------------------------------------------'

#计算聚类中心
def cent(x):
   return(sum(x)/len(x))

#距离, 返回s,C，分别是距离平方和与聚类方案
def f(center):
	# c0 = []
	# c1 = []
	# c2 = []
	c = [[] for i in range(k)]
	D = np.arange(k*n).reshape(k,n)
	d = np.array([center[i]-dat.T for i in range(k)])
	for i in range(k):
		D[i] = sum((d[i]**2).T)
	for i in range(n):
		ind = D.T[i].argmin()
		c[ind].append(i)
	C = [np.array([dat.T[i] for i in j]) for j in c]
	print(c)
	s = 0
	for i in C:
		s+=dist(i)
	return(s,C)

#计算各点到聚类中心的距离之和
def dist(x):
	#聚类中心
	m0 = cent(x)
	dis = sum(sum((x-m0)**2))
	return dis

def run():
	# 存储距离和
	s_sum = []
	#---随机产生聚类中心----#
	center = rd.sample(range(n),k)
	center = np.array([dat.T[i] for i in center])
	print '初始化聚类中心为：'.decode('utf-8')
	print(center)
	printLine()
	#初始距离和
	print '第1次计算！'.decode('utf-8')
	dd,C = f(center)
	s_sum.append(dd)
	print ('距离和为'+str(dd)).decode('utf-8')
	printLine()
	print('第2次计算！'.decode('utf-8'))
	center = [cent(i) for i in C]
	Dd,C = f(center)
	s_sum.append(Dd)
	print ('距离和为'+str(Dd)).decode('utf-8')
	# 前面已经计算2次了，所以这里从第三次开始计算
	K = 3
	while(K<n_max):
	   printLine()
	   #两次差值很小并且计算了一定次数
	   if(math.sqrt(abs(dd-Dd)) < 0 and K>20):
	      break;
	   print ('第'+str(K)+'次计算！').decode('utf-8')
	   dd = Dd
	   print ('距离和为'+str(dd)).decode('utf-8')
	   #当前聚类中心
	   center = [cent(i) for i in C]
	   Dd,C = f(center)
	   s_sum.append(Dd)
	   K+=1

	#-----------------聚类结果可视化部分--------------------#
	j = 0
	for i in C:
	   if(j == 0):
	      plt.plot(i.T[0],i.T[1],'ro')
	   if(j == 1):
	      plt.plot(i.T[0],i.T[1],'b+')
	   if(j == 2):
	      plt.plot(i.T[0],i.T[1],'g*')
	   if(j == 3):
	      plt.plot(i.T[0],i.T[1], 'c<')
	   j+=1
	plt.show()
	x = range(len(s_sum))
	plt.plot(x, s_sum)
	plt.plot(x, s_sum, 'ro')
	plt.show()


print '==============================================================================='
#数据
'''
dat = np.array([[14,22,15,20,30,20,32,13,23,20,21,22,23,24,35,18,20,31,14]
	,[15,28,18,30,35,15,30,15,25,23,24,25,26,27,30,15,24,33,12]])
'''
dat = np.random.randint(0, 15, (2, 40))
# dat = dat / float(dat[0].max())
print(dat)
#=========================聚类中心======================#
n = len(dat[0])
k = 4

# 最大训练次数
n_max = 50

# 程序入口
if __name__ == '__main__':
	print '==============================================================================='
	run()