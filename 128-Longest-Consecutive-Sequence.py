def longestSequence(nums):
    if len(nums) == 0:
        return 0
    treeset = set()
    # float("INF")  #Positive infinity
    # float("-INF") #Negative infinity
    max = float('-inf')  # this is same Integer.MIN_VALUE
    currentMax = 0
    prev = 0

    for num in nums:
        treeset.add(num)

    for n in sorted(treeset):
        if n - prev == 1:
            currentMax += 1
        else:
            currentMax = 1
        prev = n

        if currentMax > max:
            max = currentMax

    return max


nums = [100, 4, 200, 1, 3, 2]
print(longestSequence(nums))
