

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


def two_sum_1(nums, target):
    for start in range(len(nums)):
        for end in range(start + 1, len(nums)):
            if nums[start] + nums[end] == target:
                return [start, end]


print(two_sum([11, 15, 4, 5], 9))
print(two_sum_1([2, 7, 11, 15], 9))
