# Topic 11: Hashing & Hash Tables

# Task 1: Implementing a Simple Hash Table with Collision Handling

class HashTableChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Initialize the hash table with empty lists for chaining

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Update value if key already exists
                return
        self.table[index].append([key, value])  # Append new key-value pair

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Key not found

    def delete(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return
        print(f"Key '{key}' not found.")

class HashTableOpenAddressing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Initialize the hash table with None
        self.deleted = object()  # Special marker for deleted slots

    def _hash(self, key):
        return hash(key) % self.size

    def _probe(self, index):
        return (index + 1) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        start_index = index
        while self.table[index] is not None and self.table[index] is not self.deleted:
            if self.table[index][0] == key:
                self.table[index] = (key, value)  # Update value if key already exists
                return
            index = self._probe(index)
            if index == start_index:
                raise Exception("Hash table is full.")
        self.table[index] = (key, value)

    def get(self, key):
        index = self._hash(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index] != self.deleted and self.table[index][0] == key:
                return self.table[index][1]
            index = self._probe(index)
            if index == start_index:
                break
        return None  # Key not found

    def delete(self, key):
        index = self._hash(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index] != self.deleted and self.table[index][0] == key:
                self.table[index] = self.deleted  # Mark as deleted
                return
            index = self._probe(index)
            if index == start_index:
                break
        print(f"Key '{key}' not found.")

# Testing the HashTable implementations
print("Testing HashTable with Chaining:")
ht_chaining = HashTableChaining(10)
ht_chaining.insert("name", "Alice")
ht_chaining.insert("age", 25)
print(ht_chaining.get("name"))  # Output: Alice
ht_chaining.delete("age")
print(ht_chaining.get("age"))  # Output: None

print("\nTesting HashTable with Open Addressing:")
ht_open = HashTableOpenAddressing(10)
ht_open.insert("name", "Alice")
ht_open.insert("age", 25)
print(ht_open.get("name"))  # Output: Alice
ht_open.delete("age")
print(ht_open.get("age"))  # Output: None


# Task 2: Implementing a Custom Hash Function and Analyzing Collisions

import matplotlib.pyplot as plt
from collections import Counter

# Custom hash function
def custom_hash(key):
    return sum(ord(c) for c in key) % 10

# Function to analyze collisions
def analyze_collisions(hash_function, keys, table_size):
    hash_table = [[] for _ in range(table_size)]
    collisions = 0

    for key in keys:
        index = hash_function(key)
        if hash_table[index]:  # Collision occurs if the slot is not empty
            collisions += 1
        hash_table[index].append(key)

    return collisions, hash_table

# Generate a dataset of keys
keys = [f"key{i}" for i in range(100)]  # Example dataset of 100 keys

# Analyze collisions for custom hash function
custom_collisions, custom_table = analyze_collisions(custom_hash, keys, 10)

# Analyze collisions for Python's built-in hash function
builtin_collisions, builtin_table = analyze_collisions(lambda key: hash(key) % 10, keys, 10)

# Print collision results
print(f"Collisions with custom hash function: {custom_collisions}")
print(f"Collisions with built-in hash function: {builtin_collisions}")

# Plot histogram of hash values for custom hash function
custom_hash_values = [custom_hash(key) for key in keys]
builtin_hash_values = [hash(key) % 10 for key in keys]

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(custom_hash_values, bins=10, edgecolor='black', alpha=0.7)
plt.title("Custom Hash Function Distribution")
plt.xlabel("Hash Value")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
plt.hist(builtin_hash_values, bins=10, edgecolor='black', alpha=0.7)
plt.title("Built-in Hash Function Distribution")
plt.xlabel("Hash Value")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

# Task 3: Implementing a Caching Mechanism using Hashing (LRU Cache)

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # Hash table for O(1) lookups
        self.head = Node(0, 0)  # Dummy head of the doubly linked list
        self.tail = Node(0, 0)  # Dummy tail of the doubly linked list
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove a node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node):
        """Add a node right after the head."""
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)  # Move the accessed node to the front
            self._add(node)
            return node.value
        return -1  # Key not found

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])  # Remove the old node
        node = Node(key, value)
        self._add(node)  # Add the new node to the front
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            # Remove the least recently used node
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

# Testing the LRUCache
print("Testing LRUCache:")
cache = LRUCache(2)
cache.put(1, "A")
cache.put(2, "B")
print(cache.get(1))  # Output: "A"
cache.put(3, "C")  # Removes least recently used key (2)
print(cache.get(2))  # Output: -1 (not found)
print(cache.get(3))  # Output: "C"
cache.put(4, "D")  # Removes least recently used key (1)
print(cache.get(1))  # Output: -1 (not found)
print(cache.get(4))  # Output: "D"