#codewars.com


#[9,8,8,False,434,0,0]
'''
array = [0,False,0.0,9]

i = 0
size = len(array)
while i < size:
    if array[i] is 0 or array[i] is 0.0:
        del array[i]
        array.append(0)
        size = len(array)
    i += 1
print(array)
'''

def move_zeros(array):
    i = 0
    size = len(array)
    while i < size:
        if array[i] == 0 or array[i] == 0.0:
            del array[i]
            array.append(0)
            size = len(array)
        i += 1
    return(array)


print(move_zeros([0,False,0.0,9]))