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


def maxAreaContainer_1(height):
    left = 0
    right = len(height) - 1
    maxNumber = 0
    while left < right:
        if height[left] < height[right]:
            maxNumber = max(maxNumber, height[left] * (right - left))
            left += 1
        else:
            maxNumber = max(maxNumber, height[right] * (right - left))
            right -= 1
    return maxNumber


print(maxAreaContainer([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxAreaContainer_1([1, 8, 6, 2, 5, 4, 8, 3, 7]))
