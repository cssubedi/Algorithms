## Internal Sorting Algorithms

The directory contains python implementation of internal sorting algorithms along with the analyses and proofs. The focus is given on the analyses of algorithms instead of just their implementations. Please keep in mind that the code written is only intended for academic exercise.

The following books were referenced for analytical proofs:
* [Introduction to Algorithms](https://www.amazon.com/Introduction-Algorithms-3rd-MIT-Press/dp/0262033844)
* [Data Structures and Algorithms Analysis in Java](https://www.amazon.com/Structures-Algorithm-Analysis-Java-Allen/dp/0273752111)

Here is a run-time plots of the implemented sorting algorithms. You should observe that bubble sort, selection sort and insertion sort are running closer to N^2, while shell sort, heap sort, merge sort and quick sort are running closer to NlogN.
![alt tag](https://github.com/cssubedi/Algorithms/blob/master/sorting/analysis/figures/run_time_logplot.png)
![alt tag](https://github.com/cssubedi/Algorithms/blob/master/sorting/analysis/figures/run_time_plot.png)

#### Usage:
```
python sort.py -h
usage: sort.py [-h]
               [--algorithm {bubble sort,selection sort,insertion sort,shell sort,heap sort,merge sort,quick sort}]
               [--items ITEMS] [--sequence {shell,hibbard,knuth}]

Parses arguments for sorting

optional arguments:
  -h, --help            show this help message and exit
  --algorithm {bubble sort,selection sort,insertion sort,shell sort,heap sort,merge sort,quick sort}
                        Choose a sorting algorithm.
  --items ITEMS         Specify items to sort.
  --sequence {shell,hibbard,knuth}
                        If using Shell sort, specify the sequence to use.
```

#### Example:
```
$ python sort.py

Algorithm used: insertion sort

Unsorted list: [9, 39, 36, 64, 82, 51, 66, 58, 15, 63]

Sorted list: [9, 15, 36, 39, 51, 58, 63, 64, 66, 82]

```
```
$ python sort.py --algorithm="shell sort" --items=[5,3,6,2,1,8,3,0,11,2] --sequence="knuth"

Algorithm used: shell sort

Unsorted list: [5,3,6,2,1,8,3,0,11,2]

Sorted list: [0, 1, 2, 2, 3, 3, 5, 6, 8, 11]


```
