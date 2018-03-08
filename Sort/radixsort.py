#-*- coding:utf-8 -*-
import math
def radix_sort(input_list):
	"""
	input: to be sorted list
	return: ordered list
	modify: 2018-3-1
	author: winter
	"""
	if len(input_list) == 0 :
		return input_list

	n = len(input_list)
	'''
	此处是用来求最大位数的，因为求位数涉及到除10操作，因此我们可以借助对数
	max_num = max(input_list)   #max value
	bits_num = 0
	while(max_num):             #get max bits
		bits_num += 1
		max_num /= 10
	'''
	bits_num = int(math.ceil(math.log10(max(input_list))))     #一句话解决是不是很easy，同样对于除2除3，除以任何正数的都可以用对数

	bucket = [[] for i in range(10)]   #set bucket

	for i in range(1, bits_num+1):
		for j in input_list:
			bucket[j % (10**(i)) // (10**(i-1))].append(j)     #取到某一位的数值
		del input_list[:]                                      #销毁掉之前数组
		for z in bucket:                                       #重新分配索引
			input_list += z
			del z[:]

	return input_list

if __name__ == "__main__":
	array1 = [30, 40, 60, 10, 20, 50]
	print("排序前：", array1)
	array2 = radix_sort(array1)
	print("排序后：", array2)

