def missingNumber(nums):
    res = len(nums)

    for i in range(len(nums)):
        res ^= i ^ nums[i]
        # print(res)
    return res


def missingNumber1(nums):
    n = len(nums)
    expectedSum = n*(n+1)//2
    print(expectedSum)
    actualSum = sum(nums)
    return expectedSum - actualSum


nums = [3, 0, 1]
# print(missingNumber(nums))
print(missingNumber1(nums))
