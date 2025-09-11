def threeSumClosest(nums, target):
    nums.sort()
    closestNum = float('inf')

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == target:
                return total

            if abs(total - target) < abs(closestNum - target):
                closestNum = total

            if total < target:
                left += 1
            else:
                right -= 1
    return closestNum


print(threeSumClosest([-1, 2, 1, 2], 5))
