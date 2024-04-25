def Search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right)
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return left


list = [1, 3, 5, 6]
target = 4
print(Search(list, target))
