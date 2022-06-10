
# Medium (322)
'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the
fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
'''

'''
My solution 2
total = 1000
def coinchange(coins, amount):
    global total
    if amount < 0:
        return -1
    if amount == 0:
        return 1
    for i in coins:
        total = min(total, coinchange(coins, amount-i))

    return total
'''


'''
My solution
def coinchange2(coins, amount):
    table = [-1]*(MAX)

    spots = [0]
    table[0] = 0

    for k in range(amount):
        i = spots.pop(0)
        for j in coins:
            next = i + j
            if next <= amount:
                if table[next] == -1:
                    table[next] = table[i] + 1
                else:
                    table[next] = min(table[next], table[i]+1)
            if next not in spots:
                spots.append(next)

    print(table)
    return table[-1]
'''


# Correct Solution
def coin_change(coins, target):
    max_ = target + 1            # one more than target
    table = [max_] * max_
    table[0] = 0

    for i in range(1, max_):
        for coin in coins:
            if coin <= i:       # Anything greater than i goes past target
                table[i] = min(table[i], 1+table[i-coin])

    return table[target] if table[target] != max_ else -1


print(coin_change([1, 3, 4, 5], 7))


'''
[186,419,83,408]
6249
'''