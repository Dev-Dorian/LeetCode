def Merge_Two_Sorted_Lists():
    test_list1 = [1, 5, 6, 9, 11]
    test_list2 = [3, 4, 7, 8, 10, 15]
    size_1 = len(test_list1)
    size_2 = len(test_list2)

    res = []
    i, j = 0, 0

    while i < size_1 and j < size_2:
        if test_list1[i] < test_list2[j]:
            res.append(test_list1[i])
            i += 1
        else:
            res.append(test_list2[j])
            j += 1
    res = res + test_list1[i:] + test_list1[j:]
    print("The List is : " + str(res))


Merge_Two_Sorted_Lists()
