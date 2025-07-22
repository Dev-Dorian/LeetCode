def combinationSum2(candidates, target):
    ans = []

    def backtracking(start, current, total):
        if total == target:
            ans.append(current[:])
            return
        if total > target:
            return
        for index in range(start, len(candidates)):
            if index > start and candidates[index-1] == candidates[index]:
                continue
            if candidates[index] > target:
                continue

            current.append(candidates[index])
            backtracking(index+1, current, total+candidates[index])
            current.pop()
    candidates.sort()
    backtracking(0, [], 0)
    return ans


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(combinationSum2(candidates, target))
