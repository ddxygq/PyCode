import numpy as np
import matplotlib.pyplot as plt


s = [[1, 2, 3],
     [4, 5, 6]]

data = np.array(s)

# 纬度个数
print(data.ndim)

# 纬度
print(data.shape)

# 元素个数
print(data.size)

# 元素类型
print(data.dtype)

# 数组中每个元素占用字节大小
print(data.itemsize)

# 缓冲区包含数组的实际元素
print(data.reshape(3, 2))

print(np.arange(0, 10, 2))

# 常用函数
print(np.sin(np.arange(0, 9).reshape(3, 3)))

# 直方图
mu, sigma = 2, 0.5
v = np.random.normal(mu, sigma, 10000)
plt.hist(v, bins=50, density=1, color='b')

(n, bins) = np.histogram(v, bins=50, density=True)  # NumPy version (no plot)
plt.plot(.5*(bins[1:]+bins[:-1]), n)

plt.show()

# 索引
print(data[0])
