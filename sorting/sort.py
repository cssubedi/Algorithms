#!/usr/bin/python

from __future__ import print_function, unicode_literals
import argparse
from random import randint
import sys
sys.path.append("../")
import sorting


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parses arguments for sorting")
    parser.add_argument("--algorithm",
                        action="store",
                        required=False,
                        default="insertion sort",
                        help="Choose a sorting algorithm.")
    parser.add_argument("--items",
                        action="store",
                        dest="items",
                        required=False,
                        default=[randint(0, 100) for _ in range(10)],
                        help="Specify items to sort.")
    parser.add_argument("--sequence",
                        action="store",
                        dest="sequence",
                        required=False,
                        default="shell",
                        choices=["shell", "hibbard", "knuth"],
                        help="If using Shell sort, specify the sequence to use.")

    args = parser.parse_args()
    print()
    print("Unsorted list: {}".format(args.items))
    print()

    if type(args.items) == str:
        items = [int(i) for i in args.items[1:-1].split(",")]
    else:
        items = args.items

    if args.algorithm == "bubble sort":
        sorted_list = sorting.bubble_sort(items)

    elif args.algorithm == "selection sort":
        sorted_list = sorting.selection_sort(items)

    elif args.algorithm == "insertion sort":
        sorted_list = sorting.insertion_sort(items)

    elif args.algorithm == "shell sort":
        sorted_list = sorting.shell_sort(items, args.sequence)

    elif args.algorithm == "heap sort":
        sorted_list = sorting.heap_sort(items)

    elif args.algorithm == "merge sort":
        sorted_list = sorting.merge_sort(items)

    elif args.algorithm == "quick sort":
        sorted_list = sorting.quick_sort(items)

    else:
        raise ValueError("Please specify the algorithm.")

    print("Sorted list: {}".format(sorted_list))