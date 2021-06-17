

'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
'''

# O(n) time
# O(1) space
def bestTimetoBuyandSellStock(prices):
    buy = 0
    sell = 1
    profit = 0

    while sell < len(prices):
        if prices[buy] < prices[sell]:
            profit = max(profit, prices[sell] - prices[buy])
        else:
            buy = sell
        sell += 1
    return profit


print(bestTimetoBuyandSellStock([7,1,5,3,6,4]))


# Noah's solution
# Issue of [7,1] returns 5
def stock():
    array = [7,1,5,3,6,4]
    profit = 0
    lowest = array[0]
    for i in array:
        lowest = min(i, lowest)
        profit = max(i-lowest, profit)
    return profit


print(stock())
