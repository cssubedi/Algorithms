### Radix sort
Radix sort is basically multi-pass Bucket sort. If the size of elements in the input array is relatively small, Bucket sort can be performed sequentially on each indices or digits. Consider Bucket sorting $N$ integers that are between 0 and 999. This would require the array $buckets$ of size 999, which is not ideal. Instead, we perform three Bucket sorts on each digits starting from the least significant digit and use a 10-size array $buckets$.

Unlike Bucket sort, more than one element that are different could fall on the same bucket.   Thus we maintain lists. Furthermore, since each pass is stable, ordering determined in $(k-1)th$ pass is retained in future $k$th pass.

Complexity = $O(p(N + M))$, where $p$ is the number of passes (max length of elements), $N$ is the length of input array and $B$ is the number of buckets.
