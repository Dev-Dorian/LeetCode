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


nums = [5, 4, 3, 2, 1]
print(increasingTriplet(nums))
