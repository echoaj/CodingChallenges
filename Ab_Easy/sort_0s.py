
nums = [1,2,0,4,0,6,0,8,9]


def way_1():
    left = 0
    right = 0
    while right < len(nums):
        print(nums, (left, right))
        if nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1

    print(nums)


def way_2():
    index = 0
    for num in nums:
        print(nums)
        if num != 0:
            nums[index] = num
            index += 1
    print(nums)

    for i in range(index, len(nums)):
        nums[i] = 0
    print(nums)


way_2()


'''
lr
[1, 2, 0, 4, 0, 6, 0, 8, 9] (0, 0)
    lr
[1, 2, 0, 4, 0, 6, 0, 8, 9] (1, 1)
       lr
[1, 2, 0, 4, 0, 6, 0, 8, 9] (2, 2)
       l  r
[1, 2, 0, 4, 0, 6, 0, 8, 9] (2, 3)
          l  r
[1, 2, 4, 0, 0, 6, 0, 8, 9] (3, 4)
          l     r
[1, 2, 4, 0, 0, 6, 0, 8, 9] (3, 5)
             l     r
[1, 2, 4, 6, 0, 0, 0, 8, 9] (4, 6)
             l        r
[1, 2, 4, 6, 0, 0, 0, 8, 9] (4, 7)
                l        r
[1, 2, 4, 6, 8, 0, 0, 0, 9] (5, 8)
[1, 2, 4, 6, 8, 9, 0, 0, 0]

'''









# not good solution
# Space (n)
'''
new = []
for i in nums:
    if i != 0:
        new.append(i)

for j in range(nums.count(0)):
    new.append(0)

print(new)
'''
