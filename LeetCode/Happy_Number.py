# Leetcode
# 202. Happy Number
# Easy



def isHappy(n: int) -> bool:
    mem = set()
    while n not in mem:
        mem.add(n)
        n = sum([int(i)**2 for i in str(n)])

    return n == 1

print(isHappy(19))