#-*- coding:utf-8 -*-
def buddle_sort(input_list):
	"""
	input: to be sorted list
	return: ordered list
	modify: 2018-2-24
	author: winter
	"""
	if len(input_list) == 0:
		return []
	count = len(input_list)
	result = input_list

	for i in range(0, count):
		for j in range(i+1, count):
			if result[i] > result[j]:
				result[i], result[j] = result[j], result[i]

	return result


if __name__ == "__main__":
	array1 = [30, 40, 60, 10, 20, 50]
	print("排序前：", array1)
	array2 = buddle_sort(array1)
	print("排序后：", array2)
