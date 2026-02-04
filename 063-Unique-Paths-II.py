def uniquePathsWithObstacles(obstacleGrid):
    M, N = len(obstacleGrid), len(obstacleGrid[0])
    dp = {(M - 1, N - 1): 1}

    def dfs(row, col):
        if row == M or col == N or obstacleGrid[row][col]:
            return 0
        if (row, col) in dp:
            return dp[(row, col)]
        dp[(row, col)] = dfs(row + 1, col) + dfs(row, col + 1)
        return dp[(row, col)]
    return dfs(0, 0)


def uniquePathsWithObstacles_1(obstacleGrid):
    M, N = len(obstacleGrid), len(obstacleGrid[0])
    dp = [0] * N
    dp[N-1] = 1

    for row in reversed(range(M)):
        for col in reversed(range(N)):
            if obstacleGrid[row][col]:
                dp[col] = 0
            elif col + 1 < N:
                dp[col] = dp[col] + dp[col + 1]
    return dp[0]


obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(uniquePathsWithObstacles(obstacleGrid))
print(uniquePathsWithObstacles_1(obstacleGrid))
