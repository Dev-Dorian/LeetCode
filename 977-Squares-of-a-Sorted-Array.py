def sortedSquares(nums):
    hashmap = {}
    for index in range(len(nums)):
        hashmap[index] = nums[index] * nums[index]
    return sorted(hashmap.values())


nums = [-10000, -9999, 0, -7, -5, 0, 10000]
print(sortedSquares(nums))
