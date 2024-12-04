def missingNumber(nums):
    res = len(nums)

    for i in range(len(nums)):
        res ^= i ^ nums[i]
        print(res)
    return res


nums = [3, 0, 1]
print(missingNumber(nums))
