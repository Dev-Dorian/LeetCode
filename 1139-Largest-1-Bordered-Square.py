def largest1BorderedSquare(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    max_side = 0

    for k in range(min(rows, cols), 0, -1):
        print(k)
        foundSquare = False
        for r in range(rows - k + 1):
            print(r)
            for c in range(cols - k + 1):
                # print(k, r, c)
                top_border = all(grid[r][i] == 1 for i in range(c, c + k))
               # print(top_border)
                bottom_border = all(grid[r + k - 1][i]
                                    == 1 for i in range(c, c + k))
                left_border = all(grid[i][c] == 1 for i in range(r, r + k))
                right_border = all(grid[i][c + k - 1] ==
                                   1 for i in range(r, r + k))

                if top_border and bottom_border and left_border and right_border:
                    max_side = k
                    foundSquare = True
                    break
                # print(top_border)
            if foundSquare:
                break
        if foundSquare:
            break
    return max_side * max_side


grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1,]]
print(largest1BorderedSquare(grid))
