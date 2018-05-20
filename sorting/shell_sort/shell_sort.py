def shell_sort(alist, sequence):
    size = len(alist)

    if sequence == "shell":
        sequences = shell_sequences(size)
    elif sequence == "hibbard":
        sequences = hibbard_sequences(size)
    elif sequence == "knuth":
        sequences = knuth_sequences(size)
    else:
        raise ValueError("Please specify the sequence for Shell sorting")

    for increment in sequences:
        for index in range(increment, size):
            element = alist[index]
            position = index

            while position > 0 and alist[position - increment] > element:
                alist[position] = alist[position - increment]
                position -= increment

            alist[position] = element

    return alist


def shell_sequences(length):
    """
    Shell sequence: N/2, N/4, ..., 1

    """
    increment = length // 2
    increments = []

    while increment > 0:
        increments.append(increment)
        increment = increment // 2

    return increments


def hibbard_sequences(length):
    """
    Hibbard  sequence: 1, 3, 7, ... , 2^k - 1
    Worst-case running time of Shellsort using hibbard sequences is Theta(N^3/2).

    """
    increment = 1
    increments = []
    counter = 1

    while increment < length:
        increments.append(increment)
        counter += 1
        increment = 2**counter - 1

    return reversed(increments)


def knuth_sequences(length):
    """
    Knuth sequence: 1, 4, 13, ... , (3^k - 1) / 2

    """
    increment = 1
    increments = []
    counter = 0

    while increment < length:
        increments.append(increment)
        counter += 1
        increment = 3 ** counter - 1

    return reversed(increments)