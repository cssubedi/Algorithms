### Shell sort
Shell sort improves on insertion sort using the fact that insertion sort runs faster on "somewhat" sorted array. It performs several insertion sorts on different sub-sequences of elements. Shell sort uses a sequence, $h_1, h_2, h_3, ..., h_t$, called increment sequence, such that $h_1 = 1$. Shell sort is an in-place and not-stable sorting algorithm.

Shell sort begins with a suitable $h_k$ increment and performs insertion sort on the elements spaced $h_k$, such that, for every $i$ we have $A[i] < A[i+h_k]$. The array is then said to be $h_k$-sorted. The step is repeated for the next increment $h_k-1$ until $h_1$. Because the comparison distance between elements decreases until the last phase, shell short is sometimes referred to as "diminishing increment sort".

An important property to remember is that an $h_k$ sorted array that is then $h_k-1$ sorted remains $h_k$ sorted. That is, work done on early phase is not undone by later phase.

##### Increment Sequences:
Shell sequence: $N/2, N/4, ... , 1$ (repeatedly divide by 2)   
Hibbard  sequence: $1, 3, 7, ..., 2^k -1$
Knuth sequence: $1, 4, 13, ..., (3^k-1)/2$   
Sedgewick sequence: $1, 5, 19, 41, 109, ...$

The running time of Shell sort depends on the choice of increment sequence. The average-case analysis is still an open problem, except for the most trivial sequence. The worst-case complexity for Shell sequence is discussed below:

##### Worst-case running time of Shell sort using shell sequences is $\Theta(N^2)$
For such tight bound, we need to show the following:
* Upper bound is $O(N^2)$
* For some input it actually takes $\Omega(N^2)$

Consider a case where $N$ is a power of 2 such that all increments are even except 1. Let's place $N/2$ largest numbers in the odd positions and $N/2$ smallest numbers in the even positions in sorted order.

    Example:
    Start           1 9 2 10 3 11 4 12 5 13 6 14 7 15 8 16
    After 8-sort    1 9 2 10 3 11 4 12 5 13 6 14 7 15 8 16
    After 4-sort    1 9 2 10 3 11 4 12 5 13 6 14 7 15 8 16
    After 2-sort    1 9 2 10 3 11 4 12 5 13 6 14 7 15 8 16
    After 1-sort    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

As shown above, none of the insertion sort, except $h_1$, changes the list. It is easy to see that for any Shell sequence, you can always come up with an input for which shell sort becomes merely an insertion sort.

All elements in even positions $i$, moves $i-1$ positions during $h_1$-sort. Odd positioned elements do not have to move. Thus, to place $N/2$ elements in correct place requires

      1 + 2 + 3 + 4 + 5 + 6 + 7 = 28 operations.

For general $N$,   
$$\sum_{i=1}^{N/2} i-1 =  \Omega(N^2)$$

Now, we show the upper bound. At each $h_k$ sort, about $N/h_k$ elements are insertion sorted. Since insertion sort is worst-case $O(N^2)$, total cost of each pass is $O((N/h_k)^2) = O(N^2/h_k)$.

Total cost over all passes is given by,
$$O(\sum_{i=1}^{t} N^2/h_i) = O(N^2 * \sum_{i=1}^{t} 1/h_i)$$

Since, $\sum_{i=1}^{t} 1/h_i$ is a geometric series with first element 1, $\sum_{i=1}^{t} 1/h_i < 2$

Hence, total cost over all passes = $O(N^2)$. And the proof is complete!

There are couple of optimization that can be performed on this sequence:
* It is easy to observe that since increments are not relatively prime, chances are same elements will be traced (e.g: 8, 4, 2 increments)

* Smaller is the comparison distance, lesser effect does it have on the list. We want to maintain larger distance comparison.

Hence Hibbard, Knuth, Sedgewick and other sequences were developed to increase the performance of Shell sort.
