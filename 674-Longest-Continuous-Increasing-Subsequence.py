def findLengthOfLCIS(nums):
    max_length = 1
    current_length = 1

    for index in range(1, len(nums)):
        if nums[index] > nums[index - 1]:
            current_length += 1
            # if current_length > max_length:
            max_length = max(max_length, current_length)
        else:
            current_length = 1
    return max_length


nums = [1, 3, 5, 4, 7]
print(findLengthOfLCIS(nums))
