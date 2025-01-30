def minimumTotal(triangle):
    for row in range(len(triangle)-2, -1, -1):
        for col in range(0, len(triangle[row])):
            triangle[row][col] += min(triangle[row+1]
                                      [col], triangle[row+1][col+1])
    return triangle[0][0]


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(minimumTotal(triangle))
