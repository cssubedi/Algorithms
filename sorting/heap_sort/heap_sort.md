### Heap sort
Heapsort uses binary heap to sort the elements. It first builds heap from the input list of elements and then performs $N$ "delete min" operations. In order to avoid creating new list, the deleted minimum (after each "delete min" operation) is swapped with the last element of the heap. The delete_min method of BinaryHeap class is thus modified to allow such functionality.

##### Worst case complexity:
Build heap performs in $O(N)$. Each of the $N$ delete min operations, in the worst case, performs in $O(logN)$; as the root element is percolated all the way down to the leaf.

Worst case complexity = $O(NlogN)$

##### Average case complexity:
The average case complexity analysis of Heap sort is pretty involved. Here, a lower bound of $2NlogN - O(NloglogN)$ is established using simple mathematical tool. Using more complex analytical tools, a tighter bound of $2NlogN - O(N)$ can be established.

Consider an array of a random permutation of $N$ distinct elements. A lower bound on the number of binary heaps $H$, that can made from $N$ elements, can be shown to be $H > (N/(4e))^N$.

Since, build heap runs in $\Theta(N)$ on average, we need to only show bound on "delete min" operations. Each heap sort is associated with a sequence $D: d_1, d_2,...,d_N$, where $d_i$ is the depth to which $ith$ root element is percolated down to, while performing $2d_i$ comparisons. The cost associated with these "delete min" operations for a particular $D$ is given as,
$$C_D = \sum_{i=1}^{N} d_i$$
Number of comparisons  = $2C_D$

Since, each depth $d$ contains at most $2^d$ elements, total number of unique "delete min" sequences for a particular $D$ sequence is given as,
$$S_D = 2^{d_1} 2^{d_2} 2^{d_3}... 2^{d_N} = 2^{C_D}$$
The value of $d_i$ lies between $1$ and $log(N)$, giving at most $(logN)^N$ possible D sequences. (Actually, it lies between $1$ and $log(N-i)$, but we set an upper bound). Furthermore, there are $NlogN-N+1$ different values of $C_D$ (multiple $D$ sequences can give same $C_D$).   
Let's choose a cost value of $C_D$ as M. How many of the $D$ sequences are associated with cost $M$?
We set an upper bound $(logN)^N$, i.e all the possible $D$ sequences. Each of those sequences has further at most $2^M$ possible "delete min" sequences. Thus, the number of distinct "delete min" sequences that require exactly M cost is at most
$$(logN)^N 2^M$$

Consequently, the number of heaps with cost less than $M$ is at most
$$\sum_{i=1}^{M-1} (logN)^N 2^i = (logN)^N \sum_{i=1}^{M-1} 2^i = (logN)^N (2^M - 2)<(logN)^N 2^M$$

Now, for $M = NlogN - O(NloglogN)$, the number of heaps is less than $(N/16)^N$, which is a tiny fraction of total number of possible heaps, $H > (N/(4e))^N$. Hence, average number of comparisons must be at least
$$2M = 2NlogN - O(NloglogN)$$
Even though the analysis looks complex, what we have done here is basically chose a value and argued that the average must be greater than this because, there are very few values less than it. In other words, for a list $[1,2,3,4,5,6]$, the average must be greater than 2 because out of 6 values only one value is less than 2.
