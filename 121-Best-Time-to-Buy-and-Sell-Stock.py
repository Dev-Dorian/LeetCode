def maxProfit(prices):
    minim = float('inf')
    maxGain = 0
    for price in prices:
        if price < minim:
            minim = price
        elif maxGain < price - minim:
            maxGain = price - minim
    return maxGain


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
