

nums = [1, 2, 9, 4, 9, 9, 7, 8, 9]

# same array
# O(n * k)
nines = nums.count(9)
for i in range(nines):
    nums.remove(9)
for i in range(nines):
    nums.append(9)
print(nums)


nums = [1, 2, 9, 4, 9, 9, 7, 8, 9]
left = 0
for right in range(len(nums)):
    if nums[right] != 9:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1

print(nums)