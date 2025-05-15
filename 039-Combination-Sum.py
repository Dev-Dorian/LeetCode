def combinationSum(candidates, target):
    result = []
    candidates.sort()

    def backtrack(combination, remaining, start_index):
        if remaining == 0:
            # result.append(combination.copy())
            result.append(combination[:])
            return
        if remaining < 0:
            return
        for index in range(start_index, len(candidates)):
            if candidates[index] > remaining:
                break
            combination.append(candidates[index])
            backtrack(combination, remaining - candidates[index], index)
            combination.pop()
    backtrack([], target, 0)
    return result


def combinationSum_1(candidates, target):
    result = []

    def backtrack(start, current, total):
        if total == target:
            result.append(current[:])
            return
        if total > target:
            return
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, total+candidates[i])
            current.pop()

    backtrack(0, [], 0)
    return result


candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates,  target))
print(combinationSum_1(candidates,  target))
