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


obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(uniquePathsWithObstacles(obstacleGrid))
