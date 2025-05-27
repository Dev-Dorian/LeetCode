def maxProfit(prices):
    minim = float('inf')
    maxGain = 0
    for price in prices:
        if price < minim:
            minim = price
        elif maxGain < price - minim:
            maxGain = price - minim
    return maxGain


def maxProfit1(prices):
    buy = prices[0]
    profit = 0
    for sell in prices:
        # print(sell)
        if sell < buy:
            buy = sell
            print(buy)
        else:
            profit = max(profit, sell-buy)
            # print(profit)
    return profit


prices = [7, 1, 5, 3, 6, 4]
# print(maxProfit(prices))
print(maxProfit1(prices))
