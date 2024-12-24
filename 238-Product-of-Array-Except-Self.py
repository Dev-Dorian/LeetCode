def productArrayExceptSelf(nums):
    ans = [1] * len(nums)
    for i in range(1, len(nums)):
        ans[i] = ans[i - 1] * nums[i - 1]
        right = 1
    for i in range(len(nums) - 1, -1, -1):
        ans[i] *= right
        right *= nums[i]
    return ans


def productArrayExceptSelf_1(nums):
    ans = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        ans[i] = prefix
        prefix *= nums[i]
    sufix = 1
    for i in range(len(nums) - 1, -1, -1):
        ans[i] *= sufix
        sufix *= nums[i]
    return ans


def productArrayExceptSelf_2(nums):
    ans = len(nums)
    products = [1] * ans
    for i in range(1, ans):
        products[i] = products[i-1] * nums[i-1]

    right = nums[-1]
    for i in range(ans-2, -1, -1):
        products[i] *= right
        right *= nums[i]
    return products


nums = [2, 3, 4, 5]
print(productArrayExceptSelf(nums))
print(productArrayExceptSelf_1(nums))
print(productArrayExceptSelf_2(nums))
