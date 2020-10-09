
# Time Complexity
# n * (1 + k + k + 1 + 1) + n + 1   -->  O(n * k)


def group_anagrams(strings):
    map = dict()
    tracker = []

    for string in strings:              #O(n)
        numbers = ['0' for i in range(25)]  # O(1)
        for i in string:                #O(k)
            num = ord(i)-97
            numbers[num] = '1'

        result = ''.join(numbers)
        if result not in map:
            map[result] = [string]      #O(1)
        else:
            map[result].append(string)  #O(1)

    #print(map)
    for key in map:
        tracker.append(map[key])

    return tracker


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# WRONG
print(group_anagrams(["gggd", "dddg", "tan", "ate", "nat", "bat"]))