#-*- coding:utf-8 -*-

n = int(input())
lamp_num = set()

for i in range(n):
	switch_num = input().split()
	switch_num = [int(j) for j in switch_num]
	for m in range(1,len(switch_num)):
		lamp_num.add(switch_num[m])

print(len(lamp_num))




