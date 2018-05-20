def merge(alist, temp_list, left_pos, right_pos, right_end):
    left_end = right_pos - 1
    tmp_pos = left_pos

    while left_pos <= left_end and right_pos <= right_end:
        if alist[left_pos] <= alist[right_pos]:     # <= maintains sort stability
            temp_list[tmp_pos] = alist[left_pos]
            left_pos += 1
        else:
            temp_list[tmp_pos] = alist[right_pos]
            right_pos += 1
        tmp_pos += 1

    while left_pos <= left_end:
        temp_list[tmp_pos] = alist[left_pos]
        left_pos += 1
        tmp_pos += 1

    while right_pos <= right_end:
        temp_list[tmp_pos] = alist[right_pos]
        right_pos += 1
        tmp_pos += 1

    return temp_list


def sort(alist, temp_list, left, right):
    """
    The function recursively calls itself on sub-lists, followed by a call to
    merge two sorted sub-lists.
    Key points:
        Since slicing a list in python is O(N), where N is size of slice,
        recursive calls are provided with indexes instead.

        Copying temp_list back to items slows down merge sort considerably.
        Thus, role of temp_list and items are exchanged at alternate recursive
        calls and no more copying is needed.

    """
    if left < right:
        center = (left + right) // 2
        sort(temp_list, alist, left, center)
        sort(temp_list, alist, center + 1, right)
        return merge(temp_list, alist, left, center + 1, right)


def merge_sort(alist):
    temp_list = alist[:]
    return sort(alist, temp_list, 0, len(temp_list) - 1)
