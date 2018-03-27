#-*- coding:utf-8 -*-

def judge(l):
	return sum(l) % 3 == 0


if __name__ == "__main__":
	buf = []
	cnt = 0

	for i in range(1, 12 ):
		buf.append(i)

		if judge(buf):
			cnt += 1

	print(cnt)	