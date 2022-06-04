
# Total number of 1s in a number
# GeekForGeeks
# https://www.geeksforgeeks.org/count-number-of-1s-in-binary-representation-of-a-number/

"""
Example
Input: n = 13
Output: 6
Here, no <= 13 containing 1 are 1, 10, 11,
12, 13. So, total 1s are 6.

Input : n = 5
Output : 1
Here, no <= 13 containing 1 are 1.
So, total 1s are 1.
"""


def total_of_1s_in_a_num(n):
    count = 0
    i = 1
    while i <= n:
        divider = i * 10
        count += (int(n / divider) * i + min(max(n % divider - i + 1, 0), i))
        i *= 10

    return count


print(total_of_1s_in_a_num(13))
