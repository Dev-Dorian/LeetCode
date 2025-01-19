def zeroFilledSubarray(nums):
    res, count = 0, 0

    for index in range(len(nums)):
        if nums[index] == 0:
            count += 1
        else:
            count = 0
        res += count
    return res


nums = [1, 3, 0, 0, 2, 0, 0, 4]
print(zeroFilledSubarray(nums))
