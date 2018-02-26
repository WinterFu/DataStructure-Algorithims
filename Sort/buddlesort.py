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

	for i in range(0, count)[::-1]:      #需要循环的冒泡的趟数
		for j in range(0, i):            #从头开始两个比较
			if result[j] > result[j+1]:  #如果前者大于后者将前者与后者交换，最终最大值跑到最后面
				result[j], result[j+1] = result[j+1], result[j]

	return result


if __name__ == "__main__":
	array1 = [30, 40, 60, 10, 20, 50]
	print("排序前：", array1)
	array2 = buddle_sort(array1)
	print("排序后：", array2)
