#-*- coding:utf-8 -*-
import math
import random
def radix_sort(input_list):
	"""
	input: to be sorted list
	return: ordered list from small to big
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
	result = input_list
	bits_num = int(math.ceil(math.log10(max(input_list))))     #一句话解决是不是很easy，同样对于除2除3，除以任何正数的都可以用对数

	bucket = [[] for i in range(10)]   #set bucket

	for i in range(1, bits_num+1):
		for j in result:
			#bucket[j % (10**(i)) // (10**(i-1))].append(j)     #取到某一位的数值
			bucket[(j // 10**(i-1)) % 10].append(j)             #取到某一位的数值
		del result[:]                                           #销毁掉之前数组
		for z in bucket:                                        #重新分配索引
			result += z                                         #将多个列表组合成一个，列表字符串都可以用+操作
			del z[:]                                            #这一步是将z清除，也是将bucket清空

	return result

if __name__ == "__main__":
	n = input("请输入要排序数的个数:")
	print("生成%d个随机数中......" % int(n))
	array1 = random.sample(range(100), int(n))                  #在输入的序列中随机取n个不重复随机数
	print("生成的随机数列为：", array1)
	array2 = radix_sort(array1)
	print("排序后序列为：", array2)

