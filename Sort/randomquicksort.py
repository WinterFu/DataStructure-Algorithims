#-*- coding:utf-8 -*-
import random
def random_quick_sort(input_list, left, right):
	"""
	input: to be sorted list, start index and end index
	return: ordered list
	modify: 2018-2-28
	author: winter
	"""
	if left < 0 or right < 0 or left >= right or len(input_list) == 0:
		return input_list

	index = random.randint(left, right)       #产生一个随机的索引值
	result = input_list

	key = result[index]   # select key value
	result[index], result[right] = result[right], result[index]    #随机索引值与最后一个元素互换
	small = left - 1  

	for i in range(left, right):                                   #从头开始遍历与随机索引对应的值进行比较
		if(result[i] < result[right]):
			small += 1
			if small != i:
				result[i], result[small] = result[small], result[i]

	small += 1
	result[small], result[right] = result[right], result[small]

	random_quick_sort(input_list, left, small-1)
	random_quick_sort(input_list, small+1, right)

	return result


if __name__ == "__main__":
	array1 = [30, 40, 60, 10, 20, 50]
	print("排序前：", array1)
	array2 = random_quick_sort(array1, 0, 5)
	print("排序后：", array2)


