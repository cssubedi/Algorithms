def generate_pivot(alist, left_index, right_index):
    center_index = (left_index + right_index) // 2

    if alist[left_index] > alist[center_index]:
        alist[left_index], alist[center_index] = alist[center_index], alist[left_index]
    if alist[left_index] > alist[right_index]:
        alist[left_index], alist[right_index] = alist[right_index], alist[left_index]
    if alist[center_index] > alist[right_index]:
        alist[center_index], alist[right_index] = alist[right_index], alist[center_index]

    # Swap second last element and pivot.
    alist[center_index], alist[right_index - 1] = alist[right_index - 1], alist[center_index]

    return alist[right_index - 1]


def _insertion_sort(alist, left, right):
    for index in range(left + 1, right + 1):
        element = alist[index]
        position = index

        while position > 0 and alist[position - 1] > element:
            alist[position] = alist[position-1]
            position -= 1

        alist[position] = element


def sort(alist, left, right):
    if (right - left) > 2:
        pivot = generate_pivot(alist, left, right)
        i, j = left + 1, right - 2

        while i <= j:
            while alist[i] < pivot:
                i += 1

            while alist[j] > pivot:
                j -= 1

            if i <= j:
                alist[i], alist[j] = alist[j], alist[i]
                i += 1
                j -= 1

        alist[i], alist[right-1] = alist[right-1], alist[i]

        sort(alist, left, i - 1)
        sort(alist, i + 1, right)
    else:
        _insertion_sort(alist, left, right)

    return alist


def quick_sort(alist):
    if len(alist) == 0:
        return alist
    return sort(alist, 0, len(alist) - 1)
