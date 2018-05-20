def bubble_sort(alist):
    length = len(alist)
    for i in range(0, length):
        for j in range(1, length - i):
            if alist[j - 1] > alist[j]:
                alist[j - 1], alist[j] = alist[j], alist[j - 1]

    return alist
