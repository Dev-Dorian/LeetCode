def findClosestNumber(nums):
    ans = nums[0]
    for index in nums:
        # print(abs(index))
        if abs(index) < abs(ans):  # abs Return the absolute value of a number
            ans = index
        elif abs(index) == abs(ans):
            if index > ans:
                ans = index
    return ans


nums = [-4, -2, 1, 4, 8]
print(findClosestNumber(nums))


# print(abs(-3 * -2))
