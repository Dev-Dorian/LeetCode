def canPartition(nums):
    number_sum = sum(nums)
    if number_sum % 2 != 0:
        return False

    if number_sum % 2 == 0:
        return True
    return False

    """ if number_sum // 2:
            return True
    return False """


nums = [1, 2, 5]
print(canPartition(nums))
