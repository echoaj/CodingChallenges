check = "racecar"

def isPalindrome1(check):
    if check == check[::-1]:
        print(True)
    else:
        print(False)


def isPalindrome2(check):
    end = len(check) - 1
    start = 0
    while start < round(len(check) / 2):
        if check[start] != check[end]:
            return False
        start += 1
        end -= 1
    return True


def isPalindrome3(check, start, end):
    if round(len(check) / 2) == start:
        return True
    elif check[start] != check[end]:
        return False
    else:
        return isPalindrome3(check, start + 1, end - 1)

isPalindrome1(check)
print(isPalindrome2(check))
print(isPalindrome3(check, 0, len(check)-1))