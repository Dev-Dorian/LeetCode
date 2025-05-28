list = [3, 2, 2, 3]
value = 3


def removeElement(array, val):
    l = 0
    for r in range(len(array)):
        print(array[r])
        if array[r] != val:
            array[l] = array[r]
            l += 1
            print(array[l])
    return l, array[r]


print(removeElement(list, value))
