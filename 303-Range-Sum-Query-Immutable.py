class NumArray:
    def __init__(self, nums):
        self.prefix = []
        cur = 0
        for n in nums:
            cur += n
            self.prefix.append(cur)

    def sumRange(self, left, right):
        rightSum = self.prefix[right]
        leftSum = self.prefix[left - 1] if left > 0 else 0
        return rightSum - leftSum


def test(nums):
    ans = []
    cur = 0
    for i in nums:
        cur += i
        ans.append(cur)
    return ans


nums = [1, 3, 5, 7, 9]
result = NumArray(nums).sumRange(1, 3)
print(result)


print(test(nums))
