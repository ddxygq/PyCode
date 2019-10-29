近朱者赤，近墨者黑，是有一定道理的。我们为人处世的潜意识，通常告诉我们，一个人与众多成功者（比如马云）在一起，谈笑风生、指点江山，我们会认为，这个人很可能是个成功者；如果一个人在跟北海道大街上成天跟几个混混厮混一起，招摇过市，欺男霸女，我们通常认为，这个人很差劲！

`K`-近邻算法就是这样的一种算法。具体是，通过寻找测试对象`Obj`最近的`K`个样本对象，假设`K=4`，经过计算，与`Obj`最近的4个对象集合所属类别为，`K_Set=[A, B, B, B]`，`A：1`次，`B：3`次，我们判定`Obj`测试对象属于类别`B`。

# 一、k-近邻算法的原理
KNN 属于有监督的分类算法，也就是说，KNN 是通过 有标签 的样本集进行训练，并通过样本集数据对测试对象进行 分类 的算法。
KNN 的原理也很简单，通过选取样本集中 K 个离测试对象最近的样本，然后根据这 K 个样本的类型对测试对象进行分类。这也是算法名称中 K 的来历。
通过算法的原理我们也可以了解到，实现 KNN 算法的关键在于：样本集、距离的计算、K 值的选取。

# 二、距离计算
计算距离通常可以使用距离平方和
![](source/image/0.jpg)
或者欧几里得距离
![](source/image/1.jpg)
曼哈顿距离计算公式
![](source/image/2.jpg)
这里使用欧几里得距离。

# 三、K-近邻算法特点
K-近邻特点分为优点与缺点：

优点：

-简单易实现，分类精度高，异常值不敏感，没有假设条件；

缺点：

- 计算时间复杂度高、空间复杂度高；
- 分类结果受到学习样本分布均衡性影响较大；

# 四、代码
```python
import numpy as np
import matplotlib.pyplot as plt


def create_dataset():
    group = np.array([
        [1.0,1.1]
        , [0, 0]
        , [1.1, 0.9]
        , [1.3, 1.1]
        , [1.0, 1.0]
        , [0,0.1]
        , [0.1, 0.5]
    ])

    labels = ['A', 'A', 'A', 'A', 'B', 'B', 'B']

    return group, labels


def classify0(inX, dataset, labels, k):
    dataset_size = dataset.shape[0]
    diff = np.tile(inX, (dataset_size, 1)) - dataset
    sqrt_diff = diff ** 2
    dist = (sqrt_diff.sum(axis=1)) ** 0.5
    print('距离 -> ', dist)
    sort_dist = dist.argsort()
    print('距离排序下标 ->', sort_dist)

    class_count = {}
    for i in range(k):
        vote_label = labels[sort_dist[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1

    sorted_class_count = sorted(class_count.items(), key=lambda item: item[1], reverse=True)

    return sorted_class_count, sorted_class_count[0][0]


if __name__ == '__main__':
    obj = np.array([1.1, 0.8])
    group, labels = create_dataset()
    # A 类
    plt.scatter(group[0:3, 0], group[0:3, 1], c='b', s=300, alpha=0.5)
    # B 类
    plt.scatter(group[4:, 0], group[4:, 1], c='r', s=400, alpha=0.5)
    # 测试对象
    plt.scatter(obj[0], obj[1], c='g', s=500, alpha=0.5)
    plt.show()
    result, clas = classify0(obj, group, labels, 3)
    print('结果 ->', result, clas)
```
结果
```
距离 ->  [0.31622777 1.36014705 0.1        0.36055513 0.2236068  1.30384048
 1.04403065]
距离排序下标 -> [2 4 0 3 6 5 1]
结果 -> [('A', 2), ('B', 1)] A
```
代码中约定：蓝色：A类，红色：B类，绿色：待分类对象。
![]()
`('A', 2), ('B', 1)`，待预测对象属于A类。