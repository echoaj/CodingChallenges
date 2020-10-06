#codewars.com

#Simple, given a string of words, return the length of the shortest word(s).
#String will never be empty and you do not need to account for different data types.

def find_short(s):
    # your code here
    lst = s.split()
    l = 100
    for i in lst:
        if len(i) < l:
            l = len(i)
    return l

print(find_short("bitcoin take over the world maybe who knows perhaps"))


'''
def find_short(s):
    return min(len(x) for x in s.split())

print(find_short("bitcoin take over the world maybe who knows perhaps"))
'''