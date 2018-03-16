# 使用快速排序，时间复杂度为O(nlogn)
# 二分法查找的时间复杂度为O(logn)
def quicksort(array):
	if len(array)<2:
		# 基线条件：为空或只包含一个元素的数组是有序的
		return array 
	else:
		pivot = array[0] # 基线条件
		less = [i for i in array[1:] if i <= pivot]#由所有小于等于基线值的元素组成
		greater = [i for i in array[1:] if i > pivot]#由所有大于基线值的元素组成
	return quicksort(less) + [pivot] + quicksort(greater)	
print(quicksort([10,5,2,4]))
