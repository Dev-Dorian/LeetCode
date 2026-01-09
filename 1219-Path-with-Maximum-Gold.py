def getMaximumGold(grid):
    rows = len(grid)
    cols = len(grid[0])
    print(rows, cols)

    def dfs(r, c):
        if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == 0:
            return 0
        temp = grid[r][c]
        grid[r][c] = 0
        res = 0
        neighbors = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
        for r2, c2 in neighbors:
            res = max(res, temp + dfs(r2, c2))
        grid[r][c] = temp
        return res

    res = 0
    for r in range(rows):
        for c in range(cols):
            res = max(res, dfs(r, c))
    return res


grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
print(getMaximumGold(grid))
