#-*- coding:utf-8 -*-
def merge(left, right):
	i, j = 0, 0
	result = []
	while i < len(left) and j < len(right) :
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	result += left[i:]
	result += right[j:]

	return result

def merge_sort(input_list):
	"""
	input: to be sorted list
	return: ordered list
	modify: 2018-2-26
	author: winter
	"""
	if len(input_list) <= 1:
		return input_list
	count = len(input_list)
	result = input_list
	num = count // 2
	left = merge_sort(result[:num])
	right = merge_sort(result[num:])
	return merge(left, right)



if __name__ == "__main__":
	array1 = [30, 40, 60, 10, 20, 50]
	print("排序前：", array1)
	array2 = merge_sort(array1)
	print("排序后：", array2)
