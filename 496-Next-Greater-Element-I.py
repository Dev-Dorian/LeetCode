def nextGreaterElement(nums1, nums2):
    stack = []
    next_greater = {}

    for num in nums2:
        while stack and num > stack[-1]:
            last_element = stack.pop()
            next_greater[last_element] = num
        stack.append(num)
    return [next_greater.get(n, -1) for n in nums1]


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

print(nextGreaterElement(nums1, nums2))
