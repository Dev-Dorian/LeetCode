import math


def minEatingSpeed(piles, h):
    left = 1
    right = 1
    for p in piles:
        right = max(right, p)
    res = right

    while left <= right:
        speed = (left + right) // 2
        hours = 0

        for p in piles:
            hours += math.ceil(p/speed)
        if hours <= h:
            res = speed
            right = speed - 1
        else:
            left = speed + 1
    return res


def minEatingSpeed1(piles, h):
    l, r = 1, max(piles)
    while l < r:
        k = l + (r - l) // 2
        hrs = 0
        for pile in piles:
            hrs += pile / k
        if hrs <= h:
            r = k
        else:
            l = k + 1

    return l


def minEatingSpeed2(piles, h):
    l, r = 1, max(piles)
    while l < r:
        k = l + (r - l) // 2
        hrs = 0
        for pile in piles:
            hrs += pile / k + 1
        if hrs <= h:
            r = k
        else:
            l = k + 1

    return l


piles = [3, 6, 7, 11]
h = 8

print(minEatingSpeed1(piles, h))
