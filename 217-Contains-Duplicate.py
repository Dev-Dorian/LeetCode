def constainsDuplicate(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        # print(nums[i])
        # print(nums[i + 1])
        if nums[i] == nums[i + 1]:
            return True
    return False


print(constainsDuplicate([1, 2, 4, 10, 2]))


def constainsDuplicate1(nums):
    return len(nums) != len(set(nums))


print(constainsDuplicate1([1, 2, 4]))
