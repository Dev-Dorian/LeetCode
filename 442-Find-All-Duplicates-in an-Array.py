def findDuplicates(nums):
    result = []

    for index in range(len(nums)):
        lista = abs(nums[index]) - 1
        if nums[lista] < 0:
            result.append(lista + 1)
        nums[lista] = -nums[lista]
    return result


def findDuplicates1(nums):
    result = []

    for index in nums:
        lista = abs(index)
        if nums[lista - 1] < 0:
            result.append(lista)
        else:
            nums[lista - 1] *= -1
    return result


nums = [3, 5, 4, 5, 3, 2, 1, 4]
print(findDuplicates(nums))
