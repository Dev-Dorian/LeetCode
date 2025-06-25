def hIndex(citations):
    c = sorted(citations)
    h = 0

    for index in range(len(c)-1, -1, -1):
        if c[index] > h:
            h += 1
    return h


citations = [1, 8, 4, 5, 7]
print(hIndex(citations))
