#-*- coding:utf-8 -*-
def MinandMax(str_num):
	if len(str_num) != 6:
		return 0
	nums = [int(x) for x in str_num]
	nums.sort()
	n = len(nums)
	over_5index = n - 1;
	min_time = []
	for i in range(n):
		if nums[i] > 5:
			over_5index = i
			break

	if over_5index < n:
		if over_5index == n-1:
			min_time += nums
		elif over_5index == n - 2:
			min_time += nums[0:3]
			min_time.append(nums[n-2])
			min_time.append(nums[3])
			min_time.append(nums[-1])
		elif over_5index == n - 3:
			min_time += [nums[0], nums[0+3]]
			min_time += [nums[1], nums[1+3]]
			min_time += [nums[2], nums[2+3]]
		else:
			return []
	return min_time


if __name__ == "__main__":
	#s = input("Please input nums str:")
	s = '264667'
	min_Time = MinandMax(s)
	print("The min time is:\n%d%d:%d%d:%d%d" % (min_Time[0], min_Time[1], min_Time[2], min_Time[3], min_Time[4], min_Time[5]))

