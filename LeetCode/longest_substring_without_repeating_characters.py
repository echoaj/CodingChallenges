
# Leetcode #3 Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.

"""
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def longest_substring_without_repeating_characters(s):
    if s == "":
        return 0
    # sliding window technique
    count = 0
    track = set()
    l = 0
    for r in range(len(s)):     # move right pointer
        # check if current character is in track
        # if so move left pointer forward and pop what the left pointer is pointing at off set
        while s[r] in track:
            track.remove(s[l])
            l += 1
        track.add(s[r])
        count = max(count, len(track))
    return count


print(longest_substring_without_repeating_characters("abcabcbb"))
print(longest_substring_without_repeating_characters("bbbbb"))
print(longest_substring_without_repeating_characters("pwwkew"))
print(longest_substring_without_repeating_characters(" "))


