import collections


class Solution():
    def isSoduku(self, board):
        """
        for i in range(0, 9, 3):
            s = set()
            for j in range(0, 9, 3):
                item = board[i][j]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)

        for i in range(0, 9, 3):
            s = set()
            for j in range(0, 9, 3):
                item = board[j][i]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)

        for i, j in board:
            s = set()
            for row in range(i, i+9):
                for col in range(j, j+9):
                    item = board[row][col]
                    if item in s:
                        return False
                    elif item != '.':
                        s.add(item)
        return True
        """
        columns = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in columns[c] or
                        board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                columns[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
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
