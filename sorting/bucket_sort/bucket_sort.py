def bucket_sort(alist, max_value):
    buckets = [0]*(max_value + 1)

    for integer in alist:
        buckets[integer] += 1

    sorted_list = []

    for index in range(max_value+1):
        for _ in range(buckets[index]):
            sorted_list.append(index)

    return sorted_list
