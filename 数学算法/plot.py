# -*- coding: utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt

def logistic(x):
	return 1 / (1 + math.exp(-x))

def logistic_plot():
	x = np.random.randint(0, 15, (1, 40))
	y = map(logistic, x)
	print(x,y)
	plt.plot(x, y)


if __name__ == '__main__':
	logistic_plot()