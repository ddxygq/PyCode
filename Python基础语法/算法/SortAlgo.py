# -*- coding:utf-8 -*-


# 冒泡排序
def bubbleSort(arr):
	for i in range(len(arr) - 1):
		for j in range(i+1, len(arr)):
			if arr[i] > arr[j]:
				arr[i],arr[j] = arr[j],arr[i]


# 选择排序
def selectSort(arr):
	for i in range(len(arr) - 1):
		# 使用变量存储最小元素的index
		minIndex = i
		for j in range(i+1, len(arr)):
			if arr[minIndex] > arr[j]:
				minIndex = j
		arr[i],arr[minIndex] = arr[minIndex],arr[i]


# 插入排序
def insertSort(arr):
	for i in range(1,len(arr)):
		temp = arr[i]
		j = i - 1
		while j >= 0 and temp < arr[j]:
			arr[j + 1] = arr[j]
			j = j - 1
		arr[j + 1] = temp


# 快速排序
def quickSort(arr, begin, end):
	if begin < end:
		key = arr[begin]
		i = begin
		j = end
		while i < j:
			while i < j and arr[j] > key:
				j = j - 1
			if i < j:
				arr[i] = arr[j]
				i = i + 1
			while i < j and arr[i] < key:
				i = i + 1
			if i < j:
				arr[j] = arr[i]
				j = j - 1
		arr[i] = key
		quickSort(arr, begin, i - 1)
		quickSort(arr, i + 1, end)


# 堆排序
def heap_sort(arr):
    length = len(arr)

    # 循环 n - 1次
    for i in range(length - 1):
        print('第%s次构建堆' % (i),arr)
        # 建堆
        build_heap(arr, length - 1 - i)

        # 交换堆顶和"最后"一个元素
        arr[0],arr[length - 1 - i] = arr[length - 1 - i], arr[0]

        print('交换后',arr)


# 构建堆
def build_heap(arr, last):
    # 长度为last的堆，最后一个非叶子节点下标索引是(last - 1) / 2
    last_node = int((last - 1)/2)
    # range(4,-1,-1) 表示 [4,3,2,1,0]
    for i in list(range(last_node, -1, -1)):
        k = i
        # 左节点下标
        left = 2*i + 1

        # left < last表命有右子节点，left存储的是左右节点中较大数的下标索引
        if left < last and arr[left] < arr[left + 1]:
            left = left + 1

        # 子节点比父节点大，交换
        if arr[i] < arr[left]:
            # 交换位置，把大数放在上面，小数放在子节点
            arr[i],arr[left] = arr[left],arr[i]


if __name__ == '__main__':
    data = [2,56,7,10,69,5,23,34,12,24,4]
    # bubbleSort(data)
    # selectSort(data)
    # insertSort(data)
    # quickSort(data, 0, len(data) - 1)
    heap_sort(data)
    print(data)