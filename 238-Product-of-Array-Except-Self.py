def productArrayExceptSelf(nums):
    ans = [1] * len(nums)
    for i in range(1, len(nums)):
        ans[i] = ans[i - 1] * nums[i - 1]
        right = 1
    for i in range(len(nums) - 1, -1, -1):
        ans[i] *= right
        right *= nums[i]
    return ans


nums = [1, 2, 3, 4]
print(productArrayExceptSelf(nums))
