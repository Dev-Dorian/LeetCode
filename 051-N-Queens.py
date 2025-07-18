def solveNQueens(n):
    col = set()
    posDiag = set()
    negDiag = set()

    res = []
    board = [["."] * n for index in range(n)]

    def bactrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r-c)
            board[r][c] = "Q"

            bactrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r-c)
            board[r][c] = "."
    bactrack(0)
    return res


n = 4
print(solveNQueens(n))
