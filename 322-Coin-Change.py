def coinChange(coins, amount):
    # dp = [amount + 1] * (amount + 1)
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for index in range(1, amount + 1):
        for coin in coins:
            if index - coin >= 0:
                print(f"{index, coin} = {index - coin}")
                dp[index] = min(dp[index], 1 + dp[index-coin])
                print(dp[index], 1 + dp[index-coin])
    # return dp[amount] if dp[amount] != amount + 1 else -1
    return dp[amount] if dp[amount] != float("inf") else -1


coins = [1, 2, 5]
amount = 11

print(coinChange(coins, amount))
