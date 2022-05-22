'''
Leetcode
17. Letter Combinations of a Phone Number
medium
100% Correct
'''


map = {'0': [''],
       '1': [''],
       '2': ['a', 'b', 'c'],
       '3': ['d', 'e', 'f'],
       '4': ['g', 'h', 'i'],
       '5': ['j', 'k', 'l'],
       '6': ['m', 'n', 'o'],
       '7': ['p', 'q', 'r', 's'],
       '8': ['t', 'u', 'v'],
       '9': ['w', 'x', 'y', 'z']}

digits = "324"


def phone(i=0):
    if digits == "":
        return []
    if i == len(digits)-1:
        return map[digits[i]]

    chars = phone(i+1)
    perm = []
    stop = len(chars)

    for a in map[digits[i]]:
        j = 0
        while j < stop:
            b = chars[j]
            perm.append(a+b)
            j += 1
    return perm


print(phone())
