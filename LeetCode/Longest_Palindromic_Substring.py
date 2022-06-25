# Leetcode 5
# Medium Longest Palindromic Substring

# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.

"""
Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
"""

# Solution:
# As you Iterate through the string, the current character you are at is the center of the palindrome.
# Expand outwards from the center to find the longest palindrome.


def longest_palindromic_substring(string):
    if not string:
        return ''

    count = 1
    left, right = 0, 0
    for m in range(len(string)):
        l, r = m - 1, m + 1
        while l >= 0 and r < len(string) and string[l] == string[r]:
            count = max(count, r - l + 1)
            left, right = l, r
            l, r = l - 1, r + 1

        l, r = m, m + 1
        while l >= 0 and r < len(string) and string[l] == string[r]:
            count = max(count, r - l + 1)
            left, right = l, r
            l, r = l - 1, r + 1

    return string[left:right+1]


print(longest_palindromic_substring("babad"))
print(longest_palindromic_substring("cbbd"))
print(longest_palindromic_substring("cbbde"))
print(longest_palindromic_substring("a"))
print(longest_palindromic_substring(""))