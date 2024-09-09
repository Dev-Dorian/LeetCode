list = [0, 1, 2, 2, 3, 0, 4, 2, 2, 54]
value = 2


def removeElement(array, val):
    l = 0
    for r in range(len(array)):
        if array[r] != val:
            array[l] = array[r]
            l += 1
            print(array[r])
    return l


print(removeElement(list, value))
