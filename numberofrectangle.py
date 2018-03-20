#-*- coding:utf-8 -*-
import random
def NumbersOfRectangle(data, max_r, max_c, maxof1):
    numof1 = sum(list(map(lambda x: x.count(1), data)))

    if(len(data) > max_r or len(data[0]) > max_c or numof1 > maxof1):
        print("It is not valid input data!!")
        return
    table = []
    row = len(data)
    col = len(data[0])
    counter = 0

    for i in range(row):
        for j in range(col):
            if data[i][j] == 1:
                for k in range(j+1, col):
                    if data[i][k] == 1:
                        if(j, k) in table:
                            counter += 1
                        else:
                            table.append((j,k))
    print(table)
    return counter

if __name__ == "__main__":
    rows = int(input("Please input the array of rows you want:"))
    cols = int(input("Please input the array of colss you want:"))
    test_nums = [[random.randint(0,1) for i in range(cols)] for j in range(rows)]
    print("生成随机初始0-1矩阵-----")
    print(test_nums)
    res = NumbersOfRectangle(test_nums, 200, 200, 6000)
    print("The largest number of rectangle is:", res)