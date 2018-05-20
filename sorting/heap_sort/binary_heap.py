import math as m


class BinaryHeap(object):
    def __init__(self):
        self.array = [None]     # Initiated with a sentinel marker None.
        self.size = 0

    def _depth(self):
        return int(m.log(self.size, 2))

    def insert(self, item):
        self.array.append(item)
        self.size += 1
        self._bubble_up(self.size)

    def delete_min(self):
        self.array[1] = self.array[self.size]
        del self.array[self.size]
        self.size -= 1
        self._percolate_down(1)

    def build_heap(self, item_array):
        self.size = len(item_array)
        self.array = [None] + item_array

        for index in reversed(range(1, self.size//2 + 1)):
            self._percolate_down(index)

    def _bubble_up(self, item_index):
        parent_index = item_index//2
        parent = self.array[parent_index]
        if parent is None:
            return
        if parent > self.array[item_index]:
            self.array[item_index], self.array[parent_index] = \
                self.array[parent_index], self.array[item_index]
            self._bubble_up(parent_index)

    def _percolate_down(self, item_index):
        if 2*item_index + 1 <= self.size:
            left_child, right_child = self.array[2*item_index],\
                                      self.array[2*item_index+1]
        elif 2*item_index == self.size:
            left_child, right_child = self.array[2*item_index],\
                                      None
        else:
            return

        if right_child is not None and \
                (right_child < self.array[item_index]) and \
                right_child < left_child:
            self.array[item_index], self.array[2 * item_index + 1] = \
                self.array[2 * item_index + 1], self.array[item_index]
            self._percolate_down(2*item_index + 1)

        elif left_child <= self.array[item_index]:
            self.array[item_index], self.array[2*item_index] = \
                self.array[2*item_index], self.array[item_index]
            self._percolate_down(2*item_index)
