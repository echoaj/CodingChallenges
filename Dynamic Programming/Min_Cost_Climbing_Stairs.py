# LeetCode
# 746. Min Cost Climbing Stairs
# easy

def minCostClimbingStairs(cost, i):
    if i > len(cost) - 1:
        return 0

    if i in memo:
        return memo[i]
    else:
        memo[i] = cost[i] + min(minCostClimbingStairs(cost, i+1), minCostClimbingStairs(cost, i+2))
    return memo[i]


memo = {}
print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 0))