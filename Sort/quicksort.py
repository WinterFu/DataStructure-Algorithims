#-*- coding:utf-8 -*-
def quick_sort(lists, left, right):
	"""
	input: to be sorted list, start index and end index
	return: ordered list
	modify: 2018-2-24
	author: winter
	"""
	if left >= right:
		return lists

	key = lists[left]   # select key value
	low = left
	high = right
	while low < high:
		while low < high and lists[high] >= key:
			high-=1

		lists[low] = lists[high]
		while low < high and lists[low] <= key:
			low += 1

		lists[high] = lists[low]

	lists[high] = key

	quick_sort(lists, left, low-1)
	quick_sort(lists, low+1, right)

	return lists


if __name__ == "__main__":
	array1 = [30, 40, 60, 10, 20, 50]
	print("排序前：", array1)
	array2 = quick_sort(array1, 0, 5)
	print("排序后：", array2)


