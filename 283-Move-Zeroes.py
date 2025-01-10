def moveZeroes(nums):
    left = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[left] = nums[i]
            left += 1
    for left in range(left, len(nums)):
        nums[left] = 0
    return nums


nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums))
