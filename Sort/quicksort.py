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
	n = input("请输入要排序数的个数:")
	print("生成%d个随机数中......" % int(n))
	array1 = random.sample(range(100), int(n))
	print("生成的随机数列为：", array1)
	array2 = quick_sort(array1)
	print("排序后序列为：", array2)

