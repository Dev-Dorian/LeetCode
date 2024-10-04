def binarySearch(nums, target):

    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 5

print(binarySearch(nums, target))
