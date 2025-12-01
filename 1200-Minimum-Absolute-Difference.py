import math


def minimumAbsDifference(arr):
    arr.sort()
    m = float('inf')  # math.inf
    result = []

    for array in range(1, len(arr)):
        if arr[array] - arr[array - 1] < m:
            m = arr[array] - arr[array - 1]
            result = [[arr[array - 1], arr[array]]]
        elif arr[array] - arr[array - 1] == m:
            result.append([arr[array - 1], arr[array]])

    return result
#    print(arr[array], arr[array - 1])


arr = [4, 2, 1, 3]
print(minimumAbsDifference(arr))


def minimumAbsDifference_1(arr):
    arr.sort()
    min_diff = float('inf')  # math.inf
    result = []

    for array in range(1, len(arr)):
        cur = abs(arr[array] - arr[array - 1])
        if cur < min_diff:
            min_diff = cur
            result = [[arr[array - 1], arr[array]]]
        elif arr[array] - arr[array - 1] == min_diff:
            result.append([arr[array - 1], arr[array]])

    return result
#    print(arr[array], arr[array - 1])


arr = [4, 2, 1, 3]
print(minimumAbsDifference_1(arr))
