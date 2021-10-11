import numpy as np
import matplotlib.pyplot as plt
from 线性回归最小二乘法矩阵实现 import LinearRegression as LR
from 多项式回归 import PolynomialRegression as PR

'''
惩罚项：亦称为罚项、正则项，用于限制模型复杂度，在公式上可看到是增加了某个约束条件，即：subject to xxxx；

以多项式回归理解惩罚项：
对于二元二次多项式回归，所有假设空间可能为：w0*x0^2+w1*x1^2+w2*x0*x1+w3*x0+w4*x1+b
当二阶多项式过拟合时，通常考虑退回到一阶，即线性回归，假设空间为：w0*x0+w1*x1+b
这种退化可以看到是对二阶多项式增加了约束条件：w0=0,w1=0,w2=0
因此对于多项式回归，任意低阶都可以看作是其高阶+惩罚项的组合结果

惩罚项的意义：通过对公式增加灵活的约束条件，可以更平滑的控制模型复杂度，只要约束条件是有意义的，那么它就降低了原假设空间的大小，例如对于线性回归w0*x0+b，W=(w0 w1)，即W的可取范围为整个二维平面，如果增加约束条件w0^2+w1^2<r^2，则W的取值范围为二维平面上以r为半径的圆内，而W决定了线性回归的假设空间大小，因此通过约束条件得以降低假设空间大小的目的；

岭回归 = 线性回归 + 优化目标(argmin MSE)上增加约束条件(s.t. ||w||^2<=r^2)
'''


class RidgeRegression(PR):
    def __init__(self, X, y, degrees=1, lambdaVal=0):
        super(RidgeRegression, self).__init__(X, y, degrees)
        self.lambdaVal = lambdaVal

    def train(self):
        if self.lambdaVal == 0:
            return super(RidgeRegression, self).train()
        xTx = self.X.T @ self.X
        I = np.eye(xTx.shape[0])
        self.w = np.linalg.inv(xTx + self.lambdaVal * I) @ self.X.T @ self.y
        self.w = self.w.reshape(-1)
        self.w, self.b = self.w[1:], self.w[0]
        return self.w, self.b


def pain(pos=141, xlabel='x', ylabel='y', title='', x=[], y=[], line_x=[], line_y=[]):
    plt.subplot(pos)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.scatter(x, y)
    plt.plot(line_x, line_y)


if __name__ == '__main__':
    rnd = np.random.RandomState(3)
    x_min, x_max = 0, 10


    def pain(pos=141, xlabel='x', ylabel='y', title='', x=[], y=[], line_x=[], line_y=[]):
        plt.subplot(pos)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.scatter(x, y)
        plt.plot(line_x, line_y)


    # 上帝函数 y=f(x)
    def f(x):
        return x ** 5 - 22 * x ** 4 + 161 * x ** 3 - 403 * x ** 2 + 36 * x + 938


    # 上帝分布 P(Y|X)
    def P(X):
        return f(X) + rnd.normal(scale=30, size=X.shape)


    # 通过 P(X, Y) 生成数据集 D
    X = rnd.uniform(x_min, x_max, 10)  # 通过均匀分布产生 X
    y = P(X)  # 通过 P(Y|X) 产生 y

    X, y = X.reshape(-1, 1), y.reshape(-1, 1)
    x_min, x_max = min(X), max(X)

    for pos, deg in zip([331, 332, 333], [2, 5, 10]):
        model = PR(X=X, y=y, degrees=deg)
        w, b = model.train()
        print(f'最小二乘法的矩阵方式结果为：w={w} b={b}')
        line_x = [x_min + (x_max - x_min) * (i / 100) for i in range(-1, 102, 1)]
        line_y = [model.predict(x) for x in line_x]
        pain(pos, 'X', 'y', 'DEG=' + str(deg), X[:, 0], y[:, 0], line_x, line_y)
    for pos, deg, lambdaVal in zip([334, 335, 336], [5, 5, 5], [0.1, 1, 10]):
        model = RidgeRegression(X=X, y=y, degrees=deg, lambdaVal=lambdaVal)
        w, b = model.train()
        print(f'最小二乘法的矩阵方式结果为：w={w} b={b}')
        line_x = [x_min + (x_max - x_min) * (i / 100) for i in range(-1, 102, 1)]
        line_y = [model.predict(x) for x in line_x]
        pain(pos, 'X', 'y', 'DEG=' + str(deg) + ', λ=' + str(lambdaVal), X[:, 0], y[:, 0], line_x, line_y)
    for pos, deg, lambdaVal in zip([337, 338, 339], [10, 10, 10], [0.1, 1, 10]):
        model = RidgeRegression(X=X, y=y, degrees=deg, lambdaVal=lambdaVal)
        w, b = model.train()
        print(f'最小二乘法的矩阵方式结果为：w={w} b={b}')
        line_x = [x_min + (x_max - x_min) * (i / 100) for i in range(-1, 102, 1)]
        line_y = [model.predict(x) for x in line_x]
        pain(pos, 'X', 'y', 'DEG=' + str(deg) + ', λ=' + str(lambdaVal), X[:, 0], y[:, 0], line_x, line_y)

    plt.show()