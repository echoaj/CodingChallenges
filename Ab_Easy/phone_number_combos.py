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

# base case when reaching end of 324.
# pass i to function increase till index is 0
# returns 4 from map -> [g, h, i]
# [g, h, i] + [d, e, f] = [gd, ge, gf, hd, he, hf, id, ie, if]
# [gd, ge, gf, hd, he, hf, id, ie, if] + [a, b, c]


def letter_combos(i):
    if i == len(digits) - 1:
        return map[digits[i]]

    combos = letter_combos(i+1)
    perm = []

    for letter1 in combos:
        for letter2 in map[digits[i]]:
            pair = letter2 + letter1
            perm.append(pair)

    return perm


print(letter_combos(0))
