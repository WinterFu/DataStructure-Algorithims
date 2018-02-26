#-*- coding:utf-8 -*-
def adjust_heap(input_list, i, size):
	lchild = 2*i + 1
	rchild = 2*i + 2
	max_index = 1

	if i < size / 2:
		if lchild < size and input_list[lchild] > input_list[max_index]:
			max_index = lchild
		if rchild < size and input_list[rchild] > input_list[max_index]:
			max_index = rchild
		if max_index != i:
			input_list[max_index], input_list[i] = input_list[i], input_list[max_index]
			adjust_heap(input_list, max_index, size)

def build_heap(input_list, size):
	for i in range(0, (size // 2))[::-1]:               #Python3中的 / 得到的是浮点数，// 得到int数据才能放到range中
		adjust_heap(input_list, i, size)

def heap_sort(input_list):
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

	build_heap(result, count)

	for i in range(0, count)[::-1]:                   # 这里的[::-1]是用来逆序的
		result[0], result[i] = result[i], result[0]
		adjust_heap(result, 0, i)
	return result


if __name__ == "__main__":
	array1 = [30, 40, 60, 10, 20, 50]
	print("排序前：", array1)
	array2 = heap_sort(array1)
	print("排序后：", array2)