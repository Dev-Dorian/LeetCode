def summaryRanges(nums):
    ans = []
    i = 0
    while i < len(nums):
        start = nums[i]
        print(i < len(nums) - 1)
        while i < len(nums) - 1 and nums[i] + 1 == nums[i+1]:
            i += 1
        if start != nums[i]:
            ans.append(str(start) + '->' + str(nums[i]))
        else:
            ans.append(str(nums[i]))
        i += 1
    return ans


nums = [0, 1, 2, 4, 5, 7]
print(summaryRanges(nums))
