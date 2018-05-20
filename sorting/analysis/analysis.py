import matplotlib.pyplot as plt

bubble_sort_data = "~/Algorithms/sorting/analysis/data/bubble_sort.txt"

selection_sort_data = "~/Algorithms/sorting/analysis/data/selection_sort.txt"

insertion_sort_data = "~/Algorithms/sorting/analysis/data/insertion_sort.txt"

shell_sort_data = "~/Algorithms/sorting/analysis/data/shell_sort.txt"

heap_sort_data = "~/Algorithms/sorting/analysis/data/heap_sort.txt"

merge_sort_data = "~/Algorithms/sorting/analysis/data/merge_sort.txt"

quick_sort_data = "~/Algorithms/sorting/analysis/data/quick_sort.txt"

number_elements = [i for i in range(0, 10001, 5)]

with open(bubble_sort_data, "r") as file:
    lines = file.readlines()
    bubble_run_times = [float(data.strip()) for data in lines]

with open(selection_sort_data, "r") as file:
    lines = file.readlines()
    selection_run_times = [float(data.strip()) for data in lines]

with open(insertion_sort_data, "r") as file:
    lines = file.readlines()
    insertion_run_times = [float(data.strip()) for data in lines]

with open(shell_sort_data, "r") as file:
    lines = file.readlines()
    shell_run_times = [float(data.strip()) for data in lines]

with open(heap_sort_data, "r") as file:
    lines = file.readlines()
    heap_run_times = [float(data.strip()) for data in lines]

with open(merge_sort_data, "r") as file:
    lines = file.readlines()
    merge_run_times = [float(data.strip()) for data in lines]

with open(quick_sort_data, "r") as file:
    lines = file.readlines()
    quick_run_times = [float(data.strip()) for data in lines]

plt.figure(1)
plt.plot(number_elements, bubble_run_times, label="Bubble Sort")
plt.plot(number_elements, selection_run_times, label="Selection Sort")
plt.plot(number_elements, insertion_run_times, label="Insertion Sort")
plt.plot(number_elements, shell_run_times, label="Shell Sort")
plt.plot(number_elements, heap_run_times, label="Heap Sort")
plt.plot(number_elements, merge_run_times, label="Merge Sort")
plt.plot(number_elements, quick_run_times, label="Quick Sort")

plt.xlabel('N')
plt.ylabel('Run time')
plt.title('Complexity Analysis of Sorting algorithms')
plt.legend(loc="upper left")
plt.grid(True)

plt.figure(2)
plt.loglog(number_elements, bubble_run_times, label="Bubble Sort")
plt.loglog(number_elements, selection_run_times, label="Selection Sort")
plt.loglog(number_elements, insertion_run_times, label="Insertion Sort")
plt.loglog(number_elements, shell_run_times, label="Shell Sort")
plt.loglog(number_elements, heap_run_times, label="Heap Sort")
plt.loglog(number_elements, merge_run_times, label="Merge Sort")
plt.loglog(number_elements, quick_run_times, label="Quick Sort")

plt.xlabel('N')
plt.ylabel('Run time')
plt.title('Complexity Analysis of Sorting algorithms')
plt.legend(loc="upper left")
plt.grid(True)

plt.show()
