def suggestedProducts(products, searchWord):
    products.sort()
    left = 0
    right = len(products) - 1
    result = []
    ans = []
    for index in range(len(searchWord)):
        search = searchWord[index]
        while left <= right and (len(products[left]) <= index or products[left][index] < search):
            left += 1
        while left <= right and (len(products[right]) <= index or products[right][index] > search):
            right -= 1
        words_left = right - left + 1
        # print(words_left)
        if words_left >= 3:
            result.append([products[left], products[left+1], products[left+2]])
        elif words_left == 2:
            result.append([products[left], products[left+1]])
        elif words_left == 1:
            result.append([products[left]])
        else:
            result.append([])
    return result


def suggestedProducts1(P, S):
    P.sort()
    ans, left, right = [], 0, len(P) - 1
    for i in range(len(S)):
        c, res = S[i], []
        while left <= right and (len(P[left]) == i or P[left][i] < c):
            left += 1
        while left <= right and (len(P[right]) == i or P[right][i] > c):
            right -= 1
        for j in range(3):
            if left + j > right:
                break
            else:
                res.append(P[left+j])
        ans.append(res)
    return ans


def suggestedProducts2(products, searchWord):
    res = []
    rightp = 0
    products.sort()
    while rightp < len(searchWord):
        r = []
        for product in products:
            if len(r) == 3:
                break
            if product.startswith(searchWord[0:rightp + 1]):
                r.append(product)
        res.append(r)
        rightp += 1
    return res


products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
# products = ["havana"]
searchWord = "mouse"
print(suggestedProducts(products, searchWord))
print(suggestedProducts1(products, searchWord))
print(suggestedProducts2(products, searchWord))
