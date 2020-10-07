'''
Given an integer n, return the minimum steps to 1

AVAILABLE STEPS:
    * Decrement by 1
    * if n is divisible by 2, divide by 2
    * if n is divisible by 3, divide by 3

10 -> 9 -> 3 -> 1
( 3 steps)

15 -> 5 -> 4 -> 2 -> 1
( 4 steps)

6 -> 2 -> 1
( 2 step)
'''

# Noah's Solution
def nsteps(n):
    if n == 1:      # Base Cse
        return 0

    if n % 3 == 0 and n % 2 == 0:
        return min(nsteps(n/3), nsteps(n/2), nsteps(n-1)) + 1
    elif n % 3 == 0:
        return min(nsteps(n/3), nsteps(n-1)) + 1
    elif n % 2 == 0:
        return min(nsteps(n/2), nsteps(n-1)) + 1
    else:
        return nsteps(n-1) + 1


# My Solution
# WITHOUT DP
def steps(n):
    if n == 1:      # Base Cse
        return 0

    if n % 3 == 0:
        return min(steps(n/3), steps(n-1)) + 1
    elif n % 2 == 0:
        return min(steps(n/2), steps(n-1)) + 1
    else:
        return steps(n-1) + 1


# WITH DP MEMORIZATION
memo = {}
def stepsDP(n):
    if n == 1:      # Base Cse
        return 0

    if n not in memo:
        if n % 3 == 0:
            memo[n] = min(stepsDP(n/3), stepsDP(n-1)) + 1
            return memo[n]
        elif n % 2 == 0:
            memo[n] = min(stepsDP(n/2), stepsDP(n-1)) + 1
            return memo[n]
        else:
            memo[n] = stepsDP(n-1) + 1
            return memo[n]
    else:
        return memo[n]


# WITH DP TABULATION
def stepsTB(n):
    table = [n]*(n+1)
    table[1] = 0      # Base Cse
    for i in range(1,n):
        table[i+1] = min(table[i+1], table[i]+1)
        if i*2 <= n:
            table[i*2] = min(table[i*2], table[i]+1)
        if i*3 <= n:
            table[i*3] = min(table[i*3], table[i]+1)
    return table[n]


num = 100
print(f"Recursion: {num} ->\t", steps(num))
print(f"Memorization: {num} ->\t", stepsDP(num))
print(f"Tabulation: {num} ->\t", stepsTB(num))
print(f"Noah's Solution: {num} ->\t", nsteps(num))