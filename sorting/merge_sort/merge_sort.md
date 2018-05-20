### Merge sort
Merge sort is a recursive algorithm based on divide and conquer strategy. It works by diving the input array into two, recursively sorting each left and right half and then merging two halves.
Merge sort is not in-place sorting algorithm as it requires $O(N)$ memory space for temporary list. It is a stable sorting algorithm that maintains the relative position of duplicate elements (if implemented as such).

Running time of Merge sort can be obtained from the recurrence relation. Let $T(N)$ be the running time to sort $N$ items. Since it takes linear time to merge two lists, the recurrence relation is given by,
$$T(1) = O(1)$$
$$T(N) = 2T(N/2) + N$$

Solving for $T(N)$,
$${T(N) \over N} = {T(N/2) \over N/2} + 1$$
$${T(N/2) \over N/2} = {T(N/4) \over N/4} + 1$$
$$...$$

Adding both sides,

$$
{T(N) \over N} + {T(N/2) \over N/2} + ... + {T(2) \over 2} = {T(N/2) \over N/2} + {T(N/4) \over N/4} + ... + {T(1) \over 1} + {1 + 1 + ...  + 1}
$$

Telescoping the sum,
$${T(N) \over N} = {T(1) \over 1} + logN$$
Thus,
$$T(N) = \Theta(NlogN)$$

A major drawback of the merge sort is that it needs linear extra memory (though theoretically possible in $O(1)$).
