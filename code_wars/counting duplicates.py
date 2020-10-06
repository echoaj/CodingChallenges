#codewars.com

def duplicate_count(text):
    text = text.lower()
    text_list = list(text)
    text_list.sort()

    k = 1
    count = 0
    prev = ''
    for i in text_list:
        if k < len(text_list):
            if text_list[k] == i and not i == prev:
                count += 1
                prev = i
        k += 1
    return count


print(duplicate_count("helloWorld what is up bro"))


'''
def duplicate_counts(text):
    count = 0

    for c in set(text.lower()):
        if text.lower().count(c) > 1:
            count += 1
    return count

print(duplicate_counts("abccCcbbefg"))'''