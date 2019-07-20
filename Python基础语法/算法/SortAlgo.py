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

def insertSort(arr):
	for i in range(1,len(arr)):
		temp = arr[i]
		j = i - 1
		while j >= 0 and temp < arr[j]:
			arr[j + 1] = arr[j]
			j = j - 1
		arr[j + 1] = temp

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

if __name__ == '__main__':
	data = [2,56,7,10,69,5,23,34,12,24,4]
	# bubbleSort(data)
	# selectSort(data)
	# insertSort(data)
	quickSort(data, 0, len(data) - 1)
	print(data)