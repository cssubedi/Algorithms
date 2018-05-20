import math as m


class BinaryHeap(object):
    def __init__(self):
        """
            The class implements a variant of binary heap called min heap.
            First element is the smallest element.

            Space needed:
            N (actually, max size of array) + Sentinel marker + size = N + 2

            Space Complexity = O(N)
        """
        self.array = [None]     # Initiated with a sentinel marker None.
        self.size = 0

    def __str__(self):
        if self.size == 0:
            return ""
        else:
            return self._print_tree()

    def _depth(self):
        """
        For binary heap of depth d,
            Minimum number of elements:
                2^d                    (1 leaf on dth layer)
            Maximum number of elements:
                2^(d+1) - 1
            Thus bounds on depth of binary heap is
                log(N+1) - 1 <= d <= log(N) (E.g: N=2^7 --> 6 <=d <= 7)
            Depth = O(logN)
        Returns:

        """
        return int(m.log(self.size, 2))

    def insert(self, item):
        """
        Complexity of insertion:
            Append = O(1)
            Bubble up = O(depth) = O(logN)

            Total complexity = O(logN)
        Args:
            item: Int item to insert

        Returns:

        """
        self.array.append(item)
        self.size += 1
        self._bubble_up(self.size)

    def delete_min(self):
        """
        Complexity of deleting min value:
            Shifting + Reducing size = O(1)
            Percolate down = O(depth) = O(logN)

            Total Complexity = O(logN)
        Returns:

        """
        self.array[1] = self.array[self.size]
        del self.array[self.size]
        self.size -= 1
        self._percolate_down(1)

    def build_heap(self, item_array):
        """
        Complexity of building head from a list of items:
            Algorithm:
            Start at index N/2 and percolate down for each indices
            [N/2, (N/2)-1,...,1]. All items below N/2 are leaves.

            Total Complexity = O(N)

            Proof:
            Assume a perfect binary heap.
            For each index, we do 2 comparision, 1 swapping followed
            by down percolation. Maximum depth we percolate to is
            exactly the height of that index.

            Max Operations for each index =
                    (2 comparison + Swapping) * height of index
            Total Max Operations =
                    (2 comparison + Swapping) * Sum of heights of all indices
            (Leaf element has height 0)
            Thus,
                Total Complexity = O(Sum of heights of all indices)

            Consider a perfect binary heap of height h containing 2^(h+1) - 1
            elements.

            Sum of heights of layer i       =  Number of items * height of i
                                    i = 0   =  2^i * (h - i) = h
                                    i = 1   = 2*i * (h - i) = 2*(h - 1)
                                    ...
                 S = h + 2(h-1) + 4(h-2) + 8(h-3) + ... + 2^(h-1)(1)
                2S =     2(h)   + 4(h-1) + 8(h-2) + 16(h-3) + ... + 2^h(1) i

            S = -h (2 + 4 + 8 + ... + 2^h) = -h - 1 + (1 + 2 + 4 + ... + 2^h)
            Thus sum is given by,
                    S = 2^(h+1) - 1 - (h+1)     (Using sum of geometric series)
            Similarly for binary heap with 1 leaf element at height h,
                    S = 2^h - 1
            Thus for a given height h of binary heap, bounds on S is given by:
                    2^h - 1 <= S <= 2^(h+1) - 1 - (h+1)

            Above result can be succinctly also represented as,
                    S = N - b(N),  b(N) is 1's in binary representation of N

            Thus,
                Total Complexity of building heap from a list of items is O(N)
                and uses at most 2*N comparisons.

        Args:
            item_array: List of items

        Returns:

        """
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

    def _get_indices(self, layer, max_width):
        num_indices = 2**layer
        list_indices = [None]*num_indices
        list_indices[0] = max_width//(2*num_indices)

        for i in range(1, num_indices):
            list_indices[i] = list_indices[0]*(1 + 2*i)

        return list_indices

    def _print_tree(self, max_char=2):      # max_char in the item
        depth = self._depth()
        result = ""
        layer = 0
        max_width = 2**(depth + max_char)

        elements = [1]
        while layer <= depth:
            str_data = " " * max_width
            indices = self._get_indices(layer, max_width)
            len_indices = len(indices)

            if len_indices > 1:
                str_underscore = " " * max_width
                str_bar = " " * max_width
                for i in range(len_indices // 2):
                    start = indices[2 * i]
                    end = indices[2 * i + 1]
                    str_underscore = str_underscore[:start + 1] + \
                            str_underscore[start + 1:end].replace(" ", "_") + \
                            str_underscore[end:]

                    str_bar = str_bar[:start] + \
                            str_bar[start:start + 1].replace(" ", "|") + \
                            str_bar[start + 1:end] + \
                            str_bar[end:end + 1].replace(" ", "|") + \
                            str_bar[end + 1:]

                result += str_underscore + "\n" + str_bar + "\n"

            for i in range(len_indices):
                if elements[i] is not None:
                    index = indices[i]
                    str_data = str_data[:index] + \
                           str_data[index:index + 1].\
                               replace(" ", str(self.array[elements[i]])) + \
                           str_data[index + 1:]

            count_elements = len(elements)
            for i in range(count_elements):
                element = elements[0]
                if element is not None:
                    if 2*element + 1 <= self.size:
                        elements.append(2*element)
                        elements.append(2*element + 1)
                    elif 2*element == self.size:
                        elements.append(2*element)
                        elements.append(None)
                    else:
                        elements.append(None)
                        elements.append(None)
                elements.pop(0)

            layer += 1
            result += str_data + "\n"

        return result


if __name__ == "__main__":
    my_binary_heap = BinaryHeap()
    my_binary_heap.build_heap([10,9,8,7,6,5,4,3,2,1,0])
    my_binary_heap.insert(11)
    my_binary_heap.delete_min()

    print(my_binary_heap)
