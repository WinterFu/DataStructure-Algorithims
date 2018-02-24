#-*- coding:utf-8 -*-
def shell_sort(input_list):
	"""
	input: to be sorted list
	return: ordered list
	modify: 2018-2-24
	author: winter
	"""
	if len(input_list) == 0:
		return []
	result = input_list	
	count = len(result)
	step = 2
	gap = int(count // step)       #计算步长

	while gap > 0:	
		for i in range(gap, count):
			temp = result[i]       # 取出每个gap中的后一个元素
			j = i - gap            # 取每个gap前一个元素的索引
			while j >= 0 and temp < result[j]:
				result[j + gap] = result[j]
				j -= gap
			result[j + gap] = temp 
		gap //= step

	return result


if __name__ == "__main__":
	array1 = [30, 40, 60, 10, 20, 50]
	print("排序前：", array1)
	array2 = shell_sort(array1)
	print("排序后：", array2)