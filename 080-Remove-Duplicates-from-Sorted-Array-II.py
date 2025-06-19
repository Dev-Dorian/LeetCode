def removeDuplicates(nums):
    count = 1
    if len(nums) == 0:
        return 0
    for index in range(1, len(nums)):
        print(nums[index], nums[count - 2])
        if count == 1 or nums[index] != nums[count - 2]:
            nums[count] = nums[index]
            count += 1
    return count


nums = [9, 9, 10, 11, 11, 15]
print(removeDuplicates(nums))
