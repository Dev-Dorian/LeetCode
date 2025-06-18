def removeDuplicates(nums):
    count = 1
    if len(nums) == 0:
        return 0
    for index in range(1, len(nums)):
        if count == 1 or nums[index] != nums[count - 2]:
            nums[count] = nums[index]
            count += 1
    return count


nums = [1, 1, 1, 2, 2, 37]
print(removeDuplicates(nums))
