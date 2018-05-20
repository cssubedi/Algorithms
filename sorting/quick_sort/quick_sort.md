### Quick sort
Quick sort is also a recursive divide and conquer algorithm. It works by partitioning list into left and right sub-lists using a pivot element, such that elements in left $<=$ elements in right. It recursively sorts each sub-lists and then concatenates two sublists along with pivot
element. It is a stable and in-place sorting algorithm.
##### Choosing the pivot element:
* First element: Terrible idea! If the list is sorted or reverse sorted, then all elements go into one of the sub-lists only. $O(N^2)$ time spent doing nothing!
* Random element: A safe option, unless random number generator is flawed. Furthermore, random number generation is rather expensive.
* Median: The best pivot you could choose. However, it is expensive to calculate median of elements.
* Median-of-three: An estimate of median can be obtained by taking median of the three numbers: first, middle and last. The implementation uses this pivot.

##### Performing the partition:
Partition can be performed in $O(N)$. Here is an illustration of the strategy.    
Initialize $i$ and $j$ variables to first and second last element respectively.

    Initial list
    i-->                                         <--j
    3       5      4       2       3        6       7       1

Swap last element and the pivot element (median of 3, 3, 1 = 3).

    i-->                                         <--j
    3       5      4       2       1        6       7       3

Move $i$ towards right until it finds element greater than or equal to the pivot, in which case stop. Simultaneously move $j$ towards left until it finds element less than or equal to the pivot, in which case stop.

    i-->                        <--j
    3       5      4       2       1        6       7       3

When $i$ and $j$ both stop and $i$ is to the left of $j$, swap the elements.

    i-->                        <--j
    1       5      4       2       3        6       7       3

            i-->        <--j
    1       5      4       2       3        6       7       3

            i-->        <--j
    1       2      4       5       3        6       7       3

         <--j      i-->
    1       2      4       5       3        6       7       3


At this moment, $i$ and $j$ have crossed. The final step is to swap the pivot element that was placed in the end of the list with the element where $i$ is pointing.


    1       2      3       5       3        6       7       4
Thus the partitions are:

    [1       2]      [3]       [5       3        6       7       4]

As you might have noticed, strategy works with duplicate entries as well.

Since quick sort is recursive, recurrence relation will be used for the complexity analysis. Assume pivot is chosen randomly from the element. Then, since the partition step performs in linear time, the general recurrence relation is given by,
$$T(0) = T(1) = O(1)$$
$$T(N) = T(i) + T(N-i-1) + N$$

##### Worst case complexity:
Worst case is the case when pivot chosen is the smallest element all the time. The recurrence relation for such case is:
$$T(N) = T(N-1) + N$$
$$T(N-1) = T(N-2) + N-1$$
$$...$$
$$T(2) = T(1) + 2$$
Telescoping the sum,
$$T(N) = \sum_{i=2}^{N} i = \Theta(N^2)$$

##### Best case complexity:
Best case is the case when the list is already sorted or the randomly chosen pivot is always the
median. The recurrence relation for such case is:
$$T(N) = 2T(N/2) + N$$
The relation is exactly the same as merge sort. Hence,
$$T(N) = \Theta(NlogN)$$

##### Average case complexity:
Since the pivot is chosen randomly from elements, we assume that each of the $N$ possible sizes of the partition is equally likely.
$$E[T(i)] = E[T(N-i-1)] = {1 \over N}\sum_{i=0}^{N-1} i$$
Thus, the recurrence relation is given by,
$$T(N) = {2 \over N}\sum_{i=0}^{N-1} T(i) + N$$
$$NT(N) = 2\sum_{i=0}^{N-1} T(i) + N^2$$
$$(N-1)T(N-1) = 2\sum_{i=0}^{N-2}T(i) + (N-1)^2$$
Subtracting them,
$$NT(N) - (N-1)T(N-1) = 2T(N-1) + 2N - 1$$
$$NT(N) = (N+1)T(N-1) + N$$
Rearranging the terms,
$${T(N) \over N+1} = {T(N-1) \over N} + {1 \over N+1}$$
$${T(N-1) \over N} = {T(N-2) \over N-1} + {1 \over N}$$
$$...$$
$${T(1) \over 2} = {T(0) \over 1} + {1 \over 2}$$
Telescoping the sum,
$${T(N) \over N+1} = {T(0) \over 1} + \sum_{i=2}^{N+1} {1 \over i} = O(log(N))$$
Thus,
$$T(N) = O(NlogN)$$
