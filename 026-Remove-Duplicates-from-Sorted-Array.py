from typing import List


def removeDuplicates(nums):
    l = 1

    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            l += 1
        # print(r)
    return l


list = [1, 3, 15, 64, 64, 2]
print(removeDuplicates(list))
"""


def removeDuplicates1(nums):
    if len(nums) == 0:
        return 0
    left = 0
    for i in range(1, len(nums)):
        if nums[left] == nums[i]:
            continue
        else:
            left += 1
            nums[left] = nums[i]
    return left + 1


list = [1, 1, 2]
print(removeDuplicates1(list))
"""
# class Solution:
#     def removeDuplicates12(self, nums: List[int]) -> int:
#         j = 1
#         for i in range(1, len(nums)):
#             if nums[i] != nums[i - 1]:
#                 nums[j] = nums[i]
#                 j += 1
#         return j, nums


# solution = Solution()
# result = solution.removeDuplicates12([1, 1, 2, 2, 3, 3])
# print(result)
