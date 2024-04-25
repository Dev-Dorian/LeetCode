from typing import List


def removeDuplicates(nums):
    l = 1

    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            l += 1
        # print(r)
    return l, nums


list = [1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7]
print(removeDuplicates(list))


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
