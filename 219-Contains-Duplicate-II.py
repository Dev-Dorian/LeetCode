def containsNearbyDuplicate(nums, k):
    window = set()
    L = 0
    for R in range(len(nums)):
        if R - L > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])
    return False


nums = [1, 2, 3, 1]
k = 3

print(containsNearbyDuplicate(nums, k))
