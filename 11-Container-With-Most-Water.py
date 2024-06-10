import math


def maxAreaContainer(height):
    maxArea = 0
    left = 0
    right = len(height) - 1
    while left < right:
        base = right - left
        minHeight = min(height[left], height[right])
        currentArea = base * minHeight
        maxArea = max(maxArea, currentArea)
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return maxArea


print(maxAreaContainer([1, 8, 6, 2, 5, 4, 8, 3, 7]))
