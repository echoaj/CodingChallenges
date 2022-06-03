

# Find two missing numbers in an array of size n using XOR
# https://www.geeksforgeeks.org/find-two-missing-numbers-in-an-array-of-size-n-using-xor/
# Given an array of size n-2 containing n-2 numbers
# Find two missing numbers in it using XOR

"""
Examples:

Input  : arr[] = {1, 3, 5, 6}, n = 6
Output : 2 4

Input : arr[] = {1, 2, 4}, n = 5
Output : 3 5

Input : arr[] = {1, 2}, n = 4
Output : 3 4
"""

# XOR will cancel out the same elements

# 0101
# 0110 XOR
# ---------
# 0011


def find_two_missing_numbers_XOR(arr, n):
    # Get the XOR of all
    # elements in arr[] and
    # {1, 2 .. n}
    XOR = arr[0]
    for i in range(1, n - 2):
        XOR ^= arr[i]
    for i in range(1, n + 1):
        XOR ^= i

    # Now XOR has XOR of two
    # missing elements. Any set
    # bit in it must be set in
    # one missing and unset in
    # other missing number

    # Get a set bit of XOR
    # (We get the rightmost set bit)
    set_bit_no = XOR & ~(XOR - 1)

    # Now divide elements in two sets
    # by comparing rightmost
    # set bit of XOR with bit at same
    # position in each element.
    x = 0

    # Initialize missing numbers
    y = 0
    for i in range(0, n - 2):
        if arr[i] & set_bit_no:

            # XOR of first set in arr[]
            x = x ^ arr[i]
        else:

            # XOR of second set in arr[]
            y = y ^ arr[i]
    for i in range(1, n + 1):
        if i & set_bit_no:

            # XOR of first set in arr[] and
            # {1, 2, ...n }
            x = x ^ i

        else:

            # XOR of second set in arr[] and
            # {1, 2, ...n }
            y = y ^ i

    return "Two Missing Numbers are\n%d %d" % (x, y)


print(find_two_missing_numbers_XOR([1, 3, 5, 6], 6))
