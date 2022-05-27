# LeetCode
# Easy
# 136 single number

"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Time O(n)
Space O(1)
"""


def singleNumber(nums):
    total = 0
    for i in nums:
        total ^= i      # XOR
    return total


print(singleNumber([4, 1, 2, 1, 2]))

# Identical numbers with XOR cancel out and become 0.
# 0100
# 0001
# 0010
# 0001
# 0010
# --------XOR--------
# 0000

