#-*- coding:utf-8 -*-

n = int(input())
lamp_num = set()

for i in range(n):
	switch_num = input().split()
	switch_num = [int(j) for j in switch_num]
	for m in range(1,len(switch_num)):
		lamp_num.add(switch_num[m])

print(len(lamp_num))




def leaststicknum(n):
	max_num = 15
	d, p = 1, 2
	drop_array = [1]
	while(p <= max_num):
		drop_array.append(p)
		d, p = p, d + p
	stick_len_array = [i+1 for i in range(n)]
	print(drop_array, stick_len_array)

	return len(set(drop_array) & set(stick_len_array)) - 2

if __name__ == "__main__":
	n = 5
	min_sticks = leaststicknum(n)
	print(min_sticks)


