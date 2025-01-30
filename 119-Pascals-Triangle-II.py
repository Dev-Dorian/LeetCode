def getRow(rowIndex):
    res = [1]

    for index in range(rowIndex):
        nextRow = [0] * (len(res) + 1)
        for j in range(len(res)):
            nextRow[j] += res[j]
            nextRow[j+1] += res[j]
        res = nextRow
    return res


rowIndex = 3
print(getRow(rowIndex))
