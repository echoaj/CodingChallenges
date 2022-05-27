# Constraints.  Numbers in array must be between 1 and the size of the array

# O(n) Time Complexity
# O(1) Space Complexity

# The idea is loop through the array and keep track of the index of the number
# If the number is negative, then it has been seen before
# If the number is positive, then it has not been seen before
# If the number is positive, then we want to make it negative
# return the index of the abs(number) that has been seen before
def firstDuplicateNumber(array):
    for i in range(len(array)):
        num = abs(array[i])
        if array[num - 1] < 0:
            return abs(array[num - 1])
        else:
            array[num - 1] *= -1

    return -1


array = [1, 4, 6, 3, 8, 6, 1, 5]
print(firstDuplicateNumber(array))
