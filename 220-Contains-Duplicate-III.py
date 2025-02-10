def containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff):
    if valueDiff == 0 and len(set(nums)) == len(nums):
        return False

    bucket = {}
    width = valueDiff + 1

    for i, n in enumerate(nums):
        bucket_i = n // width

        if bucket_i in bucket:
            return True
        elif bucket_i + 1 in bucket and abs(n - bucket[bucket_i + 1]) < width:
            return True
        elif bucket_i - 1 in bucket and abs(n - bucket[bucket_i - 1]) < width:
            return True

        bucket[bucket_i] = n
        if i >= indexDiff:
            del bucket[nums[i-indexDiff] // width]

    return False


nums = [1, 2, 3, 1]
indexDiff = 3
valueDiff = 0
print(containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff))
