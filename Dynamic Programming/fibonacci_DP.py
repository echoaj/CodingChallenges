
memo = {}


def fib(n):
    if n == 1:      # base case 1
        return 1
    elif n == 0:
        return 0    # base case 2
    elif n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]


print(fib(4))