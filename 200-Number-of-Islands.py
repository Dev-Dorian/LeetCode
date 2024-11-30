
def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "1":
                count += 1
                dfs(grid, i, j)
        return count


def dfs(grid, row, col):
    if grid[row][col] == "0":
        return
    grid[row][col] = "0"

    if row > 0:
        dfs(grid, row - 1, col)
    if row < len(grid) - 1:
        dfs(grid, row + 1, col)
    if col > 0:
        dfs(grid, row, col - 1)
    if col < len(grid[row]) - 1:
        dfs(grid, row, col + 1)


grid = [["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]]
print(numIslands(grid))
