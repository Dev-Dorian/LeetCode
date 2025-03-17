def divideArray(nums):
    count = {}
    for index in nums:
        if index not in count:
            count[index] = 0
        count[index] += 1

    for n, cnt in count.items():
        if cnt % 2:
            return False
    return True


def divideArray_1(nums):
    odd_set = set()

    for index in nums:
        if index not in odd_set:
            odd_set.add(index)
        else:
            odd_set.remove(index)
    return len(odd_set) == 0


nums = [3, 2, 3, 2, 2, 2, 5]
print(divideArray_1(nums))
