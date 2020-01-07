# -*- coding: utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt


def helperView():
	x = np.array(range(0, 18))
	count = [613152
		, 834744
		, 966151
		, 1073790
		, 1189851
		, 1422016
		, 2136359
		, 6934936
		, 22137318
		, 31830293
		, 37177294
		, 40082233
		, 42489910
		, 44566613
		, 46607195
		, 48317698
		, 49938874
		, 51364484]

	y = np.array(count)

	plt.plot(x, y)
	plt.scatter(x, y, c='r', s=400, alpha=0.5)

	# 设置坐标轴刻度
	plt.xticks(x)

	# 设置坐标轴标题
	plt.xlabel("小时", fontsize=13, fontweight='bold')

	# 解决中文显示问题
	plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
	plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

	plt.savefig('C:/Users/Administrator/Desktop/a.png')
	plt.show()


if __name__ == '__main__':
	helperView()
