def removeDuplicates(nums):
    if len(nums) <= 1:
        return len(nums)
    slow = 0
    for i in range(1, len(nums)):
         if nums[i] != nums[slow]:
            slow += 1
            nums[slow] = nums[i]
    return slow + 1

if __name__ == "__main__":

    test_num = [1, 1, 2, 3, 3, 5]
    res = removeDuplicates(test_num)
    print(res, test_num)

