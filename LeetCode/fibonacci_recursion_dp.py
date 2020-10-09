memo = [None,None,None,None,None]

def fib(n):
    print(memo)
    if n == 1:      # base case 1
        return 1
    elif n == 0:    # base case 2
        return 0
    elif memo[n] is None:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

fib(4)
print(memo)