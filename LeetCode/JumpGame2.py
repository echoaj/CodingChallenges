# LeetCode HARD

# NEEDS MORE WORK


def jumpGame2(i):
    n = array[i]   # get item

    if i == len(array)-1:   # when reaching end
        return 0
    elif i > len(array)-1:  # when goes out of bounds
        return 100
    elif n >= len(array) - 1:
        return 1
    elif n == 0:            # when reaches a zero
        return 100


    total = 100
    for j in range(1, n+1): # branches
        result = jumpGame2(i+j) + 1
        total = min(total, result)

    return total





# array = [2, 3, 0, 1, 4]
# array = [1, 1, 1, 1]
array = [2, 1, 0, 0, 4]
# array = [1,2]
print(jumpGame2(0))





'''
def jumpGame2_Tab(array):
    length = len(array)
    table = [max(array)+1] * (max(array)+1)
    table[array[0]] = 0
    print(table)

    for cur in range(length-1):
        i = cur
        while i < min(cur+array[cur], length-1):
            i += 1
            if table[array[i]] == 0:
                table[array[i]] = table[array[cur]]+1
            elif array[i] == array[cur]:
                table[array[i]] += 1
            else:
                table[array[i]] = min(table[array[cur]]+1, table[array[i]])
            print(table)


    return table[array[-1]]

print(jumpGame2_Tab([1,2,0,1]))
'''
