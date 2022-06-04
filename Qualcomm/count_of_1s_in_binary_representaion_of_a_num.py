

def total_of_1s_in_a_num(n):
    count = 0
    while n:
        count = count + 1
        n = n & (n - 1)
    return count


print(total_of_1s_in_a_num(13))
