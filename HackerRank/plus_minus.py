# HackeRank plus minus challenge

"""
Given an array of integers, calculate the ratios of its elements that are positive,
negative, and zero. Print the decimal value of each fraction on a new line with
places after the decimal.

Note: This challenge introduces precision problems.
The test cases are scaled to six decimal places,
though answers with absolute error of up to 10^-4 are acceptable.

Example:
arr = [1, 1, 0, -1, -1]
There are n=5 elements, two positive, two negative and one zero.
Their ratios are 2/5(0.400000), 2/5(0.400000) and 1/5(0.200000). Results are printed as:

0.400000
0.400000
0.200000
"""


def plus_minus(arr):
    pos = neg = zer = 0
    for i in arr:
        pos += 1 if i > 0 else 0
        neg += 1 if i < 0 else 0
        zer += 1 if i ==0 else 0
    print(round(pos / len(arr), 6))
    print(round(neg / len(arr), 6))
    print(round(zer / len(arr), 6))


plus_minus([1, 1, 0, -1, -1])
