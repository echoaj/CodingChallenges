# LeetCode
# easy
# Use bit manipulation to check if a number is a power of two
# Example
# 16 is true
# 17 is false


def is_power_of_two(n):
    return False if n == 0 else not n & n-1


print(is_power_of_two(16))
