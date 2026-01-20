def imageSmoother(img):
    rows = len(img)
    cols = len(img[0])

    res = [[0] * cols for _ in range(rows)]


img = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(imageSmoother(img))
