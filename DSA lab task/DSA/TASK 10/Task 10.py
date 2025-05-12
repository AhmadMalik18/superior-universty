# Topic 10: Searching Algorithms

#Task 1: Implementing Linear Search and Binary Search

import time
import random
import matplotlib.pyplot as plt

# ---------------- Linear Search ----------------
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

# ---------------- Binary Search ----------------
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# ---------------- Timing Function ----------------
def measure_time(search_func, arr, target):
    start = time.time()
    search_func(arr, target)
    end = time.time()
    return end - start

# ---------------- Performance Comparison ----------------
sizes = [1000, 5000, 10000]
times_linear = []
times_binary = []

for size in sizes:
    target = -1  # value not in list to simulate worst-case
    arr = [random.randint(1, 100000) for _ in range(size)]
    sorted_arr = sorted(arr)

    times_linear.append(measure_time(linear_search, arr, target))
    times_binary.append(measure_time(binary_search, sorted_arr, target))

# ---------------- Plotting ----------------
plt.plot(sizes, times_linear, label='Linear Search', marker='o')
plt.plot(sizes, times_binary, label='Binary Search', marker='o')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Linear Search vs Binary Search Performance')
plt.legend()
plt.grid(True)
plt.show()

# ---------------- Test Cases ----------------
arr = [10, 23, 45, 70, 11, 15]
sorted_arr = sorted(arr)
print("Original List:", arr)
print("Sorted List:", sorted_arr)
print("Linear Search Index of 45:", linear_search(arr, 45))       # Output: 2
print("Binary Search Index of 45:", binary_search(sorted_arr, 45))  # Output: 4
print("Linear Search Index of 99:", linear_search(arr, 99))       # Output: -1
print("Binary Search Index of 99:", binary_search(sorted_arr, 99))  # Output: -1

# Task 2: Implementing Interpolation Search and Jump Search

import math

# ---------------- Jump Search ----------------
def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  # Optimal jump size is √n
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

# ---------------- Interpolation Search ----------------
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        # Estimate the position of the target
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

# ---------------- Performance Comparison ----------------
sizes = [1000, 5000, 10000]
times_jump = []
times_interpolation = []

for size in sizes:
    target = -1  # value not in list to simulate worst-case
    arr = sorted([random.randint(1, 100000) for _ in range(size)])

    times_jump.append(measure_time(jump_search, arr, target))
    times_interpolation.append(measure_time(interpolation_search, arr, target))

# ---------------- Plotting ----------------
plt.plot(sizes, times_binary, label='Binary Search', marker='o')
plt.plot(sizes, times_jump, label='Jump Search', marker='o')
plt.plot(sizes, times_interpolation, label='Interpolation Search', marker='o')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Search Algorithm Performance Comparison')
plt.legend()
plt.grid(True)
plt.show()

# ---------------- Test Cases ----------------
arr = [1, 3, 5, 7, 9, 11, 13, 15]
print("Jump Search Index of 7:", jump_search(arr, 7))  # Output: 3
print("Interpolation Search Index of 7:", interpolation_search(arr, 7))  # Output: 3
print("Jump Search Index of 10:", jump_search(arr, 10))  # Output: -1
print("Interpolation Search Index of 10:", interpolation_search(arr, 10))  # Output: -1

# Task 3: Implementing Exponential Search and Fibonacci Search

# ---------------- Exponential Search ----------------
def exponential_search(arr, target):
    if arr[0] == target:
        return 0

    n = len(arr)
    bound = 1
    while bound < n and arr[bound] < target:
        bound *= 2

    # Perform binary search in the found range
    return binary_search(arr[:min(bound, n)], target)

# ---------------- Fibonacci Search ----------------
def fibonacci_search(arr, target):
    n = len(arr)
    fib2 = 0  # (m-2)'th Fibonacci number
    fib1 = 1  # (m-1)'th Fibonacci number
    fib = fib2 + fib1  # m'th Fibonacci number

    # Find the smallest Fibonacci number greater than or equal to n
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1

    offset = -1

    while fib > 1:
        i = min(offset + fib2, n - 1)

        if arr[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i

    if fib1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1

    return -1

# ---------------- Performance Comparison ----------------
sizes = [1000, 5000, 10000]
times_exponential = []
times_fibonacci = []

for size in sizes:
    target = -1  # value not in list to simulate worst-case
    arr = sorted([random.randint(1, 100000) for _ in range(size)])

    times_exponential.append(measure_time(exponential_search, arr, target))
    times_fibonacci.append(measure_time(fibonacci_search, arr, target))

# ---------------- Plotting ----------------
plt.plot(sizes, times_binary, label='Binary Search', marker='o')
plt.plot(sizes, times_jump, label='Jump Search', marker='o')
plt.plot(sizes, times_interpolation, label='Interpolation Search', marker='o')
plt.plot(sizes, times_exponential, label='Exponential Search', marker='o')
plt.plot(sizes, times_fibonacci, label='Fibonacci Search', marker='o')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Search Algorithm Performance Comparison')
plt.legend()
plt.grid(True)
plt.show()

# ---------------- Test Cases ----------------
arr = [2, 4, 8, 16, 32, 64, 128]
print("Exponential Search Index of 32:", exponential_search(arr, 32))  # Output: 4
print("Fibonacci Search Index of 32:", fibonacci_search(arr, 32))  # Output: 4
print("Exponential Search Index of 10:", exponential_search(arr, 10))  # Output: -1
print("Fibonacci Search Index of 10:", fibonacci_search(arr, 10))  # Output: -1