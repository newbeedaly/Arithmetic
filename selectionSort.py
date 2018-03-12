# 简单的选择排序
def findSmallest(arr):
	smallest = arr[0] # 存储最小的值
	smallest_index = 0 # 存储最小元素的索引
	for i in range(1,len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i 
	return smallest_index

def selectionSort(arr): # 对数组进行排序
	newArr = []
	for i in range(len(arr)):
		smallest_index = findSmallest(arr) #找出最小的数组元素并将其加入新数组
		newArr.append(arr.pop(smallest_index))
	return newArr

print(selectionSort([5,3,6,2,10]))

