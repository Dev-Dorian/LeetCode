from collections import deque


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
                bfs(grid, i, j)
        return count

# Depth-First Search  DFS


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

# Breadth-First Search  BFS


def bfs(grid, row, col):
    queue = deque()
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue.append((row, col))

    while queue:
        for _ in range(len(queue)):
            current = queue.popleft()
            for dir in directions:
                r = current[0] + dir[0]
                c = current[1] + dir[1]
                if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]) or grid[r][c] == "0":
                    continue
                grid[r][c] = "0"
                queue.append((r, c))


grid = [["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]]
print(numIslands(grid))
