def maxProfit(prices):
    maxProfit = 0
    for index in range(1, len(prices)):
        if prices[index - 1] < prices[index]:
            maxProfit += prices[index] - prices[index - 1]
    return maxProfit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
