def rotate(nums, k):
    k = k % len(nums)

    def swap(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    swap(0, len(nums) - 1)
    swap(0, k-1)
    swap(k, len(nums) - 1)
    return nums


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

print(rotate(nums, k))
