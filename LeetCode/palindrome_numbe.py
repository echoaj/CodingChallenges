# Leetcode 9 easy
# https://leetcode.com/problems/palindrome-number/


# Determine whether an integer is a palindrome.
# An integer is a palindrome when it reads the same backward as forward.

"""
Example 1:
Input: 121
Output: true
"""


def get_dividor(num):
    div = 1
    while num >= 10:
        num //= 10
        div *= 10
    return div


def palindrome_num(num):
    if num < 0:
        return False
    if num < 10:
        return True

    div = get_dividor(num)              # 1) get the number of digits

    while num > 0:
        r_num = num % 10                # 2) get the last digit
        l_num = num // div              # 3) get the first digit
        if r_num != l_num:              # 4) compare the first and last digit
            return False                # 5) if not equal, return False
        num = num % div // 10           # 6) remove the first and last digit
        div //= 100                     # 7) remove the first and last digit
    return True


print(palindrome_num(10000021))
