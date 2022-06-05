# Leetcode 96 - Unique Binary Search Trees
# https://leetcode.com/problems/unique-binary-search-trees/


"""
Given an integer n, return the number of structurally unique BST's (binary search trees)
which has exactly n nodes of unique values from 1 to n.

Example 1:

    1         1           2             3       3
     \         \         / \           /       /
     3          2       1   3         2       1
    /            \                   /         \
    2            3                  1           2

Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1
"""


def unique_binary_search_trees(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    # dp -> [1, 1, 2, 0, 0, 0, 0, 0, 0, 0 ...]
    for i in range(3, n + 1):               # up to n
        print(dp)
        for j in range(1, i + 1):           # 1 to i
            dp[i] += dp[j - 1] * dp[i - j]  #
            print("\t", dp, "\t", j, f"dp[i] = {dp[j - 1]} * {dp[i - j]} -> {dp[j - 1] * dp[i - j]}")
    return dp[n]


print(unique_binary_search_trees(5))

# for x in range(0, 100):
#     print(x, unique_binary_search_trees(x))

# print(unique_binary_search_trees(1000))


