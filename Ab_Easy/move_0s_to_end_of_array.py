# Move 0s to the end of the array
# All other numbers remain the same

# BEST: O(n * k)
# BEST: O(n)
def sort_0s(array):
    l = r = 0
    while r < len(array):
        if array[r] == 0:
            r += 1
        else:
            array[l], array[r] = array[r], array[l]
            r, l = r+1, l+1


nums = [1, 2, 0, 4, 0, 0, 7, 0, 9]
#       ^^

sort_0s(nums)
print(nums)
