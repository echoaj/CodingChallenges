
# Given a number greater than 0, can you floor
# divide it by the sum of its digit and reach 1 or less?

# 15 // (1+5) = 6
# 6 // 6 = 1
# True

# 50 // (5+0) = 10
# 10 // (1+0) = 10
# False

# 484 // (4+8+4) = 30
# 30 // (3+0) = 10
# 10 // (1+0) = 10
# False


def reach_one(n):
    if n == 1:
        return True
    divisor = sum(int(i) for i in str(n))
    if divisor == 1:
        return False
    return reach_one(n // divisor)


print(reach_one(15))

