# Topic 9: Sorting Algorithms

# Task 1: Implementing and Analyzing Sorting Algorithms
import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    res = arr.copy()
    for i in range(n):
        for j in range(0, n-i-1):
            if res[j] > res[j+1]:
                res[j], res[j+1] = res[j+1], res[j]
    return res

def selection_sort(arr):
    res = arr.copy()
    n = len(res)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if res[j] < res[min_idx]:
                min_idx = j
        res[i], res[min_idx] = res[min_idx], res[i]
    return res

def insertion_sort(arr):
    res = arr.copy()
    for i in range(1, len(res)):
        key = res[i]
        j = i - 1
        while j >= 0 and key < res[j]:
            res[j + 1] = res[j]
            j -= 1
        res[j + 1] = key
    return res



def measure_time(sort_func, arr):
    start = time.time()
    sort_func(arr)
    end = time.time()
    return end - start

def generate_random_list(size):
    return [random.randint(1, 10000) for _ in range(size)]

sizes = [100, 500, 1000, 2000]
times_bubble = []
times_selection = []
times_insertion = []

for size in sizes:
    test_list = generate_random_list(size)
    times_bubble.append(measure_time(bubble_sort, test_list))
    times_selection.append(measure_time(selection_sort, test_list))
    times_insertion.append(measure_time(insertion_sort, test_list))


plt.plot(sizes, times_bubble, label='Bubble Sort', marker='o')
plt.plot(sizes, times_selection, label='Selection Sort', marker='o')
plt.plot(sizes, times_insertion, label='Insertion Sort', marker='o')

plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Sorting Algorithms Performance Comparison')
plt.legend()
plt.grid(True)
plt.show()
arr = [64, 25, 12, 22, 11]
print("Bubble Sort:", bubble_sort(arr))
print("Selection Sort:", selection_sort(arr))
print("Insertion Sort:", insertion_sort(arr))


#Task 2: Implementing Quick Sort and Merge Sort with Performance Comparison

import time
import random
import matplotlib.pyplot as plt


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def measure_time(sort_func, arr):
    start = time.time()
    sort_func(arr)
    end = time.time()
    return end - start


def generate_random_list(size):
    return [random.randint(1, 100000) for _ in range(size)]

sizes = [1000, 5000, 10000]
times_quick = []
times_merge = []

for size in sizes:
    test_list = generate_random_list(size)
    times_quick.append(measure_time(quick_sort, test_list))
    times_merge.append(measure_time(merge_sort, test_list))


plt.plot(sizes, times_quick, label='Quick Sort', marker='o')
plt.plot(sizes, times_merge, label='Merge Sort', marker='o')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Quick Sort vs Merge Sort Performance')
plt.legend()
plt.grid(True)
plt.show()


arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
print("Quick Sort:", quick_sort(arr))
print("Merge Sort:", merge_sort(arr))

# Task 3: Implementing Heap Sort and Counting Sort for Large Datasets

import time
import random
import matplotlib.pyplot as plt

# ---------------- Heap Sort ----------------
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    res = arr.copy()
    n = len(res)
    for i in range(n // 2 - 1, -1, -1):
        heapify(res, n, i)
    for i in range(n - 1, 0, -1):
        res[i], res[0] = res[0], res[i]
        heapify(res, i, 0)
    return res

# ---------------- Counting Sort ----------------
def counting_sort(arr):
    if not arr:
        return []
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    result = []
    for i, c in enumerate(count):
        result.extend([i] * c)
    return result

# ---------------- Timing Function ----------------
def measure_time(sort_func, arr):
    start = time.time()
    sort_func(arr)
    end = time.time()
    return end - start

# ---------------- Performance Test ----------------
sizes = [10000, 50000, 100000]
times_heap = []
times_counting = []

for size in sizes:
    # Generate random datasets
    list_heap = [random.randint(1, 100000) for _ in range(size)]
    list_counting = [random.randint(0, 1000) for _ in range(size)]  # counting sort needs limited range

    times_heap.append(measure_time(heap_sort, list_heap))
    times_counting.append(measure_time(counting_sort, list_counting))

# ---------------- Plotting ----------------
plt.plot(sizes, times_heap, label='Heap Sort', marker='o')
plt.plot(sizes, times_counting, label='Counting Sort', marker='o')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Heap Sort vs Counting Sort Performance')
plt.legend()
plt.grid(True)
plt.show()

# ---------------- Example Input/Output ----------------
arr1 = [4, 10, 3, 5, 1]
arr2 = [1, 4, 1, 2, 7, 5, 2]
print("Heap Sort:", heap_sort(arr1))
print("Counting Sort:", counting_sort(arr2))
