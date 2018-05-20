### Bucket sort
Bucket sort is a linear time stable sorting algorithm that uses an additional information about the input array of items, the maximum value $M$. Bucket sort works by keeping an array $buckets$ of size $M$ with each elements initialized to $0$'s. The input array is scanned and the array $buckets$ is updated for each $item$ as such $buckets[item] \mathrel{{+}{=}} 1$. The array $buckets$ is then scanned to output the sorted array.

Bucket sort takes $O(N)$ time to scan the element in the array and update the buckets. It takes $O(M)$ time to scan the buckets and output the sorted array.

Thus, the complexity is $O(N + M)$. If $M$ is $O(N)$, then  
Complexity = $O(N)$

To come in terms with $\Omega(NlogN)$ running time complexity of comparison based sorting algorithm, understand that the step, $buckets[item] \mathrel{{+}{=}} 1$, is actually performing $M$ way comparison in one step.
