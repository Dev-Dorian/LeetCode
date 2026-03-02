def canPartition(nums):
    number_sum = sum(nums)
    if number_sum % 2 != 0:
        return False

    target = number_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for index in range(target, num - 1, -1):
            dp[index] = dp[index] or dp[index - num]
    return dp[target]


nums = [1, 5, 11, 5]
print(canPartition(nums))
