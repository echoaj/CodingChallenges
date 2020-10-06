# Given an array of numbers, replace each number with the product of
# all the numbers in the array except the number itself *without* using division.
from functools import reduce

def array_product(arr):
    copy = arr.copy()
    for i in range(len(arr)):
        removed = copy[i]
        copy.remove(removed)
        num = reduce(lambda x,y: x*y, copy)
        copy.insert(i,removed)
        arr[i] = num

    print(arr)

array_product([1,4,5,2,3])