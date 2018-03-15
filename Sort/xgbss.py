#-*- coding:utf-8 -*-
import random
def search_target_sep(num_set, target):
	num_set.sort()

	res = []
	for i in range(len(num_set))[::-1]:
		if num_set[i] == target:
			res.append(num_set)
			continue
		elif num_set[i] > target:
			continue

		else:
			if(target - num_set[i])  in num_set[:i]:
				res.append(num_set[i])
				res.append(target - num_set[i])
			search_target_sep(num_set[:i], target - num_set[i])

	return res


if __name__ == "__main__":
	test_num = [2 ,2 ,3 ,4,7]
	result = search_target_sep(test_num, 7)
	print(result)




