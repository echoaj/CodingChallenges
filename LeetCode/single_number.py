# LeetCode
# Easy
# 136 single number

# Time O(n)
# Space O(1)
def singleNumber(nums):
    total = 0
    for i in nums:
        total ^= i
    return total


print(singleNumber([4,1,2,1,2]))

# 0100
# 0001
# 0010
# 0001
# 0010