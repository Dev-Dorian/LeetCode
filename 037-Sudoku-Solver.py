def solveSudoku(board):
    def is_valid(num, row, col):
        for index in range(9):
            # print(board[3 * (row // 3) + index // 3][3*(col // 3) + index % 3])
            if board[row][index] == num or board[index][col] == num or board[3 * (row // 3) + index // 3][3*(col // 3) + index % 3] == num:
                return False
        return True

    def solve():
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for num in map(str, range(1, 10)):
                        if is_valid(num, i, j):
                            board[i][j] = num
                            if solve():
                                return True
                            board[i][j] = "."
                    return False
        return True
    solve()


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

solveSudoku(board)
for row in board:
    print(row)
