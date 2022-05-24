# codewars.com

# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty, and you do not need to account for different data types.

def find_short(s):
    # your code here
    words = s.split()
    length = len(words[0])
    for word in words:
        length = min(length, len(word))
    return length


print(find_short("bitcoin take over the world maybe who knows perhaps"))

'''
def find_short(s):
    return min(len(x) for x in s.split())

print(find_short("bitcoin take over the world maybe who knows perhaps"))
'''
