import bisect


def containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff):
    if valueDiff == 0 and len(set(nums)) == len(nums):
        return False

    bucket = {}
    width = valueDiff + 1

    for i, n in enumerate(nums):
        # print(n // width)
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


nums = [1, 2, 3, 1]  # [8,7,15,1,6,1,9,15]
indexDiff = 3  # 1
valueDiff = 0  # 3
print(containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff))


def containsNearbyAlmostDuplicate1(nums, indexDiff, valueDiff):
    window = []
    for i in range(len(nums)):
        if i > indexDiff:
            # Remove the element that is no longer in the window
            val_to_remove = nums[i - indexDiff - 1]
            index = bisect.bisect_left(window, val_to_remove)
            if index < len(window) and window[index] == val_to_remove:
                del window[index]

        # Find the position to insert nums[i]
        pos = bisect.bisect_left(window, nums[i])

        # Check the previous element
        if pos > 0:
            if nums[i] - window[pos - 1] <= valueDiff:
                return True

        # Check the current element
        if pos < len(window):
            if window[pos] - nums[i] <= valueDiff:
                return True

        # Insert nums[i] into the window
        bisect.insort(window, nums[i])

    return False
