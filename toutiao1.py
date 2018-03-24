#-*- coding:utf-8 -*-

def diff_of_element_list(nums, k):
    newist = [i+k for i in nums]
    return len(set(nums) & set(newist))

if __name__ == "__main__":
    m, k = input("请输入数组长度和差值：").split()
    nums = input("请输入数组元素：").split()
    nums = [int(i) for i in nums]

    n = diff_of_element_list(nums, int(k))
    print("满足差值为%d的数对数目为：%d" % (int(k), n))


