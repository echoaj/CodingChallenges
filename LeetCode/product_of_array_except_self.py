# Medium (238)

'''

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

'''


def productExceptSelf(nums):
    length = len(nums)
    output = [1] * length

    for i in range(length-1):
        output[i+1] = output[i] * nums[i]

    var = 1
    for i in range(length-1, 0, -1):
        var *= nums[i]
        output[i-1] *= var

    return output

print(productExceptSelf([1,2,3,4]))


