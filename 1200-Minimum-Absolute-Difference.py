import math


def minimumAbsDifference(arr):
    arr.sort()
    m = math.inf
    result = []

    for array in range(len(arr)):
        print(arr[array], arr[array])


arr = [4, 2, 1, 3]
print(minimumAbsDifference(arr))
