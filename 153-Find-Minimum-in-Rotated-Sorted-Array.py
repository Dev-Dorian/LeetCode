def findMin(nums):
    left = 0
    right = len(nums) - 1
    while left <= right:
        medium = (left + right) // 2
        if nums[left] <= nums[right]:
            return nums[left]
        elif nums[medium] > nums[right]:
            left = medium + 1
        else:
            right = medium


nums = [3, 4, 5, 1, 2]
print(findMin(nums))
