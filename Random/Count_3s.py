'''
Given a positive number, count the number of 3s in that digit
then floor divide it by 3 and continue the count until
0 is reached.

100             (0)
100 // 3 = 33   (2)
33 // 3 = 10    (0)
10 // 3 = 3     (1)
3 // 3 = 1      (0)
1 // 3 = 0      (0)
0+2+0+1+0+0 = 3

672             (0)
672 // 3 = 224  (0)
224 // 3 = 74   (0)
74 // 3 = 24    (0)
24 // 3 = 8     (0)
8 // 3 = 2      (0)
2 // 3 = 0      (0)
0+0+0+0+0+0+0 = 0

389             (1)
389 // 3 = 129  (0)
129 // 3 = 43   (1)
43 // 3 = 14    (0)
14 // 3 = 4     (0)
4 // 3 = 1      (0)
1 // 3 = 0      (0)
1+0+1+0+0+0+0 = 2
'''


def count3s(n):
    if n == 0:
        return 0

    threes = str(n).count('3')
    return count3s(n//3) + threes


print(count3s(100))
