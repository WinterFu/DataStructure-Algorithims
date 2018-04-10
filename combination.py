#-*- coding:utf-8 -*-

def dfs(string, index, result):
	if(index == len(string)):
		print(result)
		return
	result.append(string[index])
	dfs(string, index + 1, result)
	result.pop()
	dfs(string, index+1, result)


#从头扫描字符串得到第一个字符，针对第一个字符，有两种选择  
#把这个字符放到组合中去，接下来我们需要在剩下的n-1个字符中选取m-1个字符；  
#如果不把这个字符放到组合中去，则需要在剩下的n-1个字符中选取m个字符 
#这个可以实现取出任意k(k<=n)个数字的组合
def combination(nums, index, result):
	if(index == 0):
		print(result)
		return

	if len(nums) == 0:
		return

	result.append(nums[0])
	combination(nums[1:], index - 1, result)   #注意这里当nums只含有一个元素时nums[1：]得到的是一个空列表，当然对于一个空列表这样也会返回空
	result.pop()
	combination(nums[1:], index, result)

#运用位图的思想，先看字符串的长度n，然后则可以知道不算空串的所有组合为2^n - 1
#例如 001-->a; 011-->b，因此遍历组合数目，然后判断其哪一位为1，如果为1则输出对应的字符。
def Bit_Combination(string):
	n = len(string)
	comb_num = 1<<n

	for i in range(comb_num):       #注意这里是从0开始，也就是意味着把[]也作为一种组合
		res =[]
		for j in range(n):
			if(i &(1<<j)):          #判断哪一位为1
				res.append(string[j])

		print(res)

#稍微做一下变形，输出任意k(k<=n)个元素的组合，这里只需要设计一个counter计数器，满足k的输出即可
#当然这还是把所有组合都算了一遍
def Bit_Combination_k(string, k):
	n = len(string)
	comb_num = 1<<n

	for i in range(comb_num):       #注意这里是从0开始，也就是意味着把[]也作为一种组合
		res =[]
		counter = 0
		for j in range(n):
			if(i &(1<<j)):          #判断哪一位为1
				res.append(string[j])
				counter+=1
		if counter == k:
			print(res)

#判断一个字符串是否为回文
def is_palindrome(string):
	op_string = string[::-1]    #或者转换成列表使用内置的l.reverse()函数，然后再''.jion(s)将列表转换成字符串

	return True if op_string == string else False  #或者string.find(op_string, 0, len(string)),这里完全一样返回0索引，要注意对应是true

if __name__ == "__main__":
	s = 'abbcbba'
	if(is_palindrome(s)):
		print("Yes!")
	else:
		print("No!")
	res = []
	a = [1,2,3]
	# for i in range(3):
	# 	combination(a, i, res)
	#Bit_Combination(a)
	dfs(a, 0, res)