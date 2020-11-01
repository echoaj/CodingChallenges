# Leetcode
# 860. Lemonade Change
# Easy
# Greedy Solution


def lemonadeChange(bills):
    ten = 0
    five = 0
    for i in bills:
        if i == 5:
            five += 1
        elif i == 10:
            ten += 1
            if five > 0:
                five -= 1
            else:
                return False
        elif i == 20:
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True




print(lemonadeChange([5,5,5,5,20,20,5,5,20,5]))