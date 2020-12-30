
'''

Given an odd number, find the minimum divisions to 0

Steps:
subtract
divide 3
divide 5

If result is odd keep going
If result is even multiply by 31 then keep going

'''


def max_num(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n * 31

    r1 = max_num(n//2) + 1
    r2 = max_num(n//3) + 1
    r3 = max_num(n//5) + 1
    return min(r1,r2,r3)



print(max_num(100))