# - Programming Interviews Exposed.pdf

# Write a function that determines whether two integers
# are equal without using any comparison operators.


def is_equal(x, y):
    return not x ^ y


a = 8
b = 8

print(is_equal(a, b))
