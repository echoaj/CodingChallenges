# Leetcode 219. Contains Duplicate II

"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""


def containsNearbyDuplicate(nums, k):
    dist = k + 1
    map = {}

    for i in range(len(nums)):
        digit = nums[i]
        if digit in map:
            dist = min(dist, abs(i - map[digit]))

        map[digit] = i

    return True if dist <= k else False


print(containsNearbyDuplicate([1,0,1,1], 1))