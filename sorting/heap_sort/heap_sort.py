import sys
sys.path.append("./heap_sort/")
from binary_heap import BinaryHeap


class HeapSort(BinaryHeap):
    def __init__(self):
        BinaryHeap.__init__(self)

    def delete_min(self):
        self.array[1], self.array[self.size] = self.array[self.size], self.array[1]
        self.size -= 1
        self._percolate_down(1)

    def sort(self, alist):
        self.build_heap(alist)
        for _ in range(self.size):
            self.delete_min()

        return self.array


def heap_sort(alist):
    sort = HeapSort()
    return sort.sort(alist)[1:]