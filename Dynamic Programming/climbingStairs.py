# LeetCode 746
# Easy


memo = {}
def climbingStairs(n):
    if n == 0:
        return 1
    if n < 0:
        return 0

    if n in memo:
        return memo[n]
    else:
        memo[n] = climbingStairs(n-1) + climbingStairs(n-2)
    return memo[n]


print(climbingStairs(3))