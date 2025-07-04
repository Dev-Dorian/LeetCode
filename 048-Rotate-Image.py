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


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(matrix))
