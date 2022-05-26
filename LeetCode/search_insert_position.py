# Leetcode 35. Search Insert Position
# Easy

# Given a sorted array of distinct integers and a target value,
# return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

"""
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
"""


def set_insert(nums, target):
    if nums[-1] < target:
        return len(nums)
    i = 0
    while nums[i] < target and i < len(nums)-1:
        i += 1
    return i


print(set_insert([1, 3, 5, 6], 4))
