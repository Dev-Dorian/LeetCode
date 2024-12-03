def constainsDuplicate(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        # print(nums[i])
        # print(nums[i + 1])
        if nums[i] == nums[i + 1]:
            return True
    return False


def constainsDuplicate1(nums):
    return len(nums) != len(set(nums))


def constainsDuplicate2(nums):
    mySet = set()
    for i in nums:
        if i in mySet:
            return True
        mySet.add(i)
    return False


print(constainsDuplicate([1, 2, 4, 10, 2]))
print(constainsDuplicate1([1, 2, 4, 10, 2]))
print(constainsDuplicate2([1, 2, 4, 10, 2]))

print(constainsDuplicate([1, 2, 4]))
print(constainsDuplicate1([1, 2, 4]))
print(constainsDuplicate2([1, 2, 4]))
