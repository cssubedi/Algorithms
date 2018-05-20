### Insertion sort
Insertion sort works by inserting $ith$ element on sorted $i-1$ elements, for $0 < i < N$. Thus there are $N-1$ passes in total. Insertion sort is in-place and stable sorting algorithm. The implementation consists of nested loops. Outer loop takes $N-1$ iterations. The inner loop takes at max $i$ iterations for the $ith$ pass. Since only one assignment is performed, a shift operation requires approximately a third of the processing work of an exchange operation (like in bubble sort).

##### Worst-case: The list is in reverse order
In such case, the inner loop takes $i$ iterations for the $ith$ pass. Thus, the total number of iterations is
$$1 + 2 + 3 + .... + N-1  = N(N-1)/2 = \Theta(N^2)$$

##### Best-case: The list is already sorted
If the input array is sorted, then the inner loop fails immediately. Thus,the total number of iterations is
$$\Theta(N)$$
Hence, the complexity of insertion sort lies between $\Theta(N)$ and $\Theta(N^2)$, depending on the input.

##### Average-case:
Inversions are any ordered pair $(i, j)$ in the input array $A$ such that $i < j$ but $A[i] > A[j]$. Each swap removes only one inversion. Thus, the complexity of any sorting algorithm, that performs swapping (explicitly like bubble sort or implicitly like insertion sort) of adjacent elements, is proportional to the number of inversions on the input. Under the assumptions that there are no duplicates, $N > 1$ and any permutation of $N$ distinct elements is equally likely, we can compute average number of inversions in an array of $N$ distinct elements.

Let $L$ be the list of elements and $L_r$ its reverse order list. Then, any element pair $(x, y)$ such that $y > x$, is an inversion in exactly one of $L$ or $L_r$. Number of ways you can choose 2 distinct elements from $N$ is given as,
$$
C_{2}^{N}
= {N! \over (N-2)! * 2!} = {N(N-1)\over2}
$$
Total number of inversion in $L$ and $L_r$ = $N(N-1)/2$

Average number of inversions = $N(N-1)/4$

Any algorithm (not only insertion sort) that sorts by exchanging adjacent elements requires $\Omega(N^2)$ time on average. This is the case because on average there are $N(N-1)/4 = \Omega(N^2)$ inversions.

##### Sum up the running time:
* Worst case = $\Theta(N^2)$  
* Best case = $\Theta(N)$   
* Average case for random array = $\Theta(N^2)$   
* "Almost sorted" case: $\Theta(N)$     

If speaking for all cases in general, it runs in $O(N^2)$
