def singleNumber(nums):
    res = 0
    for index in nums:
        res = index ^ res
    return res


nums = [2, 2, 1]
print(singleNumber(nums))
