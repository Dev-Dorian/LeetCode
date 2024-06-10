def convert(s, numRows):
    if numRows == 1:
        return s

    pos = [""] * numRows
    size = len(s)
    dir = 1
    current_row = 0

    for i in range(size):
        pos[current_row] += s[i]
        if current_row == 0:
            dir = 1
        elif current_row == (numRows - 1):
            dir = -1
        current_row += dir
    return "".join(pos)


if __name__ == '__main__':
    # begin
    # s = Solution()
    print(convert("HERMES", 3))
