#-*- coding:utf-8 -*-
def merge(left, right):
	i, j = 0, 0
	merge_list = []
	while i < len(left) and j < len(right):       #扫描第一段和第二段序列直到有一个扫描结束
		if left[i] <= right[j]:                   #判断第一段序列和第二段序列中取出的数哪个更小，将其存入合并序列中，并继续向下扫描
			merge_list.append(left[i])
			i += 1
		else:
			merge_list.append(right[j])
			j += 1
	merge_list += left[i:]    #若第一段序列未扫描完，将其全部复制加到序列后面
	merge_list += right[j:]   #若第二段序列未扫描完，将其全部复制加到序列后面

	return merge_list

def merge_sort(input_list):
	"""
	input: to be sorted list
	return: ordered list
	modify: 2018-2-26
	author: winter
	"""
	if len(input_list) <= 1:
		return input_list
	count = len(input_list)
	result = input_list
	num = count // 2
	left = merge_sort(result[:num])
	right = merge_sort(result[num:])
	return merge(left, right)



if __name__ == "__main__":
	n = input("请输入要排序数的个数:")
	print("生成%d个随机数中......" % int(n))
	array1 = random.sample(range(100), int(n))
	print("生成的随机数列为：", array1)
	array2 = merge_sort(array1)
	print("排序后序列为：", array2)

