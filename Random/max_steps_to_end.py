'''
array = [0,9,0,0,3,0,5,1,2,0,1,0]

You can hope how many times you want and your hops
do not have a limit.  Count the maximum steps it would
take to get to the end.  The numbers represent how much
you would move forward by.
'''

def max_steps(x):
    if x >= len(array):
        return 0
    num = array[x]
    result2 = max_steps(num+x+2)
    result1 = max_steps(num+x+1)
    total =  max(result1, result2) + 1
    return total

array = [0, 9, 0, 0, 3, 0, 5, 1, 2, 0, 1, 0]
answer = max_steps(0)

print(answer)

