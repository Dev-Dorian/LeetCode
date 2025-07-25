def subsets(nums):
    res = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            # res.append(subset.copy())
            res.append(subset[:])
            return

        subset.append(nums[i])
        dfs(i + 1)

        subset.pop()
        dfs(i + 1)
    dfs(0)
    return res


nums = [41, 52, 63]
print(subsets(nums))
