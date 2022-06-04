
# Add two numbers without using + or any arithmetic operators.


def add_recursion(a, b):
    if b == 0:
        return a
    else:
        return add_recursion(a ^ b, (a & b) << 1)


def add_iterative(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a


print(add_recursion(1, 2))
print(add_recursion(2, 2))
print(add_recursion(3, 2))
print(add_recursion(7, 5))

print(add_iterative(1, 2))
print(add_iterative(2, 2))
print(add_iterative(3, 2))
print(add_iterative(7, 5))

# 1 2
# 1 ^ 2       |  (1 & 2) << 1)
# 0001 ^ 0010 |  (0001 & 0010) << 1)
# 0011        |   0000 << 1
# 3           |   0
# return 3

# 7, 5
# 7 ^ 5, (7 & 5) << 1)
# 0111 ^ 0101 | (0111 & 0101) << 1)
# 0010        |  0101 << 1
# 2           |  1010
# 0010 ^ 1010 | (0010 & 1010) << 1)
# 1000        |  0010 << 1
# 8           |  0100
# 1000 ^ 0100 | (0000 & 0100) << 1)
# 1100        |  0000 << 1
# 12           |  0


