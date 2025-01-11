def majorityElement(nums):
    count = 0
    candidates = 0
    for num in nums:
        if count == 0:
            candidates = num
        count += 1 if num == candidates else -1
    return candidates


nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))
