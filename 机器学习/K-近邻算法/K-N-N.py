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
