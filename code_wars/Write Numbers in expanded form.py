#codewars.com

import math


def expanded_form(num):
    num = str(num)
    quantity = len(num) - 1
    digits = []
    for i in num:
        if i == '0':
            quantity -= 1
        if quantity >= 0 and i != '0':
            digits.append(i + '0' * quantity)
            quantity -= 1
    return " + ".join(digits)


print(expanded_form(2745))