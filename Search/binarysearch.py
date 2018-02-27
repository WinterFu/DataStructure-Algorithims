#-*- coding:utf-8 -*-
def binary_search(input_list, key):
	"""
	input: to be searched list(must be orderd) and key vlaue
	return: search yes or not 
	modify: 2018-2-27
	author: winter
	"""
	if len(input_list) == 0:
		return False
	low = 0
	high = len(input_list) - 1
	while(low <= high):
		mid = (low + high) // 2
		if(input_list[mid] == key):
			return mid                    #查找成功直接返回位置
		elif(input_list[mid] < key):      #关键字大于中间位置的值，则在大值区间[mid+1, high]继续查找
			low = mid + 1
		else:                             #关键字小于中间位置的值，则在小值区间[low, mid-1]继续查找
			high = mid -1

	return False

if __name__ == "__main__":
	array1 = [10, 20, 30, 40, 50, 60, 70]
	print("30 is in the array1 or not ?", binary_search(array1, 30))
	print("80 is in the array1 or not ?", binary_search(array1, 80))
