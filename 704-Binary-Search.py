def linearSearch(nums, target):

    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


def binarySearch_1(nums, target):
    nums.sort()
    left = 0
    right = len(nums) - 1

    while left <= right:
        medium = (left + right) // 2
        if nums[medium] == target:
            return medium
        elif nums[medium] > target:
            right = medium - 1
        else:
            left = medium + 1
    return -1


nums = [-1, 0, 3, 5, 2, 9, 12, 1, 76, 50, 4]
target = 50

print(linearSearch(nums, target))
print(binarySearch_1(nums, target))
