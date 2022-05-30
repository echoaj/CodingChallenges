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


def longest_palindromic_substring(s):

    if len(s) == 0:
        return ""
    count = 0
    left = right =0
    for m in range(len(s)):
        l = r = m
        while l >= 0 and r < len(s) and s[l] == s[r]:
            length = r - l + 1
            if length > count:
                left, right = l, r
                count = length
            l, r = l-1, r+1

        l = r = m
        r += 1
        # Same exact code as above, but with the right pointer being incremented by 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            length = r - l + 1
            if length > count:
                left, right = l, r
                count = length
            l, r = l-1, r+1
    return s[left:right+1]


print(longest_palindromic_substring("babad"))
print(longest_palindromic_substring("cbbd"))
print(longest_palindromic_substring("cbbde"))
print(longest_palindromic_substring("a"))
print(longest_palindromic_substring(""))