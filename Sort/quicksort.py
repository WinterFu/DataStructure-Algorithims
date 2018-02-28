#-*- coding:utf-8 -*-
def quick_sort(input_list, left, right):
	"""
	input: to be sorted list, start index and end index
	return: ordered list
	modify: 2018-2-24
	author: winter
	"""
	if left >= right:
		return input_list

	key = input_list[left]   # select key value
	low = left
	high = right
	while low < high:
		while low < high and input_list[high] >= key:
			high-=1

		input_list[low] = input_list[high]
		while low < high and input_list[low] <= key:
			low += 1

		input_list[high] = input_list[low]

	input_list[low] = key

	quick_sort(input_list, left, low-1)
	quick_sort(input_list, low+1, right)

	return input_list


if __name__ == "__main__":
	array1 = [30, 40, 60, 10, 20, 50]
	print("排序前：", array1)
	array2 = quick_sort(array1, 0, 5)
	print("排序后：", array2)
