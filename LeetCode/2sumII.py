# Leetcode 167 Medium

"""
167. Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.
"""


def two_sum_ii(nums, target):
    # store the inverse
    l = 0
    r = len(nums) - 1

    while l < r:
        total = nums[l]+nums[r]
        if total > target:
            r -= 1
        elif total < target:
            l += 1
        else:
            return [l+1, r+1]

    return []


print(two_sum_ii([0, 2, 7, 8, 11, 15], 9))
