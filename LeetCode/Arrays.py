'''
Remove Duplicates from sorted Array
'''

def remove_duplicates(nums):
    nums = list(set(nums))
    print(nums)


#remove_duplicates([1,1,1,1,2,2,3,4,5,5,6,6,6,7,8,8])





'''
Rotate an array k times to the right when k is positive
Rotate it to the left when k is negative
'''
def rotate_array(k, nums):
    length = len(nums) - 1

    if k >= 0:
        for i in range(k):
            temp = nums[length]
            nums.pop()
            nums.insert(0, temp)
    else:
        for i in range(0, k, -1):
            temp = nums[0]
            nums.pop(0)
            nums.append(temp)

    print(nums)


#rotate_array(-3, [1,2,3,4,5,6,7])





'''
Given a non empty array of integers, each element appears twice
exept for one.  Find that one.
'''
def find_single_number(nums):
    for i in nums:
        if nums.count(i) == 1:
            print(i)
            break

#find_single_number([2,5,2,5,3,6,3,9,6,8,8])





'''
Given two lists, find their intersection.  No Duplicates
'''

def intersection2(arr1, arr2):
    print(list(set(arr1).intersection(set(arr2))))

#intersection2([1,2,3,4,4,5,6], [0,3,4,4,5,7])




'''
Given two lists, find their intersection.  Duplicates should be shown.
'''
def intersection2(arr1, arr2):
    new = []
    for i in arr1:
        if i not in new:
            count1 = arr1.count(i)
            count2 = arr2.count(i)
            default = count1 if count1 < count2 else count2
            for j in range(default):
                new.append(i)
    print(new)


#intersection2([0,3,4,4,5,7], [4,4,4,4,4])





'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, 
and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
EXAMPLE:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
'''

def add_one(num):
    number = int("".join(map(str, num))) + 1
    num = list(map(int, str(number)))
    print(num)



#add_one([4,3,2,1])



'''
Given an array nums, write a function to move all 0's to the end of it while 
maintaining the relative order of the non-zero elements.
EXAMPLE
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

def move_zeros(arr):
    for i in arr:
        if i == 0:
            arr.remove(0)
            arr.append(0)
    print(arr)


#move_zeros([0,1,0,3,12])



'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
EXAMPLE:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

def two_sums(arr, target):
    current = 0
    difference = 0
    for i in arr:
        difference = target - i
        if difference in arr and difference != i:
            current = i
            break

    print([arr.index(current), arr.index(difference)])
    
    
two_sums([2, 7, 11, 15], 9)



'''
Rotate a 2 dimensional list.
'''
def rotate_matrix(matrix, degrees):
    deg = int(degrees/90)
    for i in range(deg):
        new = []
        length = len(matrix)
        for i in range(length):
            new.append([])
            for row in matrix:
                new[i].insert(0,row[i])

        matrix = new
    print(matrix)



two_D = [[1, 2, 3, 4],
         [1, 2, 3, 4],
         [1, 2, 3, 4],
         [1, 2, 3, 4]]

rotate_matrix(two_D, 90)


