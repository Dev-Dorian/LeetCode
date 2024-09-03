
class Solution():
    def isSoduku(self, board):
        set1 = set()
        set2 = set()
        set3 = set()

        for i in range(9):
            set1 = set()
            for j in range(9):
                if board[i][j].isnumeric() and board[i][j] in set1:
                    print(set1, board[i][j])
                    return False
                set1.add(board[i][j])

        for i in range(9):
            set2 = set()
            for j in range(9):
                if board[j][i].isnumeric() and board[j][i] in set2:
                    print(set1, board[j][i])
                    return False
                set2.add(board[j][i])

        for i in range(9):
            for j in range(9):
                set3 = set()
                if i % 3 == 0 and j % 3 == 0:
                    print(i, j)
                    for k in range(i, i+3):
                        for v in range(j, j+3):
                            if board[k][v].isnumeric() and board[k][v] in set3:
                                return False
                            set3.add(board[k][v])

        return True


if __name__ == "__main__":
    board = [[".", ".", "4", ".", ".", ".", "6", "3", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             ["5", ".", ".", ".", ".", ".", ".", "9", "."],
             [".", ".", ".", "5", "6", ".", ".", ".", "."],
             ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
             [".", ".", ".", "7", ".", ".", ".", ".", "."],
             [".", ".", ".", "8", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."]]

    print(Solution().isSoduku(board))
