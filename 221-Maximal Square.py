def maximalSquare(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    print(cols)
    dp = [[0] * (cols + 1) for _ in range(rows+1)]
    max_side = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1':
                dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
                max_side = max(max_side, dp[i+1][j+1])
    return max_side * max_side


matrix = [["0", "1"], ["1", "0"]]
print(maximalSquare(matrix))
