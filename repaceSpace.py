#-*- coding:utf-8 -*-
def replace_space(input_str, specify_str):
	"""
	input: to be replaced str and specify str
	return: new str
	modify: 2018-3-7
	author: winter
	"""
	if len(input_str) == 0:
		return 
	count1 = len(input_str)
	count2 = input_str.count(' ')   #计算空格的个数，无论是list还是str都可计算某个元素出现的次数
	result = ''

	for i in range(0, count1):      #遍历原始字符串
		if input_str[i] != ' ':
			result += input_str[i]
		else:
			result += specify_str
	return result


if __name__ == "__main__":
	str1 = 'I am a student'
	spe_str = 'zz'
	print("替换前：", str1)
	str2 = replace_space(str1, spe_str)
	print("替换后：", str2)


"""
更简单一点的办法就是: input_str.replace(' ', 'zz')
"""