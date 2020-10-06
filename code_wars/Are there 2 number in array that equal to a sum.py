
array = [1,4,9,0,4,6] #sum = 14
array2= [1,2,6,2,8,7]
array3 = [4,-3,54,-4,6,10,34-5,6,2,-6,4,29,-7,0,4,23,-83,-3]
array4 = [-2,-4,-9,-3,-10]

def findMatchingSum(a):
    dict = {}
    for i in a:
        if dict.get(i):
            return True
        else:
            dict[14-i] = True
    return False

print(findMatchingSum(array))
print(findMatchingSum(array2))
print(findMatchingSum(array3))
print(findMatchingSum(array4))