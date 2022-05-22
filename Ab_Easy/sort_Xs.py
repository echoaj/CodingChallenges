# Move all Xs to the end of the array without changing the order of the remaining elements

array = ['X', 'B', 'C', 'X', 'X', 'D', 'E', 'X', 'F', 'G']    # RESULT -> ABCDEFGXXX

# 1) create two pointer variables pointing to first element
# 2) move first pointer forward till X is found
# 3) move second pointer to that position
# 4) bubble X to the end of array
# 5) return first pointer to location of second pointer

x_count = array.count("X")

j = 0
while j < len(array) and j < len(array) - x_count:
    num = array[j]
    if num == "X":
        i = j
        while i+1 < len(array):
            array[i], array[i+1] = array[i+1], array[i]
            print(array)
            i += 1
        j -= 1
    j += 1

print(array)


# O(n * k)




















# xs = array.count("X")
# print(xs)
#
# new_array = []
# for i in array:
#     if i != "X":
#         new_array.append(i)
#
# for i in range(xs):
#     new_array.append("X")
# print(new_array)