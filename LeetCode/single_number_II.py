# Leetcode 137. Single Number II
# Given an array of integers, every element appears three times except for one. Find that single one.
# Your algorithm should have a linear runtime complexity.
# Could you implement it without using extra memory?


def single_number2(nums):
    map = {}
    for num in nums:
        if num not in map:
            # First instance found
            map[num] = 1
        else:
            # Another instance found. Increase counter
            map[num] += 1

    for key in map:
        if map[key] == 1:
            return key
    return -1


#  [1, 1, 1, 2, 2, 2, 10]
#  [1, 2, 10] * 3 = [1, 1, 1, 2, 2, 2, 10, 10, 10]
#  sum3 = 39  <----  sum([1, 1, 1, 2, 2, 2, 10, 10, 10])
#  sum = 19  <----  sum([1, 1, 1, 2, 2, 2, 10])
#  sum3 - sum = 20
#  20 // 2 = 10
def single_number2_2(nums):
    total3 = sum(set(nums)) * 3
    total = sum(nums)
    return (total3 - total) // 2


print(single_number2([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 100, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]))
print(single_number2_2([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 100, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]))
