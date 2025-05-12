# Task 1: Analyzing Time Complexity of Algorithms

import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

    items_greater = []
    items_lower = []

    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

random_list = [random.randint(0, 10000) for _ in range(1000)]

bubble_list = random_list.copy()
merge_list = random_list.copy()
quick_list = random_list.copy()

bubble_time = measure_time(bubble_sort, bubble_list)
merge_time = measure_time(merge_sort, merge_list)
quick_time = measure_time(lambda arr: quick_sort(arr), quick_list)

times = {'Bubble Sort': bubble_time, 'Merge Sort': merge_time, 'Quick Sort': quick_time}

plt.bar(times.keys(), times.values(), color=['red', 'blue', 'green'])
plt.xlabel('Sorting Algorithm')
plt.ylabel('Execution Time (seconds)')
plt.title('Sorting Algorithm Execution Time Comparison')
plt.show()

print("Execution times:")
for algo, time_taken in times.items():
    print(f"{algo}: {time_taken:.6f} seconds")

# Task 2: Recursive vs Iterative Approach

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]


def measure_execution_time(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    return result, end_time - start_time


test_values = [10, 20, 30, 40]
print("Execution Time Analysis:")
for n in test_values:
    print(f"\nFor n = {n}:")
    
    _, recursive_time = measure_execution_time(fibonacci_recursive, n)
    print(f"Recursive: {recursive_time:.6f} seconds")
    
    _, iterative_time = measure_execution_time(fibonacci_iterative, n)
    print(f"Iterative: {iterative_time:.6f} seconds")
    
    _, memoized_time = measure_execution_time(fibonacci_memoized, n)
    print(f"Memoized: {memoized_time:.6f} seconds")

# Task 3: Task 3: Visualizing Big-O Notation

import numpy as np
import matplotlib.pyplot as plt

def constant(n):
    return np.ones_like(n)

def logarithmic(n):
    return np.log2(n)

def linear(n):
    return n

def linear_log(n):
    return n * np.log2(n)

def quadratic(n):
    return n ** 2

def exponential(n):
    return 2 ** n

n_values = np.arange(1, 1001)

plt.figure(figsize=(10, 6))
plt.plot(n_values, constant(n_values), label='O(1)', color='blue')
plt.plot(n_values, logarithmic(n_values), label='O(log n)', color='green')
plt.plot(n_values, linear(n_values), label='O(n)', color='red')
plt.plot(n_values, linear_log(n_values), label='O(n log n)', color='purple')
plt.plot(n_values, quadratic(n_values), label='O(n^2)', color='orange')
plt.plot(n_values, exponential(n_values), label='O(2^n)', color='brown')

plt.yscale('log')
plt.xlabel('Input Size (n)')
plt.ylabel('Operations')
plt.title('Big-O Notation')
plt.legend()
plt.grid(True)
plt.show()
