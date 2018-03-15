#-*- coding:utf-8 -*-
#只有一组是满足答案的
def twoSum(nums, target):
	if len(nums) < 2 or target <= 1:
		print("It is error input!!!")

	dic_num = {}
	for i in range(len(nums)):
		dic_num[nums[i]] = i

	key_list = list(dic_num.keys())
	#print(key_list)
	for j in key_list:
		if(target - j) in key_list:
			print(dic_num[j], dic_num[target - j])
			break



if __name__ == "__main__":
	test_num = [2,4,5,1,9,0,8]
	search_targesum(test_num, 12)



#优秀答案
def twoSum(nums, target):
	d = {}

	for i, num in enumerate(nums):
		if target - num in d:
			return [d[target - num], i]
		d[num] = i
