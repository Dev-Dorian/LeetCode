def islandPerimeter(grid):
    rows = len(grid)
    cols = len(grid[0])

    def dfs(r, c):

    for r in range(rows):
        for c in range(cols):
            if grid[r][c]:
                return dfs(r, c)


grid = [[0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]]
print(islandPerimeter(grid))
