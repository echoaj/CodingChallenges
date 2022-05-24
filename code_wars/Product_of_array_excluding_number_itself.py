from functools import reduce


'''
Google Interview Question
given an array of numbers, replace each number with the product of
all the numbers in the array except the number itself without using division.
'''

array = [5, 4, 2, 9, 7, 13, 8, 2, 100]

total = reduce(lambda x, y: x*y, array)

for i in range(len(array)):
    array[i] = total // array[i]

print(array)
