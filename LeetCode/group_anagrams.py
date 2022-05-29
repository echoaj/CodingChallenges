# Leetcode Problem: https://leetcode.com/problems/group-anagrams/
# Medium 49
# Given an array of strings, group anagrams together.

# Example:
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

# Note:
# All inputs will be in lowercase.
# The order of your output does not matter.


def group_anagrams(strs):
    map_ = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word in map_:
            map_[sorted_word].append(word)
        else:
            map_[sorted_word] = [word]
    return list(map_.values())


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
