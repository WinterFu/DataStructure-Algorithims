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
	small = left - 1                                               #记录的是比索引值对应元素小的元素的索引

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
	n = input("请输入要排序数的个数:")
	print("生成%d个随机数中......" % int(n))
	array1 = random.sample(range(100), int(n))
	print("生成的随机数列为：", array1)
	array2 = random_quick_sort(array1)
	print("排序后序列为：", array2)


