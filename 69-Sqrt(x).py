def fSqrt(data):
    left, right = 0, data

    result = 0
    while left <= right:
        midle = left + ((right - left) // 2)
        if midle**2 > data:
            right = midle - 1
        elif midle**2 < data:
            left = midle + 1
            result = midle
        else:
            return midle
    return result


print(fSqrt(9))
