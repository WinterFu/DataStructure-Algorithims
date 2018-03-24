#-*- coding:utf-8 -*-
def getPermutation(str_nums):
	res = []
	if len(str_nums) == 0:
		return res

	permutation(str_nums, res, 0)
	return res



def permutation(strs, res, cur):
	length = len(strs)
	if(cur == length):
		res.append(strs)
		return
	strs = [int(x) for x in strs]
	for i in range(cur, length):
		strs[i], strs[cur] = strs[cur], strs[i]
		permutation(strs, res, cur + 1)
		strs[i], strs[cur] = strs[cur], strs[i]
	
if __name__ == "__main__":
	test_str = "abc"
	result = getPermutation(test_str)
	print(result)
	 