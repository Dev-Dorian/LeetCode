def Median():
    a = nums1 = [1, 2]  # [1, 2, 6, 7, 8]
    b = nums2 = [3, 4]  # [3, 4, 5, 9, 10, 11]
    m = len(nums1)
    n = len(nums2)
    if n < m:
        a = nums2
        b = nums1
    s = 0
    e = len(a)
    while s <= e:
        p1 = (s + e)//2
        p2 = (m + n + 1)//2 - p1
        maxLA = a[p1-1] if p1 > 0 else float("-infinity")
        maxLB = b[p2-1] if p2 > 0 else float("-infinity")
        minRA = a[p1] if p1 < len(a) else float("infinity")
        minRB = b[p2] if p2 < len(b) else float("infinity")
        if (maxLA <= minRB) and (maxLB <= minRA):
            d1 = max(maxLA, maxLB)
            d2 = min(minRA, minRB)
            if (n + m) % 2 == 0:
                return (d1 + d2)/2
            else:
                return d1
        elif maxLA > minRB:
            e = p1 - 1
        elif maxLB > minRA:
            s = p1 + 1


print(Median())
