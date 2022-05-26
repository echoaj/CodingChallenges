# Leetcode 349. Intersection of Two Arrays
# Easy

# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.

"""
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
"""


def intsersection(nums1, nums2):
    return list(set(nums1).intersection(nums2))


print(intsersection([1, 2, 2, 1], [2, 2]))


# solution 2
def inserction2(nums1, nums2):
    hash_map = {}
    result = []

    for num in nums2:
        hash_map[num] = 1

    for num in nums1:
        if hash_map.get(num) == None:
            continue
        else:
            if num not in result:
                result.append(num)

    return result