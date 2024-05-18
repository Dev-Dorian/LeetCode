class Solution():
    """
    def merget0(self, nums1, m, nums2, n):
        for get in range(len(nums1) - 1, m - 1, -1):
            # print(len(nums1) - 1, m - 1, -1)
            nums1.pop(get)
        for check in range(len(nums2)):
            nums1.append(nums2[check])
        nums1.sort()
        return nums1
    """

    def merget1(self, nums1, m, nums2, n):
        i, j, k = 0, 0, 0
        temp = nums1.copy()
        while i < m and j < n:
            if temp[i] < nums2[j]:
                nums1[k] = temp[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        while i < m:
            nums1[k] = temp[i]
            i += 1
            k += 1
        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1
        return nums1
        # print(temp)

    def merget2(self, nums1, m, nums2, n):
        del nums1[m:]
        nums1.extend(nums2)
        nums1.sort()
        return nums1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
# print(Solution().merget0(nums1, m, nums2, n))
# print(Solution().merget1(nums1, m, nums2, n))
print(Solution().merget2(nums1, m, nums2, n))
