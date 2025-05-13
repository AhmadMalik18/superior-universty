# Topic 2: Arrays & Strings

# Task 1: Implementing Custom Array Operations

class DynamicArray:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * self.capacity

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
    
    def insert_end(self, value):
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        self.array[self.size] = value
        self.size += 1
    
    def insert_at(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.size += 1
    
    def delete_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1
        if self.size > 0 and self.size == self.capacity // 4:
            self._resize(self.capacity // 2)
    
    def search(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                return i
        return -1
    
    def display(self):
        return [self.array[i] for i in range(self.size)]


dynamic_array = DynamicArray()
dynamic_array.insert_end(10)
dynamic_array.insert_end(20)
dynamic_array.insert_end(30)
dynamic_array.insert_at(1, 15)
dynamic_array.delete_at(2)
print("Array after operations:", dynamic_array.display())
print("Index of 15:", dynamic_array.search(15))
print("Index of 100:", dynamic_array.search(100))  

# Task 2: Finding the Longest Substring Without Repeating Characters

import time

def longest_substring_brute_force(s):
    max_length = 0
    longest_substring = ""
    
    for i in range(len(s)):
        seen = set()
        current_substring = ""
        
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            current_substring += s[j]
        
        if len(current_substring) > max_length:
            max_length = len(current_substring)
            longest_substring = current_substring
    
    return longest_substring, max_length

def longest_substring_sliding_window(s):
    char_index = {}
    left = max_length = 0
    longest_substring = ""
    
    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1
        
        char_index[s[right]] = right
        
        if right - left + 1 > max_length:
            max_length = right - left + 1
            longest_substring = s[left:right + 1]
    
    return longest_substring, max_length

def measure_time(func, s):
    start_time = time.time()
    result = func(s)
    end_time = time.time()
    return result, end_time - start_time


test_string = "abcabcbb"
brute_result, brute_time = measure_time(longest_substring_brute_force, test_string)
sliding_result, sliding_time = measure_time(longest_substring_sliding_window, test_string)

print("Brute Force Method:", brute_result, "Execution Time:", brute_time)
print("Sliding Window Method:", sliding_result, "Execution Time:", sliding_time)

# Task 3: Two-Dimensional Array – Image Rotation

def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for row in matrix:
        row.reverse()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_matrix(matrix)

for row in matrix:
    print(row)

   