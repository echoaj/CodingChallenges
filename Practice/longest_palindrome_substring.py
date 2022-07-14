
# longest palindrome substring


def longest_palindrome_substring(string):
    if not string:
        return ''

    count = 1
    for m in range(len(string)):
        l, r = m-1, m+1
        while l >= 0 and r < len(string) and string[l] == string[r]:
            count = max(count, r - l + 1)
            l, r = l-1, r+1

        l, r = m, m+1
        while l >= 0 and r < len(string) and string[l] == string[r]:
            count = max(count, r - l + 1)
            l, r = l-1, r+1

    return count


if __name__ == '__main__':
    print(longest_palindrome_substring('abcd'))
    print(longest_palindrome_substring('abcddcabcd'))
    print(longest_palindrome_substring('abcdaabcdbcd'))

