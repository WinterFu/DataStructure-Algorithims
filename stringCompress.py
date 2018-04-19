#-*- coding:utf-8 -*-

def string_compress(string):
	if len(string) == 0:
		return
	res = ''
	n = len(string)
	for i in range(n):
		if (i != n-1) and string[i] == string[i+1]:   #这里增加前面那个条件，是为了防止字符串越界
			continue
		else:
			if string.count(string[i]) > 1:
				res += str(string.count(string[i]))
				res += string[i]
			else:
				res += string[i]

	if(len(string) == len(res)):
		print(string)
	else:
		print(res)

if __name__ == "__main__":
	tset_str = 'aaabbccccdffghkk'
	string_compress(tset_str)
