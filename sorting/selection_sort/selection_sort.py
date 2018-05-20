def selection_sort(alist):
    length = len(alist)

    for i in range(0, length):
        min_index = i
        for j in range(i, length):
            if alist[j] < alist[min_index]:
                min_index = j

        alist[i], alist[min_index] = alist[min_index], alist[i]

    return alist
