def trappingRainWater(height):
    total = 0
    left = 0
    right = len(height) - 1
    leftMax = 0
    rightMax = 0

    while (left < right):
        if height[left] < height[right]:
            if height[left] > leftMax:
                leftMax = height[left]
            else:
                total += leftMax - height[left]
            left += 1
        else:
            if height[right] > rightMax:
                rightMax = height[right]
            else:
                total += rightMax - height[right]
            right -= 1
    return total


height = [4, 2, 0, 3, 2, 5]
print(trappingRainWater(height))
