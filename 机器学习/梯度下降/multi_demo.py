import random


# 向量内积函数
def dot(m, n):
    return (sum(m_i * n_i for m_i, n_i in zip(m, n)))


# 平均值函数
def mean(x):
    return (sum(x) / len(x))


# 计算协方差
####-----要计算一个序列方差只需covariance(x,x)即可---####
def de_mean(x):
    x_bar = mean(x)

    return ([x_i - x_bar for x_i in x])


def covariance(x, y):
    return (dot(de_mean(x), de_mean(y)) / (len(x) - 1))


# 计算相关系数
import math


def correlation(x, y):
    s_x = math.sqrt(covariance(x, x))
    s_y = math.sqrt(covariance(y, y))

    return (covariance(x, y) / (s_x * s_y))


# -----------------【最小二乘法】线性回归系数求法--------------
def line_coef(x, y):
    s1 = covariance(x, x) * (len(x) - 1)
    s2 = dot(y, de_mean(x))
    beta = s2 / s1
    alpha = mean(y) - beta * mean(x)

    return (alpha, beta)

# *********实验************
# 由于暂时没有实验数据，这里生成【随机干扰】数据
import random as rdm


# from numpy import *
def ran(a1, a2, x):
    return [a1 + a2 * x_i + 2.5 * random.random() for x_i in x]


a1 = 1.5
a2 = 2.5
x = range(20)
y = ran(a1, a2, x)
# 线性拟合
alpha, beta = line_coef(x, y)
print('*------------最小二乘法-------------*')
print('系数为：', alpha, beta)

# 可视化
import matplotlib.pyplot as plt

# 开一个【2x2】的图像窗口
# plt.subplot(221)
plt.figure(1)
plt.scatter(x, y, marker='*', color='b')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Linear Fit')
# 拟合直线
plt.plot(x, [alpha + beta * x_i for x_i in x], color='orange')
# plt.subplot(222)
plt.show()


# 误差分析
# -----主要考察:(1)误差平方和;(2)R方（越大拟合得越好）
def err(alpha, beta, x, y):  # 返回每个实际y值与拟合值差向量
    return ([y_i - (alpha + beta * x_i) for x_i, y_i in zip(x, y)])


def error_total(alpha, beta, x, y):
    y1 = err(alpha, beta, x, y)

    return (dot(y1, y1))

print('误差为：', error_total(alpha, beta, x, y))


# 计算R方

def r_square(alpha, beta, x, y):
    return (1 - error_total(alpha, beta, x, y) / covariance(y, y))


R_square = r_square(alpha, beta, x, y)
print('R方：', R_square)
if (R_square > 0.95):
    print('在0.05置信水平下，该线性拟合不错!')
else:
    print('在0.05置信水平下，该线性拟合效果不佳!')