#Task 1: Optimized Bubble Sort Implementation
def optimized_bubble_sort(arr):
    n = len(arr)
    total_swaps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                total_swaps +=1
                if not swapped:
                    break
    return total_swaps
arr = [7,8,56,42,45]
print(optimized_bubble_sort(arr))


#Task 2: Count and Compare Swaps in Bubble Sort vs. Insertion Sort
def bubble_sort(arr):
    n = len(arr)
    swap_count = 0 
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j + 1], arr[j]
                swap_count += 1
    return swap_count
def insertion_sort(arr):
    n = len(arr)
    swaps_count = 0 
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
            swaps_count += 1
        arr[j+1] = key
    return swaps_count
arr2=[56,78,12,12]
bubble_arr = arr2.copy()
bubble_swaps = bubble_sort(bubble_arr)
insertion_arr = arr2.copy()
insertion_swaps = insertion_sort(insertion_arr)
print(f"Bubbled Sort Swaps: {bubble_swaps}")
print(f"Insertion Sort Swaps: {insertion_swaps}")
if bubble_swaps < insertion_swaps:
    print("Bubble sort performaed fewer swaps.")
else:
    print("Insertion sort performsed fewer swaps.")



