import random
import matplotlib.pyplot as plt


def flip_plot(minExp, maxExp):
    """
    Assumes minExp and maxExp positive integers; minExp < maxExp
    Plots results of 2**minExp to 2**maxExp coin flips
    """
    # 两个参数的含义，抛硬币的次数为2的minExp次方到2的maxExp次方，也就是一共做了(2**maxExp - 2**minExp)批次实验，每批次重复抛硬币2**n次

    ratios = []
    xAxis = []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        numHeads = 0 # 初始化，硬币正面朝上的计数为0
        for n in range(numFlips):
            if random.random() < 0.5:  # random.random()从[0, 1)随机的取出一个数
                numHeads += 1  # 当随机取出的数小于0.5时，正面朝上的计数加1
        numTails = numFlips - numHeads  # 得到本次试验中反面朝上的次数
        ratios.append(numHeads/float(numTails))  #正反面计数的比值
    plt.title('Heads/Tails Ratios')
    plt.xlabel('Number of Flips')
    plt.ylabel('Heads/Tails')
    plt.plot(xAxis, ratios)
    plt.hlines(1, 0, xAxis[-1], linestyles='dashed', colors='r')
    plt.show()


flip_plot(4, 16)