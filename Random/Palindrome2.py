# check if a string is palindrome
# other wise see if string can be rearranged so that it can be a plindrome


def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


def can_be_palindrome(word):
    odd = False
    for i in word:
        num = word.count(i)
        if num % 2 == 1:
            if not odd:
                odd = True
            else:
                return False
                exit(0)
    return True


word = "racecar"
is_palindrome(word)
print(can_be_palindrome(word))