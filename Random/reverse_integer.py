''' leet code
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.'''

num = -2147483648
flag = 1
lst_num = list(str(num))

if lst_num[0] == '-':
    flag = -1
    lst_num.pop(0)

lst_num = lst_num[::-1]

num = int(''.join(lst_num))

if num >> 31 > 0:
    print(0)
else:
    print(num * flag)