def islandPerimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    visit = set()

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return 1

        if (r, c) in visit:
            return 0

        visit.add((r, c))
        perimeter = 0

        perimeter += dfs(r + 1, c) + dfs(r - 1, c) + \
            dfs(r, c + 1) + dfs(r, c - 1)

        return perimeter

    for r in range(rows):
        for c in range(cols):
            if grid[r][c]:
                return dfs(r, c)


def islandPerimeter_1(grid):
    r, c, perimeter = len(grid), len(grid[0]), 0
    for i in range(r):
        for j in range(c):
            if grid[i][j]:
                perimeter += 4
                if i and grid[i-1][j]:
                    perimeter -= 2
                if j and grid[i][j-1]:
                    perimeter -= 2
    return perimeter


grid = [[0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]]
print(islandPerimeter(grid))
print(islandPerimeter_1(grid))
