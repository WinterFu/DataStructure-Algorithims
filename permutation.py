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


def permutation0(strs):
	length = len(strs)
	if length <= 1:
		return strs

	res = []
	for i in range(length):
		temp = strs.copy()
		del(temp[i])

		res += [strs[i] + j for j in permutation0(temp)]
	return res

def permutation1(strs, k):
	length = len(strs)
	if k <= 1:
		return strs

	res = []
	for i in range(length):
		temp = strs.copy()
		del(temp[i])

		res += [strs[i] + j for j in permutation1(temp, k-1)]
	return res

if __name__ == "__main__":
	test_str = "abc"
	test_arr = [i for i in test_str]
	result = permutation1(test_arr, 2)
	print(result)
	 