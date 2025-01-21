def increasingTriplet(nums):
    if len(nums) < 3:
        return False

    first = second = float('inf')
    for index in nums:
        if index <= first:
            first = index
        elif index <= second:
            second = index
        else:
            return True
    return False


nums = [2, 1, 5, 0, 4, 6]
print(increasingTriplet(nums))
