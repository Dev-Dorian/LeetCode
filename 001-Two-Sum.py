def two_sum(nums, target):
    num_dict = {}
    solution = [0, 0]

    for i in range(len(nums)):
        remaining = target - nums[i]
        if remaining in num_dict:
            solution[0] = i
            solution[1] = num_dict[remaining]
            return solution
        else:
            num_dict[nums[i]] = i

    return solution


print(two_sum([1, 1, 3], 5))
