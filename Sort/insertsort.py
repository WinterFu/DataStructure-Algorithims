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
	n = input("请输入要排序数的个数:")
	print("生成%d个随机数中......" % int(n))
	array1 = random.sample(range(100), int(n))
	print("生成的随机数列为：", array1)
	array2 = insert_sort(array1)
	print("排序后序列为：", array2)
