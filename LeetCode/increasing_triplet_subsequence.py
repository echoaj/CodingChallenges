# leetcode 334 Increasing Triplet Subsequence
# https://leetcode.com/problems/increasing-triplet-subsequence/description/
# Given an integer array nums, return true if there exists a triple of indices (i, j, k)
# such that i < j < k and nums[i] < nums[j] < nums[k].
# If no such indices exists, return false.

"""
Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
"""


def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) < 3:
        return False
    first = nums[0]
    second = float('inf')   # set second to infinity
    for num in nums:
        if num <= first:
            first = num     # reset first
        elif num <= second:
            second = num
        else:
            return True
    return False


print(increasingTriplet([1, 2, 3, 4, 5]))
print(increasingTriplet([5, 4, 3, 2, 1]))
print(increasingTriplet([2, 1, 5, 0, 7, 8]))
