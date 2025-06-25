def hIndex1(citations):
    c = sorted(citations)
    hIndex = 0

    for index in range(len(c)-1, -1, -1):
        if c[index] > hIndex:
            hIndex += 1
    return hIndex


citations = [1, 8, 4, 5, 7]
print(hIndex1(citations))
