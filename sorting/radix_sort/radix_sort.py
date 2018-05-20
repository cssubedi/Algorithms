def radix_sort(alist, max_len):
    words_by_length = [[] for _ in range(max_len + 1)]
    for string in alist:
        words_by_length[len(string)].append(string)

    buckets = [[] for _ in range(256)]

    index = 0
    for word_list in words_by_length:
        for string in word_list:
            alist[index] = string
            index += 1

    start_index = len(alist)

    for position in range(max_len - 1, -1, -1):
        start_index -= len(words_by_length[position + 1])

        for index in range(start_index, len(alist), +1):
            string = alist[index]
            buckets[ord(string[position])].append(string)

        index = start_index
        for this_bucket in buckets:
            for string in this_bucket:
                alist[index] = string
                index += 1
            this_bucket.clear()

    return alist





