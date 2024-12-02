def threeSum(nums):
    if len(nums) < 3:
        return []
    ans = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            sum = nums[i] + nums[l] + nums[r]
            if sum == 0:
                ans.append((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
                while nums[r] == nums[r + 1] and l < r:
                    r -= 1
            elif sum < 0:
                l += 1
            else:
                r -= 1
    return ans


def threeSum_1(nums):
    ans = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue
        b = i + 1
        c = len(nums) - 1

        while b < c:
            sum3 = a + nums[b] + nums[c]
            if sum3 > 0:
                c -= 1
            elif sum3 < 0:
                b += 1
            else:
                ans.append([a, nums[b], nums[c]])
                b += 1
                c -= 1
                while nums[b] == nums[b-1] and b < c:
                    b += 1
    return ans


print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum_1([-1, 0, 1, 2, -1, -4]))
