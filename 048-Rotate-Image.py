def rotate(matrix):
    left = 0
    right = len(matrix) - 1
    print(right)
    while left < right:
        # matrix[left], matrix[right] = matrix[right], matrix[left] OPTIONAL 1

        temp = matrix[left]  # OPTIONAL 2
        matrix[left] = matrix[right]
        matrix[right] = temp

        left += 1
        right -= 1
    for i in range(len(matrix)):
        for j in range(i):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    return matrix


def rotate1(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
    return matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(matrix))
print(rotate1(matrix))
