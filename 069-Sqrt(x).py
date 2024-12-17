def fSqrt(x):
    left, right = 0, x

    result = 0
    while left <= right:
        midle = left + ((right - left) // 2)
        if midle**2 > x:
            right = midle - 1
        elif midle**2 < x:
            left = midle + 1
            result = midle
        else:
            return midle
    return result


def fSqrt1(x):
    left = 0
    right = x

    while left <= right:
        m = (left + right) // 2
        if m * m < x:
            left = m + 1
        elif m * m > x:
            right = m-1
        else:
            return m
    return right


print(fSqrt(4))
print(fSqrt1(8))
