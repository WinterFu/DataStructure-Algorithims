#-*- coding:utf-8 -*-
def insert_sort(input_list):
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

	for i in range(1, count):
		key = result[i]
		j = i-1       #为key在前面的lists[0..i-1]有序区间找一个合适的位置
		while j >= 0:
			if result[j] > key:         #如果当前值大于key值那么将当前值后移一位，key值变成当前值
				result[j+1] = result[j]
				result[j] = key
			j-=1

	return result


if __name__ == "__main__":
	array1 = [30, 40, 60, 10, 20, 50]
	print("排序前：", array1)
	array2 = insert_sort(array1)
	print("排序后：", array2)