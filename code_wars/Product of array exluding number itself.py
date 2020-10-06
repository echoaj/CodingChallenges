#google interview question

'''
given an array of numbers, replace each number with the product of
all the numbers in the array except the number itself without using division.
'''

array = [5,4,2,9,7,13,8,2,100]          #52416000


i = 0
len = len2= len(array)
array_product = []

while i < len:
    product = 1
    for j in range(1, len2):
        product = product * array[j]
    array.append(array[i])
    array.remove(array[i])
    array_product.append(product)
    len = len - 1
    print(array_product)

