def intersection(nums1, nums2):
    seen = set(nums1)
    res = []

    for n in nums2:
        if n in seen:
            res.append(n)
            seen.remove(n)
    return res


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

print(intersection(nums1, nums2))
