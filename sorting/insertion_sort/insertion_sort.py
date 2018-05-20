def insertion_sort(alist):
    for index in range(1, len(alist)):
        element = alist[index]
        position = index

        while position > 0 and alist[position - 1] > element:
            alist[position] = alist[position - 1]
            position -= 1

        alist[position] = element
    return alist