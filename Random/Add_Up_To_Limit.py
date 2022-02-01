

def add_to_limit(limit, num1, num2, total):
    # base case
    if total == limit:
        return True
    elif total > limit:
        return False

    result1 = add_to_limit(limit, num1, num2, total+num1)
    result2 = add_to_limit(limit, num1, num2, total+num2)

    return result1 or result2


print(add_to_limit(11, 2, 3, 0))
