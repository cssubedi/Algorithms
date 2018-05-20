### Selection sort
Selection sort is an improvement on bubble sort because elements are moved more than 1 slot per step. Selection sort works by scanning the array, selecting the smallest element and swapping with $A[0]$. You repeat the process by scanning the remaining  array, selecting the smallest and performing the swapping until last element is reached.

Selection sort is not stable as the relative position of duplicate elements might change. It is an in-place sorting algorithm that only needs $O(1)$ extra space to store "min_index" temporary variable.

Running time = $O(N^2)$
