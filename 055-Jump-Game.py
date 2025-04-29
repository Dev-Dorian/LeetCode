""" 
FUNCTION canJump(nums):
    result = 0
    n = length(nums)

    FOR index FROM 0 TO n - 1 DO
        IF result < index THEN
            RETURN False
        END_IF
        IF result >= n THEN
            RETURN True
        END_IF
        result = MAX(result, nums[index] + index)
    END_FOR

    RETURN True
END_FUNCTION
 """


def canJump(nums):
    result = 0
    # print(len(nums))

    # numsList = enumerate(nums)
    # print(list(numsList))

    # for index in range(len(nums)):
    for index, _ in enumerate(nums):
        if result < index:
            return False
        if result >= len(nums):
            return True
        result = max(result, nums[index] + index)
    return True


nums = [3, 2, 1, 0, 4]
print(canJump(nums))


def canJump_1(nums):
    result = 0
    n = len(nums)
    for index in range(n):
        if index > result:
            return False
        result = max(result, nums[index] + index)
    return True


nums = [3, 2, 1, 0, 4]
print(canJump_1(nums))
