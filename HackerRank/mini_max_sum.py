# HackerRank: Mini-max-sum
# https://www.hackerrank.com/challenges/mini-max-sum/problem

"""
Given five positive integers, find the minimum and maximum values that can be calculated by
summing exactly four of the five integers. Then print the respective minimum and maximum
values as a single line of two space-separated long integers.
"""

# Example:
# arr = [1, 3, 5, 7, 9]
# Output:
# 1  9
# Explanation: The minimum sum is 1 + 3 + 5 + 7 = 16 and the maximum sum is 9 + 5 + 7 = 24.


def mini_max_sum(arr):
    smallest = min(arr)
    largest = max(arr)
    total = sum(arr)
    print(total - largest, total - smallest)


arr = [1, 3, 5, 7, 9]
mini_max_sum(arr)
