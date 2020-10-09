# Check if two words are anagrams


def anagrams(string1, string2):
    return True if sorted(string1) == sorted(string2) else False


word1 = "race"
word2 = "care"

print(anagrams(word1, word2))

word3 = "dice"
word4 = "mars"
print(anagrams(word3, word4))
