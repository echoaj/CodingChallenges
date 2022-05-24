# codewars.com

def unique_in_order(iterable):
    l = []
    if not iterable == '':
        l.append(iterable[0])
        for i in iterable:
            if not l[-1] == i:
                l.append(i)
    return l


unique_in_order2 = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]

num = unique_in_order('AAAABBBCCDAABBB')
print(num)

num = unique_in_order2('AAAABBBCCDAABBB')
print(num)