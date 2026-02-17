def uniquePaths(m, n):
    dp = [1] * n
    for row in range(1, m):
        for col in range(1, n):
            dp[col] = dp[col] + dp[col - 1]
    return dp[-1]


m = 3
n = 7
print(uniquePaths(m, n))
