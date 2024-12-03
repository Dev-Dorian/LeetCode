def getConcatenation(nums):
    return nums * 2


def getConcatenation_1(nums):
    ans = []
    for j in range(2):
        for i in nums:
            ans.append(i)
    return ans


nums = [1, 2, 1]
print(getConcatenation(nums))
print(getConcatenation_1(nums))
