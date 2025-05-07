def intersection(nums1, nums2):
    seen = set(nums1)
    res = []

    for n in nums2:
        if n in seen:
            res.append(n)
            seen.remove(n)
    return res


nums1 = [1, 2, 6, 4]
nums2 = [5, 6]

print(intersection(nums1, nums2))
