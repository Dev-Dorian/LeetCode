def twoSumll(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        current = numbers[left] + numbers[right]
        if current > target:
            right -= 1
        elif current < target:
            left += 1
        elif current == target:
            break
    return left + 1, right + 1


numbers = [2, 7, 11, 15]
target = 9
print(twoSumll(numbers, target))
